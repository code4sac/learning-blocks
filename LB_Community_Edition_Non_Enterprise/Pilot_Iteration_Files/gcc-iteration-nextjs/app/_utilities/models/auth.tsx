import * as React from "react";
import { User } from "./user";

export interface AuthenticatedState {
  isAuthenticated: boolean;
  setUser: (user: User | null) => void;
  user: User | null;
}

const AuthContext = React.createContext<AuthenticatedState | null>(null);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = React.useState<User | null>(null);
  const isAuthenticated = !!user;
  return (
    <AuthContext.Provider value={{ isAuthenticated, user, setUser }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = React.useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
}
