import { createFormHook } from "@tanstack/react-form";

import {
	Select,
	TextArea,
	TextField,
} from "@/components/other/demo.FormComponents.tsx";
import { fieldContext, formContext } from "./demo.form-context.ts";
import { SubscribeButton } from "@/components/ui/button/SubscribeButton.tsx";

export const { useAppForm } = createFormHook({
	fieldComponents: {
		TextField,
		Select,
		TextArea,
	},
	formComponents: {
		SubscribeButton,
	},
	fieldContext,
	formContext,
});
