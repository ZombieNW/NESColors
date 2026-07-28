export const COLOR_PROMPTS = [
	'Gray',
	'Azure',
	'Blue',
	'Violet',
	'Magenta',
	'Rose',
	'Red',
	'Orange',
	'Yellow',
	'Lime',
	'Green',
	'Teal',
	'Cyan'
];

export function getRandomPrompt() {
	const index = Math.floor(Math.random() * COLOR_PROMPTS.length);
	return COLOR_PROMPTS[index];
}
