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


	def buy(self, design_id):
		pass


	def add_to_inventory(self, design_id, customer_id):
		DB.add_to_inventory(design_id, customer_id)


	def delete_notification(self, notificaton_id):
		pass

	def subscribe(self, artist_id):
		pass


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
		statement = "SELECT * FROM inventory WHERE customer_id = (?);"
		c.execute(statement, (user_id,))
		inventory_list = c.fetchall()
		title_list = []
		name_list = []
		if len(inventory_list) == 0:
			return None
		else:
			return(inventory_list)
		conn.commit()
		conn.close()


	@staticmethod
	def get_all_artists(db=defaultdb):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "SELECT first_name, last_name FROM users WHERE user_type = 'artist';"
		c.execute(statement,)
		name_list = c.fetchall()
		print(name_list)

# DB.get_all_artists()