<script>
	let isLoaded = $state(false);

	function handleCanPlay() {
		isLoaded = true;
	}
</script>

<video
	src="/glitch.mp4"
	autoplay
	loop
	muted
	playsinline
	oncanplaythrough={handleCanPlay}
	class="pointer-events-none fixed inset-0 -z-10 h-full w-full object-cover transition-opacity duration-1000 ease-in-out {isLoaded
		? 'opacity-10'
		: 'opacity-0'}"
>
</video>
