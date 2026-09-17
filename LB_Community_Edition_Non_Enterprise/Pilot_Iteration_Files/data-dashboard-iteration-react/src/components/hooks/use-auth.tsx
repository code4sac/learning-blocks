import type { RegisteredRouter } from "@tanstack/react-router";
import * as React from "react";

// Helper to create a mock JWT. In a real app, this would be done on the server.
const createMockJwt = (user: string) => {
	const header = { alg: "HS256", typ: "JWT" };
	const payload = { sub: user, iat: Date.now() };
	// A real signature would be a cryptographic hash. We'll just fake it.
	const signature = "mock-signature";

	return [
		btoa(JSON.stringify(header)),
		btoa(JSON.stringify(payload)),
		signature,
	].join(".");
};

// Helper to parse a mock JWT. In a real app, you'd verify this on the server.
const parseMockJwt = (token: string) => {
	try {
		const [, payload] = token.split(".");
		return JSON.parse(atob(payload));
	} catch (_e) {
		return null;
	}
};

export interface AuthContext {
	isAuthenticated: boolean;
	user?: string;
	currentOrg?: string;
	previousOrgs?: string[];
	login: (user: string) => Promise<void>;
	logout: () => void;
}

export const AuthContext = React.createContext<AuthContext | null>(null);

export function AuthProvider({
	children,
	router,
}: {
	children: React.ReactNode;
	router: RegisteredRouter;
}) {
	const [user, setUser] = React.useState<string | undefined>(() => {
		const token = localStorage.getItem("mock_jwt");
		if (token) {
			const parsed = parseMockJwt(token);
			return parsed?.sub;
		}
		return undefined;
	});

	const [currentOrg, _setCurrentOrg] = React.useState<string | undefined>(
		undefined,
	);
	const [previousOrgs, _setPreviousOrgs] = React.useState<string[] | undefined>(
		undefined,
	);

	const isAuthenticated = !!user;

	const login = async (newUser: string) => {
		// Simulate a server call
		await new Promise((resolve) => setTimeout(resolve, 500));

		// In a real app, you'd get a JWT from the server
		const token = createMockJwt(newUser);
		localStorage.setItem("mock_jwt", token);
		setUser(newUser);
		router.invalidate(); // Invalidate the router to update the context
	};

	const logout = () => {
		localStorage.removeItem("mock_jwt");
		setUser(undefined);
		router.invalidate(); // Invalidate the router to update the context
	};

	return (
		<AuthContext.Provider
			value={{
				isAuthenticated,
				user,
				login,
				logout,
				currentOrg,
				previousOrgs,
			}}
		>
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

// This is a hack to get the auth context into the router context
// We will be able to remove this once we have a better solution
// for dependency injection in TanStack Router
export function getAuthContext(
	router: RegisteredRouter,
): RegisteredRouter["options"]["context"]["auth"] {
	return router.options.context?.auth;
}
