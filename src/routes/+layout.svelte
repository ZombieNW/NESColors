<script>
	import './layout.css';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href="/icon.png" />
	<title>NES Community Palette</title>
</svelte:head>

{@render children()}
