import { createFileRoute, redirect } from "@tanstack/react-router";

export const Route = createFileRoute("/_auth/logout")({
	beforeLoad: ({ context }) => {
		context.auth.logout();
		throw redirect({
			to: "/login",
			search: {
				redirect: "/",
			},
			replace: true,
		});
	},
});
