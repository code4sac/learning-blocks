import { createRouter, RouterProvider } from "@tanstack/react-router";
import { StrictMode } from "react";
import ReactDOM from "react-dom/client";
import * as AppQueryProvider from "./integrations/tanstack-query/root-provider.tsx";
import * as AuthProvider from "./hooks/auth-provider.tsx";
import { routeTree } from "./routeTree.gen";
import "./globals.css";
import reportWebVitals from "./reportWebVitals.ts";

const router = createRouter({
	routeTree,
	context: {
		...AppQueryProvider.getContext(),
		...AuthProvider.getContext(),
	},
	defaultPreload: "intent",
	scrollRestoration: true,
	defaultStructuralSharing: true,
	defaultPreloadStaleTime: 0,
});

declare module "@tanstack/react-router" {
	// biome-ignore lint: Register the router instance for type safety
	interface Register {
		router: typeof router;
	}
}

function InnerApp() {
	const auth = useAuth();
	return <RouterProvider router={router} context={{ auth }} />;
}

function App() {
	return (
		<AuthProvider router={router}>
			<InnerApp />
		</AuthProvider>
	);
}

const rootElement = document.getElementById("app");
if (rootElement && !rootElement.innerHTML) {
	const root = ReactDOM.createRoot(rootElement);
	root.render(
		<StrictMode>
			<AppQueryProvider.Provider>
				<App />
			</AppQueryProvider.Provider>
		</StrictMode>,
	);
}

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
