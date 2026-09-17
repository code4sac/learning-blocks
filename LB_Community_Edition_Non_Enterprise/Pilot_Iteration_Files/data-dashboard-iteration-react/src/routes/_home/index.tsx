import { createFileRoute } from "@tanstack/react-router";
import GaugeChart from "../../integrations/apache-echarts/gauge-chart.tsx";
import SearchHomepageForm from "../../components/form/SearchHomepageForm.tsx";

export type HomePageProps = {};
export const Route = createFileRoute("/_home/")({
	component: HomePage,
});

function HomePage({}: HomePageProps) {
	return (
		<main className="flex flex-col">
			<header className="container mx-auto flex flex-col items-center mt-16">
				<h1 className="text-[calc(10px+2vmin)]">Find a school district to view its information.</h1>
				<SearchHomepageForm />
			</header>
			<section className="bg-[#282c34] text-white ">
				<h2>Indicators from Red, orange, yellow, green, to Blue.</h2>
				<GaugeChart />
			</section>
			<section className="bg-[#282c34] text-white ">
				<a
					className="text-[#61dafb] hover:underline"
					href="https://reactjs.org"
					target="_blank"
					rel="noopener noreferrer"
				>
					Learn React
				</a>
				<a
					className="text-[#61dafb] hover:underline"
					href="https://tanstack.com"
					target="_blank"
					rel="noopener noreferrer"
				>
					Learn TanStack
				</a>
			</section>
		</main>
	);
}
