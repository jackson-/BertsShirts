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
				self.my_id = self.userobj[0]
				self.user_type = DB.check_user_type(self.userobj[0])[0]
				if self.user_type == 'artist':
					self.userobj = Artist(self.user_type)
					self.main_menu_artist()
				elif self.user_type == 'customer':
					self.userobj = Customer(self.user_type)
					self.main_menu_customer()



	def registration(self):
		while(True):
			choice = Views.user_prompt("You do not seem to have an account with us. Would you like to make one? Y/N: ")
			if choice == 'y' or choice == 'Y':
				self.user_type = Views.user_prompt("Are you an artist or a customer?: ")
				if self.user_type == 'artist':
					self.first_name = Views.user_prompt("What is your first name?: ")
					self.last_name = Views.user_prompt("What is your last name?: ")
					DB.create_artist(self.first_name, self.last_name, self.username, self.user_type)
					self.userobj = DB.load_user(self.username)
					self.my_id = self.userobj[0]
					self.userobj = Artist(self.user_type)
					self.main_menu_artist()
				elif self.user_type == 'customer':
					self.first_name = Views.user_prompt("What is your first name?: ")
					self.last_name = Views.user_prompt("What is your last name?: ")
					DB.create_customer(self.first_name, self.last_name, self.username, self.user_type)
					self.userobj = DB.load_user(self.username)
					self.my_id = self.userobj[0]
					self.userobj = Customer(self.user_type)
					self.main_menu_customer()
				else:
					Views.invalid_choice()
					self.registration()
			else:
				self.sign_in()

	def main_menu_artist(self):
		while(True):
			choice = Views.main_menu_artist()
			if choice ==  '1':
				title = Views.user_prompt("What is the title of your new design?: ")
				price = Views.user_prompt("What is the price of your new design?: ")
				self.userobj.create_design(title, self.my_id, price)
				print("This works")
			elif choice == '2':
				pass
			elif choice == '3':
				pass
			elif choice == '4':
				self.sign_in()
			else:
				Views.invalid_choice()



	def main_menu_customer(self):
		while(True):
			choice = Views.main_menu_customer()
			if choice == '1':
				pass
			elif choice == '2':
				pass
			elif choice == '3':
				pass
			elif choice == '4':
				pass
			elif choice == '5':
				self.sign_in()
			else:
				Views.invalid_choice()


shirt_con = Controller()
shirt_con.sign_in()