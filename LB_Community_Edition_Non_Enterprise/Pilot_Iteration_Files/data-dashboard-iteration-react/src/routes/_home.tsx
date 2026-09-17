import { createFileRoute, Outlet } from "@tanstack/react-router";
import { useAuth } from "@/components/hooks/use-auth";
import Navbar from "@/components/ui/navbar/Navbar.tsx";


export const Route = createFileRoute("/_home")({
	component: HomeLayout,
});

function HomeLayout() {
	const _auth = useAuth();
	return (
		<div className="min-h-screen bg-coo4-500">
			<Navbar />
			<Outlet />
		</div>
	);
}
