import { useForm } from "@tanstack/react-form";
import { z } from "zod";

export const loginSchema = z.object({
	user: z.string().min(1, "Username is required"),
});

export type LoginFormValues = z.infer<typeof loginSchema>;

export function useLoginForm(opts: {
	onSubmit: (data: LoginFormValues) => Promise<void> | void;
}) {
	return useForm<LoginFormValues>({
		defaultValues: {
			user: "",
		},
		onSubmit: async ({ value }) => {
			await opts.onSubmit(value);
		},
	});
}
