from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.services.supabase_client import supabase
import logging

logger = logging.getLogger("pem")
bearer = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer)):
    token = credentials.credentials

    try:
        user_resp = supabase.auth.get_user(token)
        if not user_resp or not user_resp.user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
        user_id = user_resp.user.id
    except HTTPException:
        raise
    except Exception as e:
        logger.warning("Token validation error: %s", e)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")

    try:
        res = supabase.table("profiles").select("*").eq("id", user_id).single().execute()
        if not res.data:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Account not found")
        return res.data
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Profile fetch error for user %s: %s", user_id, e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An internal error occurred")

def require_admin(user=Depends(get_current_user)):
    if user.get("role") != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin access required")
    return user