<script>
	import ColorHero from '$lib/components/color-hero.svelte';
	import Prose from '$lib/components/prose.svelte';
	import Footer from '$lib/components/footer.svelte';
	import BackgroundVideo from '$lib/components/background-video.svelte';

	let { data, form } = $props();
</script>

<div class="mx-auto w-full px-8 md:w-1/2">
	<ColorHero totalSubmissions={data.total} {form} />
	<Prose />
	<Footer />
</div>
<BackgroundVideo />
