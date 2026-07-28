import { integer, sqliteTable, text } from 'drizzle-orm/sqlite-core';

export const colors = sqliteTable('colors', {
	id: integer('id').primaryKey({ autoIncrement: true }),
	prompt: text('prompt').notNull(),
	value: text('value').notNull()
});
