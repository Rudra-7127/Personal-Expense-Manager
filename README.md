<div align="center">

# 💰 Personal Expense Manager

### A full-stack personal finance tracker — built to make managing money effortless.

[![React](https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Supabase](https://img.shields.io/badge/Supabase-PostgreSQL-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](docker-compose.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

**Created by [Rudra J Rabadiya](https://github.com/Rudra-7127)**

🌐 **Live Demo:** [https://personalexpensemanager.dpdns.org](https://personalexpensemanager.dpdns.org)

</div>

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔐 **Authentication** | Secure register & login with JWT-based auth via Supabase |
| 📊 **Dashboard** | At-a-glance overview of income, expenses & current balance |
| 📉 **Expenses** | Add, edit, and delete expense entries with category tagging |
| 📈 **Income** | Track multiple income sources separately |
| 🤝 **Udhar Book** | Manage money lent & borrowed with mark-as-paid support |
| 📋 **All Entries** | Unified transaction view with powerful filters |
| 📑 **Reports** | Monthly & yearly reports with visual charts + export to PDF or Excel |
| 👤 **Profile** | View and update your personal profile |
| 👑 **Admin Panel** | Platform-wide user management, user reports & platform stats (admin only) |
| 🌙 **Dark / Light Mode** | Theme toggle with persistent preference |

---

## 🏗️ Tech Stack

<table>
  <tr>
    <td valign="top" width="50%">

### 🖥️ Frontend

| Technology | Version | Purpose |
|---|---|---|
| **React** | 18.3 | UI framework |
| **Vite** | 5 | Build tool & dev server |
| **React Router** | v6 | Client-side routing |
| **Recharts** | 3 | Charts & data visualisation |
| **Axios** | 1.7 | HTTP client |
| **date-fns** | 3.6 | Date formatting |
| **jsPDF + AutoTable** | latest | PDF export |
| **XLSX** | 0.18 | Excel export |
| **react-hot-toast** | 2.4 | Toast notifications |
| **Supabase JS** | 2.43 | Auth token management |

  </td>
  <td valign="top" width="50%">

### ⚙️ Backend

| Technology | Version | Purpose |
|---|---|---|
| **FastAPI** | 0.111+ | REST API framework |
| **Uvicorn** | 0.29+ | ASGI server |
| **Supabase** | 2.4+ | PostgreSQL database + Auth |
| **python-jose** | 3.3 | JWT verification |
| **Pydantic v2** | 2.11+ | Request/response validation |
| **pydantic-settings** | 2.2+ | Environment config |
| **httpx** | 0.27+ | Async HTTP client |
| **python-dotenv** | 1.0 | `.env` file loading |

  </td>
  </tr>
</table>

---

## 📁 Project Structure

```
Personal Expense Manager/
│
├── 🖥️  PEM-Frontend/                  # React + Vite frontend
│   ├── src/
│   │   ├── components/                # Reusable layout & modal components
│   │   │   └── Layout.jsx             # App shell (sidebar, topbar)
│   │   ├── context/
│   │   │   ├── AuthContext.jsx        # Authentication state & helpers
│   │   │   └── ThemeContext.jsx       # Dark/light theme provider
│   │   ├── lib/                       # Utilities & constants
│   │   ├── pages/
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── Expenses.jsx
│   │   │   ├── Income.jsx
│   │   │   ├── Udhar.jsx
│   │   │   ├── AllEntries.jsx
│   │   │   ├── Reports.jsx
│   │   │   ├── Profile.jsx
│   │   │   └── admin/
│   │   │       ├── AdminDashboard.jsx
│   │   │       ├── AdminUserDetail.jsx
│   │   │       └── AdminReports.jsx
│   │   └── styles/                    # Global CSS
│   ├── index.html
│   ├── vite.config.js
│   ├── vercel.json                # Vercel routing configuration for SPA
│   └── package.json
│
└── ⚙️  PEM-Backend/                   # FastAPI backend
    ├── app/
    │   ├── main.py                    # FastAPI app entry point & CORS config
    │   ├── config.py                  # Environment settings (pydantic-settings)
    │   ├── routes/
    │   │   ├── auth.py                # Register, login, /me
    │   │   ├── entries.py             # Income & expense CRUD
    │   │   ├── udhar.py               # Udhar (lending/borrowing) CRUD
├── ⚙️  PEM-Backend/                   # FastAPI backend
│   ├── app/
│   ├── supabase/
│   │   └── schema.sql                 # Full database schema
│   ├── Dockerfile                 # Dockerfile for FastAPI backend
│   ├── .dockerignore
│   ├── requirements.txt
│   ├── Procfile                       # Render deployment config
│   └── runtime.txt                    # Python version pin
│
└── 🐳 docker-compose.yml              # One-command full-stack container orchestration
```

---

## 🚀 Getting Started

### Prerequisites

> Make sure you have the following installed before proceeding.

| Requirement | Version |
|---|---|
| [Node.js](https://nodejs.org) | ≥ 18 |
| [Python](https://python.org) | ≥ 3.11 |
| [Supabase](https://supabase.com) | Active project |

---

### Step 1 — Clone the Repository

```bash
git clone https://github.com/Rudra-7127/Personal-Expense-Manager.git
cd Personal-Expense-Manager
```

---

## 🐳 Quick Start with Docker (Recommended)

### Option A — Pull Pre-built Images from Docker Hub 🚀
No need to build locally! Pull the official Docker Hub images directly:

```bash
# Pull images from Docker Hub
docker pull rudrarabadiya/zevonix-backend:latest
docker pull rudrarabadiya/zevonix-frontend:latest
```

- ⚙️ **Docker Hub Backend:** [rudrarabadiya/zevonix-backend](https://hub.docker.com/r/rudrarabadiya/zevonix-backend)
- 🖥️ **Docker Hub Frontend:** [rudrarabadiya/zevonix-frontend](https://hub.docker.com/r/rudrarabadiya/zevonix-frontend)

---

### Option B — Build & Run Locally with Docker Compose

1. **Configure Environment:**
   Create `.env` in `PEM-Backend/`:
   ```bash
   cp PEM-Backend/.env.example PEM-Backend/.env
   ```
   Fill in your Supabase credentials in `PEM-Backend/.env`:
   ```env
   SUPABASE_URL=https://your-project.supabase.co
   SUPABASE_SERVICE_KEY=your-service-role-key
   SUPABASE_JWT_SECRET=your-jwt-secret
   ALLOWED_ORIGINS=http://localhost:5173
   ```

2. **Launch Containers:**
   ```bash
   docker compose up --build
   ```

3. **Access Services:**
   - 🌐 **Frontend UI:** `http://localhost:5173`
   - ⚙️ **Backend API:** `http://localhost:8000`
   - 📖 **Interactive Swagger Docs:** `http://localhost:8000/docs`

---


## 💻 Manual Local Development Setup

### Step 2 — Database Setup

1. Go to your **Supabase Dashboard → SQL Editor**
2. Paste and run the full contents of `PEM-Backend/supabase/schema.sql`

---

### Step 3 — Backend Setup

```bash
cd PEM-Backend

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

# Install dependencies
pip install -r requirements.txt

# Configure environment
copy .env.example .env
# → Open .env and fill in your Supabase credentials
```

**Required `.env` variables:**

```env
SUPABASE_URL=https://xxxx.supabase.co
SUPABASE_SERVICE_KEY=your-service-role-key
SUPABASE_JWT_SECRET=your-jwt-secret
ALLOWED_ORIGINS=http://localhost:5173
```

> 💡 Get these values from: **Supabase Dashboard → Project Settings → API**

**Start the backend server:**

```bash
uvicorn app.main:app --reload
```

✅ API is live at: `http://localhost:8000`  
📖 Interactive docs: `http://localhost:8000/docs`

---

### Step 4 — Frontend Setup

```bash
cd PEM-Frontend

# Install dependencies
npm install

# Configure environment
copy .env.example .env
# → Open .env and fill in your API URL and Supabase credentials
```

**Required `.env` variables:**

```env
VITE_API_URL=http://localhost:8000
VITE_SUPABASE_URL=https://xxxx.supabase.co
VITE_SUPABASE_ANON_KEY=your-anon-key
```

**Start the dev server:**

```bash
npm run dev
```

✅ App is live at: `http://localhost:5173`

---

## 📡 API Reference

### 🔓 Auth

| Method | Route | Auth | Description |
|--------|-------|:----:|-------------|
| `POST` | `/auth/register` | — | Register a new user |
| `POST` | `/auth/login` | — | Login and receive JWT |
| `GET` | `/auth/me` | 🔒 | Get current user profile |

### 💸 Entries (Income & Expenses)

| Method | Route | Auth | Description |
|--------|-------|:----:|-------------|
| `GET` | `/entries/` | 🔒 | List all entries |
| `POST` | `/entries/` | 🔒 | Create a new entry |
| `PUT` | `/entries/{id}` | 🔒 | Update an entry |
| `DELETE` | `/entries/{id}` | 🔒 | Delete an entry |

### 🤝 Udhar

| Method | Route | Auth | Description |
|--------|-------|:----:|-------------|
| `GET` | `/udhar/` | 🔒 | List udhar records |
| `POST` | `/udhar/` | 🔒 | Add an udhar record |
| `PATCH` | `/udhar/{id}/mark-paid` | 🔒 | Mark udhar as paid |

### 📑 Reports

| Method | Route | Auth | Description |
|--------|-------|:----:|-------------|
| `GET` | `/reports/monthly?year=&month=` | 🔒 | Monthly report for current user |
| `GET` | `/reports/yearly?year=` | 🔒 | Yearly report for current user |

### 👑 Admin

| Method | Route | Auth | Description |
|--------|-------|:----:|-------------|
| `GET` | `/admin/dashboard` | 👑 | Platform-wide statistics |
| `GET` | `/admin/users` | 👑 | List all platform users |
| `GET` | `/admin/users/{id}/full` | 👑 | Full detail of a user |
| `GET` | `/reports/admin/{user_id}/monthly` | 👑 | Monthly report for any user |
| `GET` | `/reports/admin/{user_id}/yearly` | 👑 | Yearly report for any user |

> 🔒 = Requires JWT Bearer token &nbsp;&nbsp; 👑 = Admin role required

---

## ☁️ Deployment

### Backend → [Render](https://render.com)

1. Create a **New Web Service** and connect your GitHub repo
2. Set **Root Directory** to `PEM-Backend`
3. **Build Command:** `pip install -r requirements.txt`
4. **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Add all `.env` variables under the **Environment** tab

### Frontend → [Vercel](https://vercel.com) / [Netlify](https://netlify.com)

1. Connect your repo and set **Root Directory** to `PEM-Frontend`
2. **Build Command:** `npm run build`
3. **Output Directory:** `dist`
4. Add all `VITE_*` variables in the platform's environment settings

> 💡 **Note on Routing:** A `vercel.json` file is pre-configured in the frontend root to handle Single Page Application (SPA) routing. This automatically prevents 404 errors when reloading pages or navigating directly to URLs like `/login`.

> ⚠️ After deploying the backend, update `VITE_API_URL` in the frontend env to your Render service URL, and update `ALLOWED_ORIGINS` in the backend env to your Vercel/Netlify URL.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

<div align="center">

<br>

# 👨‍💻 About the Developer

<h2><em>Rudra Rabadiya</em></h2>



[![Portfolio](https://img.shields.io/badge/🌐%20Portfolio-Visit%20My%20Site-2d6a4f?style=for-the-badge&logoColor=white&labelColor=1a3d2b)](https://rudrarabadiya.dpdns.org)
&nbsp;
[![GitHub](https://img.shields.io/badge/GitHub-RudraRabadiya-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/RudraRabadiya)

<br>

*© 2026 Rudra Rabadiya · All Rights Reserved*

</div>
