import { useFormContext } from "@/components/form/demo/demo.form-context.ts";

export function SubscribeButton({ label }: { label: string }) {
	const form = useFormContext();
	return (
		<form.Subscribe selector={(state) => state.isSubmitting}>
			{(isSubmitting) => (
				<button
					type="submit"
					disabled={isSubmitting}
					className="px-6 py-2 bg-indigo-600 text-white rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 transition-colors disabled:opacity-50"
				>
					{label}
				</button>
			)}
		</form.Subscribe>
	);
}