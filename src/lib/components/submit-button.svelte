<script>
	let { color = $bindable('#ffffff'), loading } = $props();
</script>

<button
	disabled={loading}
	style:--btn-bg={color}
	style:--btn-hover="color-mix(in srgb, {color} 80%, white)"
	style:--btn-border="color-mix(in srgb, {color} 50%, black)"
	style:--btn-shadow="color-mix(in srgb, {color} 30%, black)"
	class="my-8 cursor-pointer border-4 border-(--btn-border) bg-(--btn-bg) px-12 py-3 text-2xl font-bold tracking-wider text-(--btn-shadow) uppercase shadow-[6px_6px_0_0_var(--btn-shadow)] transition-all duration-75 hover:bg-[--btn-hover] active:translate-x-1 active:translate-y-1 active:shadow-[0px_0px_0_0_var(--btn-shadow)]"
>
	{#if loading}
		Loading...
	{:else}
		Submit
	{/if}
</button>
