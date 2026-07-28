import { fail } from '@sveltejs/kit';
import { submitColor, getTotalSubmissions } from '$lib/server/colors.js';

export async function load() {
	const total = await getTotalSubmissions();
	return { total };
}

export const actions = {
	submitColor: async ({ request }) => {
		const formData = await request.formData();
		const prompt = formData.get('prompt')?.toString();
		const value = formData.get('value')?.toString();

		if (!prompt || !value) {
			return fail(400, { error: 'Missing prompt or value' });
		}

		await submitColor(prompt, value);
		return { success: true };
	}
};
