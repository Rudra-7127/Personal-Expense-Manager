import { createContext, useContext, useEffect, useState } from 'react'

const ThemeContext = createContext(null)

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState(() => {
    return localStorage.getItem('pem_theme') || 'dark'
  })
  const [currency, setCurrency] = useState(() => {
    return localStorage.getItem('pem_currency') || '$'
  })

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme)
    localStorage.setItem('pem_theme', theme)
  }, [theme])

  useEffect(() => {
    localStorage.setItem('pem_currency', currency)
  }, [currency])

  const toggleTheme = () => setTheme(t => t === 'dark' ? 'light' : 'dark')

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme, currency, setCurrency }}>
      {children}
    </ThemeContext.Provider>
  )
}

export const useTheme = () => useContext(ThemeContext)

