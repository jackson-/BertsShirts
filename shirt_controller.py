from shirt_views import Views
from shirt_models import DB, User, Customer, Artist, Design, Notification

class Controller:

	def sign_in(self):
		while(True):
			self.username = Views.sign_in()
			self.userobj = DB.load_user(self.username)
			if self.userobj == None:
				self.registration()
			else:
				self.main_menu()


	def registration(self):
		while(True):
			choice = Views.user_prompt("You do not seem to have an account with us. Would you like to make one? Y/N: ")
			if choice == 'y' or choice == 'Y':
				self.user_type = Views.user_prompt("Are you an artist or a customer?: ")
				if self.user_type == 'artist' or self.user_type == 'Artist' or self.user_type == 'ARTIST':
					self.first_name = Views.user_prompt("What is your first name?: ")
					self.last_name = Views.user_prompt("What is your last name?: ")
					DB.create_artist(self.first_name, self.last_name, self.username, self.user_type)
					print("This works")
				elif self.user_type == 'customer' or self.user_type == 'Customer' or self.user_type == 'CUSTOMER':
					self.first_name = Views.user_prompt("What is your first name?: ")
					self.last_name = Views.user_prompt("What is your last name?: ")
					DB.create_customer(self.first_name, self.last_name, self.username, self.user_type)
					print("This works")
				else:
					print("That is not a valid answer. Try again.")
					self.registration()
			else:
				self.sign_in()

shirt_con = Controller()
shirt_con.sign_in()