import sqlite3

class User:

	def __init__(self, username, first_name, last_name):
		self.username = username
		self.first_name = first_name
		self.last_name = last_name

	def create_account(self):


class Customer(User):
	pass


class Artist(User):
	pass


class Design:

	def __init__(self, title, price):
		self.title = title
		self.price = price


class Notification:

	def __init__(self, message):
		self.message = message


class Transactions:

	def __init__(self):
		pass