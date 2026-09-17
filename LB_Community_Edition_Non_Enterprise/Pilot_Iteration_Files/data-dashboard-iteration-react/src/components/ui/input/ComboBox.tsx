import React, { useEffect, useRef, useState } from "react";

function FieldInfo({
	field,
}: {
	field: {
		state: { meta: { touchedErrors: string[]; isValidating: boolean } };
	};
}) {
	return (
		<>
			{field.state.meta.touchedErrors ? (
				<em className="text-red-600">{field.state.meta.touchedErrors}</em>
			) : null}
			{field.state.meta.isValidating ? (
				<em className="text-gray-500">Validating...</em>
			) : null}
		</>
	);
}

export function ComboBox({
	field,
	options,
	placeholder,
	label,
}: {
	field: any;
	options: string[];
	placeholder: string;
	label: string;
}) {
	const [isOpen, setIsOpen] = useState(false);
	const [filteredOptions, setFilteredOptions] = useState(options);
	const selectRef = useRef<HTMLDivElement>(null);

	useEffect(() => {
		const handleClickOutside = (event: MouseEvent) => {
			if (
				selectRef.current &&
				!selectRef.current.contains(event.target as Node)
			) {
				setIsOpen(false);
			}
		};
		document.addEventListener("mousedown", handleClickOutside);
		return () => {
			document.removeEventListener("mousedown", handleClickOutside);
		};
	}, []);

	const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
		const value = e.target.value;
		field.handleChange(value);
		setIsOpen(true);
		if (value) {
			setFilteredOptions(
				options.filter((option) =>
					option.toLowerCase().includes(value.toLowerCase()),
				),
			);
		} else {
			setFilteredOptions(options);
		}
	};

	const handleSelect = (value: string) => {
		field.handleChange(value);
		setIsOpen(false);
	};

	return (
		<div className="flex-1" ref={selectRef}>
			<div className="relative">
				<label
					htmlFor={field.name}
					className="block  font-medium text-cool1-500 tracking-wide"
				>
					{label}
				</label>
				<input
					type="text"
					id={field.name}
					name={field.name}
					value={field.state.value}
					placeholder={placeholder}
					onChange={handleInputChange}
					onFocus={() => {
						if (field.state.value) {
							setFilteredOptions(
								options.filter((option) =>
									option.toLowerCase().includes(field.state.value.toLowerCase()),
								),
							);
						} else {
							setFilteredOptions(options);
						}
						setIsOpen(true);
					}}
					onBlur={field.handleBlur}
					className="peer mt-1 block w-full bg-transparent p-2 text-left outline-none  tracking-wider cursor-text"
				/>
				<span
					className="absolute bottom-0 left-0 block h-px w-full bg-gray-300"
					aria-hidden="true"
				/>
				<span
					className="absolute bottom-0 left-0 block h-px w-full origin-center scale-x-0 transform bg-cool1-500 transition-transform duration-300 ease-in-out peer-focus-within:scale-x-100"
					aria-hidden="true"
				/>
				{isOpen && (
					<div className="absolute z-10 mt-1 w-full rounded-sm border border-gray-200 bg-white shadow-lg">
						<ul className="max-h-60 overflow-auto rounded-sm  text-base  focus:outline-none sm:text-sm tracking-wide">
							{filteredOptions.map((option) => (
								<li
									key={option}
									onClick={() => handleSelect(option)}
									className="relative cursor-pointer select-none py-2 pl-3 pr-9 text-gray-900 hover:bg-cool4-500 "
								>
									{option}
								</li>
							))}
						</ul>
					</div>
				)}
			</div>
			<div className="mt-1 h-5 text-xs">
				<FieldInfo field={field} />
			</div>
		</div>
	);
}
