import sqlite3


## default values
defaultdb = "shirt.db"

class User:

	def __init__(self, username, first_name, last_name):
		self.username = username
		self.first_name = first_name
		self.last_name = last_name


class Customer(User):
	
	def __init__(self, user_type):
		self.user_type = user_type


	def buy(self, design_id, customer_id):
		DB.add_to_inventory(design_id, customer_id)


	def delete_notification(self, notificaton_id):
		pass

	def subscribe(self, customer_id, artist_id):
		DB.create_subscription(customer_id, artist_id)


class Artist(User):

	def __init__(self, user_type):
		self.user_type = user_type

	
	def create_design(self, title, artist_id, artist_name, price):
		DB.create_design(title, artist_id, artist_name, price)


	def delete_notification(self, notificaton_id):
		pass


class Design:

	def __init__(self, title, price):
		self.title = title
		self.price = price


class Notification:

	def __init__(self, message):
		self.message = message



class DB:

	@staticmethod
	def load_user(username, db=defaultdb):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		c.execute("SELECT id, first_name, last_name, user_type FROM users WHERE username = (?)", (username, ))
		user = c.fetchone()
		if user is None:
			return(None)
		else:
			return(user)

	@staticmethod
	def create_artist(first_name, last_name, username, user_type, db=defaultdb):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "INSERT INTO users(first_name, last_name, username, user_type) VALUES(?, ?, ?, ?); "
		c.execute(statement, (first_name, last_name, username, user_type,))
		conn.commit()
		conn.close()

	@staticmethod
	def create_subscription(customer_id, artist_id, db=defaultdb):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "INSERT INTO subscriptions(customer_id, artist_id) VALUES(?, ?); "
		c.execute(statement, (customer_id, artist_id,))
		conn.commit()
		conn.close()


	@staticmethod
	def create_customer(first_name, last_name, username, user_type, db=defaultdb):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "INSERT INTO users(first_name, last_name, username, user_type) VALUES(?, ?, ?, ?); "
		c.execute(statement, (first_name, last_name, username, user_type,))
		conn.commit()
		conn.close()

	@staticmethod
	def create_design(title, artist_id, artist_name, price, purchase_times=0, db=defaultdb):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "INSERT INTO designs(title, artist_id, artist_name, price, purchase_times) VALUES(?, ?, ?, ?, ?); "
		c.execute(statement, (title, artist_id, artist_name, price, purchase_times,))
		conn.commit()
		conn.close()

	@staticmethod
	def create_notification(user_id, message, db=defaultdb):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "INSERT INTO notifications(user_id, message) VALUES(?, ?); "
		c.execute(statement, (user_id, message,))
		conn.commit()
		conn.close()

	@staticmethod
	def add_to_inventory(design_id, customer_id, db=defaultdb):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "INSERT INTO inventory(design_id, customer_id) VALUES(?, ?); "
		c.execute(statement, (design_id, customer_id,))
		conn.commit()
		conn.close()


	@staticmethod
	def check_user_type(user_id, db=defaultdb):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		c.execute("SELECT user_type FROM users WHERE id = (?)", (user_id, ))
		user_type = c.fetchone()
		return(user_type)

	@staticmethod
	def get_design_stats(artist_id, db=defaultdb):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT title, purchase_times FROM designs WHERE artist_id = (?); "
		c.execute(statement, (artist_id,))
		design_stats = c.fetchall()
		if len(design_stats) == 0:
			return None
		else:
			return(design_stats)
		conn.commit()
		conn.close()

	@staticmethod
	def get_notifications(user_id, db=defaultdb):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT message FROM notifications WHERE user_id = (?); "
		c.execute(statement, (user_id,))
		messages = c.fetchall()
		if len(messages) == 0:
			return None
		else:
			return(messages)
		conn.commit()
		conn.close()

	@staticmethod
	def delete_notification(notification_id, db=defaultdb):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "DELETE * FROM notifications WHERE id = (?); "
		c.execute(statement, (notification_id,))
		notifications = c.fetchall()
		conn.commit()
		conn.close()


	@staticmethod
	def get_artist_name(artist_id, db=defaultdb):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT * FROM users WHERE user_type = 'artist'; "
		c.execute(statement, (artist_id,))
		messages = c.fetchall()
		if len(messages) == 0:
			return None
		else:
			return(messages)
		conn.commit()
		conn.close()


	@staticmethod
	def get_artist_id(first_name, last_name, db=defaultdb):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT id FROM users WHERE user_type = 'artist' AND first_name = (?) AND last_name = (?); "
		c.execute(statement, (first_name, last_name,))
		ids = c.fetchall()
		if len(ids) == 0:
			return None
		else:
			return(ids)
		conn.commit()
		conn.close()


	@staticmethod
	def get_all_designs(db=defaultdb):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT id, artist_name, title, price FROM designs;"
		c.execute(statement,)
		design_list = c.fetchall()
		if len(design_list) == 0:
			return None
		else:
			return(design_list)
		conn.commit()
		conn.close()

	@staticmethod
	def get_inventory(user_id, db=defaultdb):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT title, artist_name FROM designs INNER JOIN inventory ON designs.id = inventory.design_id AND inventory.customer_id = (?);"
		c.execute(statement, (user_id,))
		info = c.fetchall()
		if len(info) == 0:
			return(None)
		else:
			return(info)
		conn.close()


	@staticmethod
	def get_all_artist_names(db=defaultdb):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT first_name, last_name FROM users WHERE user_type = 'artist';"
		c.execute(statement,)
		name_list = c.fetchall()
		return(name_list)

	@staticmethod
	def get_subscriptions(artist_id, db=defaultdb):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT customer_id FROM subscriptions WHERE artist_id = (?);"
		c.execute(statement, (artist_id,))
		subscription_list = c.fetchall()
		return(subscription_list)

	@staticmethod
	def update_purchase_times(design_id, db=defaultdb):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT purchase_times FROM designs WHERE id = (?);"
		c.execute(statement, (design_id,))
		purchases = c.fetchall()
		if len(purchases) == 0:
			return(None)
		else:
			purchases = purchases[0][0]
			purchases += 1
			print(purchases)
		statement = "UPDATE designs SET purchase_times = (?) WHERE id = (?)"
		c.execute(statement, (purchases, design_id,))
		conn.commit()
		conn.close()

