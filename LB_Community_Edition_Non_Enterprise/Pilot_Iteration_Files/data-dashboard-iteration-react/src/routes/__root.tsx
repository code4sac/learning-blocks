import { createRootRouteWithContext, Outlet } from "@tanstack/react-router";
import { TanStackRouterDevtools } from "@tanstack/react-router-devtools";
import type { AuthContext } from "@/components/hooks/use-auth";
import TanStackQueryLayout from "../integrations/tanstack-query/layout.tsx";

interface AuthenticatedRouteContext {
	auth: AuthContext;
}

export const Route = createRootRouteWithContext<AuthenticatedRouteContext>()({
	component: () => (
		<>
			<Outlet />
			<TanStackRouterDevtools />
			<TanStackQueryLayout />
		</>
	),
});
