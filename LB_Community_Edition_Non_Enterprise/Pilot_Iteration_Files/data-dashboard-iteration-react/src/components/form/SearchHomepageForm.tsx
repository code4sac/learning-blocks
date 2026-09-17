import { useForm } from "@tanstack/react-form";
import React from "react";
import { ComboBox } from "../ui/input/ComboBox";

// Mock API call for async validation
const checkDistrictExists = async (
	name: string,
): Promise<string | undefined> => {
	console.log(`Checking if "${name}" exists...`);
	await new Promise((resolve) => setTimeout(resolve, 500));
	if (name.toLowerCase().includes("invalid")) {
		return "This district does not seem to exist.";
	}
	return undefined;
};

// A custom hook to encapsulate the form logic
export function useSearchHomepageForm(opts?: {
	onSubmit?: (data: { schoolOrDistrict: string; location: string }) => void;
}) {
	const form = useForm({
		defaultValues: {
			schoolOrDistrict: "",
			location: "",
		},
		onSubmit: async ({ value }) => {
			console.log("Form submitted with:", value);
			alert(`Searching for ${value.schoolOrDistrict} in ${value.location}`);
			opts?.onSubmit?.(value);
		},
	});

	return form;
}

export default function SearchHomepageForm() {
	const form = useSearchHomepageForm();
	const schoolOptions = [
		"Springfield Elementary",
		"Shelbyville Middle School",
		"Ogdenville High",
	];
	const locationOptions = [
		"Springfield, IL",
		"Shelbyville, TN",
		"Ogdenville, OH",
	];

	return (
		<form
			onSubmit={(e) => {
				e.preventDefault();
				e.stopPropagation();
				form.handleSubmit();
			}}
			className="flex w-4xl items-end gap-4 pb-40"
		>
			<form.Field
				name="schoolOrDistrict"
				validators={{
					onChange: ({ value }) =>
						!value ? "Please enter a school or district." : undefined,
				}}
			>
				{(field) => (
					<ComboBox
						field={field}
						options={schoolOptions}
						placeholder="Enter a school or district"
						label="School or District"
					/>
				)}
			</form.Field>
			<form.Field
				name="location"
				validators={{
					onChange: ({ value }) =>
						!value ? "Please enter a location." : undefined,
				}}
			>
				{(field) => (
					<ComboBox
						field={field}
						options={locationOptions}
						placeholder="Enter a location"
						label="Location"
					/>
				)}
			</form.Field>
			<form.Subscribe
				selector={(state) => [state.canSubmit, state.isSubmitting]}
			>
				{([canSubmit, isSubmitting]) => (
					<button
						className="flex-shrink rounded-md bg-cool2-500 px-4 py-2 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-cool2-500 disabled:opacity-50"
						type="submit"
						disabled={!canSubmit}
					>
						{isSubmitting ? "Searching..." : "Search"}
					</button>
				)}
			</form.Subscribe>
		</form>
	);
}
