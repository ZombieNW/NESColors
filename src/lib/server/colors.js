import { db } from './db/index';
import { colors } from './db/schema';
import { count } from 'drizzle-orm';

export async function submitColor(prompt, value) {
	await db.insert(colors).values({ prompt, value });
	return { success: true };
}

export async function getTotalSubmissions() {
	const [{ total }] = await db.select({ total: count() }).from(colors);
	return total;
}
