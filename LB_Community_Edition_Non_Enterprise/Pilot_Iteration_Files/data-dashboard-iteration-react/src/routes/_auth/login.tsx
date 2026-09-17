import { createFileRoute, redirect, useNavigate } from "@tanstack/react-router";
import { z } from "zod";
import { loginSchema, useLoginForm } from "@/components/forms/auth";
import { useAuth } from "@/components/hooks/use-auth";

export const Route = createFileRoute("/_auth/login")({
	beforeLoad: ({ context }) => {
		if (context.auth.isAuthenticated) {
			throw redirect({
				to: "/",
			});
		}
	},
	component: LoginComponent,
	validateSearch: z.object({
		redirect: z.string().optional(),
	}),
});

function LoginComponent() {
	const auth = useAuth();
	const navigate = useNavigate();
	const { redirect } = Route.useSearch();
	const form = useLoginForm({
		onSubmit: async (value) => {
			await auth.login(value.user);
			navigate({ to: redirect || "/", replace: true });
		},
	});
	return (
		<div className="flex min-h-screen items-center justify-center p-4 bg-gray-50 dark:bg-gray-900">
			<div className="w-full max-w-md rounded-lg border border-gray-200 bg-white p-6 shadow-md dark:border-gray-700 dark:bg-gray-800">
				<h2 className="mb-6 text-center text-2xl font-bold text-gray-900 dark:text-white">
					Login
				</h2>

				<form
					onSubmit={(e) => {
						e.preventDefault();
						e.stopPropagation();
						form.handleSubmit();
					}}
				>
					<form.Field
						name="user"
						validators={{
							onChange: loginSchema.shape.user,
						}}
					>
						{(field) => (
							<div className="mb-6">
								<label
									htmlFor={field.name}
									className="mb-2 block text-sm font-medium text-gray-700 dark:text-gray-300"
								>
									Username
								</label>
								<input
									id={field.name}
									name={field.name}
									value={field.state.value}
									onBlur={field.handleBlur}
									onChange={(e) => field.handleChange(e.target.value)}
									className="block w-full rounded-md border border-gray-300 bg-gray-50 p-2.5 text-gray-900 focus:border-blue-500 focus:outline-none focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:border-blue-500 dark:focus:ring-blue-500"
									placeholder="Enter your username"
								/>
								{field.state.meta.errors ? (
									<p className="mt-1 text-sm text-red-600 dark:text-red-400">
										{field.state.meta.errors.join(", ")}
									</p>
								) : null}
							</div>
						)}
					</form.Field>
					<button
						type="submit"
						disabled={form.state.isSubmitting}
						className="w-full rounded-lg bg-blue-600 px-5 py-2.5 text-center text-sm font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-4 focus:ring-blue-300 disabled:opacity-70 dark:bg-blue-500 dark:hover:bg-blue-600 dark:focus:ring-blue-800"
					>
						{form.state.isSubmitting ? "Logging in..." : "Login"}
					</button>
				</form>
			</div>
		</div>
	);
}
