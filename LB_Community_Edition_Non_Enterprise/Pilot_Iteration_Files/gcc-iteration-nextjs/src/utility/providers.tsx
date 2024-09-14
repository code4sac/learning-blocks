'use client'

import { NextUIProvider } from '@nextui-org/system'
import * as React from 'react'
import { ThemeProviderProps } from 'next-themes/dist/types'
import { ThemeProvider as NextThemesProvider } from 'next-themes'
import { useRouter } from 'next/navigation'

export interface AppNextUIProviderProps {
  children?: React.ReactNode
  themeProps?: ThemeProviderProps
}
export const AppNextUIProvider: React.FC<AppNextUIProviderProps> = ({
  children,
  themeProps,
}) => {
  let router = useRouter()

  return (
    <NextUIProvider navigate={router.push}>
      <NextThemesProvider {...themeProps}>{children}</NextThemesProvider>
    </NextUIProvider>
  )
}

export interface AuthenticatedState {
  isAuthenticated: boolean
  setUser: (user: User | null) => void
  user: User | null
}

let AuthContext = React.createContext<AuthenticatedState | null>(null)

export function AuthProvider({ children }: { children: React.ReactNode }) {
  let [user, setUser] = React.useState<User | null>(null)
  let isAuthenticated = !!user
  return (
    <AuthContext.Provider value={{ isAuthenticated, user, setUser }}>
      {children}
    </AuthContext.Provider>
  )
}

export function useAuth() {
  let context = React.useContext(AuthContext)
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider')
  }
  return context
}

export class User {
  id!: string
  name!: string
}
