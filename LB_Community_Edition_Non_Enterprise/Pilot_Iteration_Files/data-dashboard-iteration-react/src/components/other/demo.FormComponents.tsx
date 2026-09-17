import { useFieldContext, } from ".../.../hooks/demo.form-context";
import { useStore } from "@tanstack/react-form";

function ErrorMessages({
	errors,
}: {
	errors: Array<string | { message: string }>;
}) {
	return (
		<>
			{errors.map((error) => (
				<div
					key={typeof error === "string" ? error : error.message}
					className="text-red-500 mt-1 font-bold"
				>
					{typeof error === "string" ? error : error.message}
				</div>
			))}
		</>
	);
}

export function TextField({
	label,
	placeholder,
}: {
	label: string;
	placeholder?: string;
}) {
	const field = useFieldContext<string>();
	const errors = useStore(field.store, (state) => state.meta.errors);

	return (
		<div>
			<label htmlFor={label} className="block font-bold mb-1 text-xl">
				{label}
				<input
					value={field.state.value}
					placeholder={placeholder}
					onBlur={field.handleBlur}
					onChange={(e) => field.handleChange(e.target.value)}
					className="w-full px-4 py-2 rounded-md border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500"
				/>
			</label>
			{field.state.meta.isTouched && <ErrorMessages errors={errors} />}
		</div>
	);
}

export function TextArea({
	label,
	rows = 3,
}: {
	label: string;
	rows?: number;
}) {
	const field = useFieldContext<string>();
	const errors = useStore(field.store, (state) => state.meta.errors);

	return (
		<div>
			<label htmlFor={label} className="block font-bold mb-1 text-xl">
				{label}
				<textarea
					value={field.state.value}
					onBlur={field.handleBlur}
					rows={rows}
					onChange={(e) => field.handleChange(e.target.value)}
					className="w-full px-4 py-2 rounded-md border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500"
				/>
			</label>
			{field.state.meta.isTouched && <ErrorMessages errors={errors} />}
		</div>
	);
}

export function Select({
	label,
	values,
}: {
	label: string;
	values: Array<{ label: string; value: string }>;
	placeholder?: string;
}) {
	const field = useFieldContext<string>();
	const errors = useStore(field.store, (state) => state.meta.errors);

	return (
		<div>
			<label htmlFor={label} className="block font-bold mb-1 text-xl">
				{label}
			</label>
			<select
				title="Name field"
				name={field.name}
				value={field.state.value}
				onBlur={field.handleBlur}
				onChange={(e) => field.handleChange(e.target.value)}
				className="w-full px-4 py-2 rounded-md border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500"
			>
				{values.map((value) => (
					<option key={value.value} value={value.value}>
						{value.label}
					</option>
				))}
			</select>
			{field.state.meta.isTouched && <ErrorMessages errors={errors} />}
		</div>
	);
}
