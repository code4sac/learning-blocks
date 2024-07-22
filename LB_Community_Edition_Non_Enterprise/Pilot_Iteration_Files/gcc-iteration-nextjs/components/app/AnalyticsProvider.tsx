//import * as React from 'react'
//import { User } from './models/user'

//export interface AuthenticatedState {
//  isAuthenticated: boolean
//  setUser: (user: User | null) => void
//  user: User | null
//}

//const AuthContext = React.createContext<AuthenticatedState | null>(null)

//export function AnalyticsProvider({ children }: { children: React.ReactNode }) {
//  const [user, setUser] = React.useState<User | null>(null)
//  const isAuthenticated = !!user
//  return <AuthContext.Provider value={{ isAuthenticated, user, setUser }}>
//    {children}
//  </AuthContext.Provider>
//}

