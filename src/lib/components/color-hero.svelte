<script>
	import { enhance } from '$app/forms';
	import { getRandomPrompt } from '$lib/client/colors';
	import SubmitButton from './submit-button.svelte';

	let { totalSubmissions = 0, form: formResult = null } = $props();

	let pickedColor = $state('#ffffff');
	let prompt = $state('');
	let isSubmitting = $state(false);

	$effect(() => {
		prompt = getRandomPrompt();
	});
</script>

<form
	method="POST"
	action="?/submitColor"
	use:enhance={() => {
		isSubmitting = true;

		return async ({ update, result }) => {
			isSubmitting = false;
			await update();

			if (result.type === 'success') {
				prompt = getRandomPrompt();
				pickedColor = '#ffffff';
			}
		};
	}}
	class="mt-24 mb-8 flex w-full flex-col items-center justify-center"
>
	<input type="hidden" name="prompt" value={prompt} />
	<input type="hidden" name="value" value={pickedColor} />

	<h1 class="text-6xl leading-0 tracking-wide text-mauve-400">Give me</h1>
	<h1 class="text-8xl tracking-wider" style:color={pickedColor}>{prompt}</h1>
	<p class="mb-6 text-xl leading-0 text-mauve-600">
		Total Submissions: {totalSubmissions}
	</p>

	<div class="my-4 h-64 w-64">
		<!-- the actual color picker -->
		<input
			type="color"
			name="color"
			id="colorInput"
			aria-label="Pick a color"
			class="h-full w-full cursor-pointer border-none outline-none"
			bind:value={pickedColor}
			style:box-shadow="0 0 64px color-mix(in srgb, {pickedColor} 50%, transparent)"
		/>

		<!-- color code display -->
		<p
			class="-translate-y-10 text-center text-xl"
			style:color="color-mix(in srgb, {pickedColor} 30%, black)"
		>
			{pickedColor}
		</p>
	</div>

	<SubmitButton color={pickedColor} loading={isSubmitting} />
</form>
