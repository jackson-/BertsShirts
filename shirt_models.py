import sqlite3
import create_db

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


	def add_to_inventory(self, design_id):
		pass


	def delete_notification(self, notificaton_id):
		pass

	def subscribe(self, artist_id):
		pass


class Artist(User):

	def __init__(self, user_type):
		self.user_type = user_type

	
	def create_design(self):
		pass


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
	def create_user(first_name, last_name, username, user_type, db=defaultdb):
		conn = sqlite3.connect(db)
		c = conn.cursor()
		statement = "INSERT INTO users(first_name, last_name, username, user_type) VALUES(?, ?, ?); "
		c.execute(statement, (name, created_at, permission_level,))
		conn.commit()
		conn.close()