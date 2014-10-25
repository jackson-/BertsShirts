import sqlite3

def create_users_table():
	conn = sqlite3.connect('shirt.db')
	c = conn.cursor()
	c.execute('''DROP TABLE IF EXISTS `users`;''')
	c.execute("""CREATE TABLE `users` (
			`id` INTEGER,
			`first_name` TEXT,
			`last_name` TEXT,
			`username` VARCHAR,
			`user_type` TEXT,
			PRIMARY KEY (`id`)
			)""")
	conn.commit()
	conn.close()


def create_inventory_table():
	conn = sqlite3.connect('shirt.db')
	c = conn.cursor()
	c.execute('''DROP TABLE IF EXISTS `inventory`;''')
	c.execute("""CREATE TABLE `inventory` (
			`id` INTEGER,
			`design_id` INTEGER,
			`customer_id` INTEGER,
			PRIMARY KEY (`id`),
			FOREIGN KEY (design_id) REFERENCES designs(id),
			FOREIGN KEY (customer_id) REFERENCES users(id)
			)""")
	conn.commit()
	conn.close()


def create_designs_table():
	conn = sqlite3.connect('shirt.db')
	c = conn.cursor()
	c.execute('''DROP TABLE IF EXISTS `designs`;''')
	c.execute("""CREATE TABLE `designs` (
			`id` INTEGER,
			`artist_id` INTEGER,
			`artist_name` TEXT,
			`title` TEXT,
			`price` INT,
			`purchase_times` INT,
			PRIMARY KEY (`id`),
			FOREIGN KEY (artist_id) REFERENCES users(id)
			)""")
	conn.commit()
	conn.close()


def create_subscriptions_table():
	conn = sqlite3.connect('shirt.db')
	c = conn.cursor()
	c.execute('''DROP TABLE IF EXISTS `subscriptions`;''')
	c.execute("""CREATE TABLE `subscriptions` (
			`id` INTEGER,
			`customer_id` INTEGER,
			`artist_id` INTEGER,
			FOREIGN KEY (customer_id) REFERENCES users(id),
			FOREIGN KEY (artist_id) REFERENCES users(id),
			PRIMARY KEY (`id`)
			)""")
	conn.commit()
	conn.close()


def create_notifications_table():
	conn = sqlite3.connect('shirt.db')
	c = conn.cursor()
	c.execute('''DROP TABLE IF EXISTS `notifications`;''')
	c.execute("""CREATE TABLE `notifications` (
			`id` INTEGER,
			`user_id` INTEGER,
			`message` VARCHAR,
			FOREIGN KEY (user_id) REFERENCES users(id),
			PRIMARY KEY (`id`)
			)""")
	conn.commit()
	conn.close()


def create_transactions_table():
	conn = sqlite3.connect('shirt.db')
	c = conn.cursor()
	c.execute('''DROP TABLE IF EXISTS `transactions`;''')
	c.execute("""CREATE TABLE `transactions` (
			`id` INTEGER,
			`customer_id` INTEGER,
			`artist_id` INTEGER,
			`design_id` INTEGER,
			`price_paid` INT,
			FOREIGN KEY (design_id) REFERENCES designs(id),
			FOREIGN KEY (customer_id) REFERENCES users(id),
			FOREIGN KEY (artist_id) REFERENCES users(id),
			PRIMARY KEY (`id`)
			)""")
	conn.commit()
	conn.close()


create_users_table()
create_inventory_table()
create_designs_table()
create_subscriptions_table()
create_notifications_table()
create_transactions_table()