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
				self.first_name = self.userobj[1]
				self.last_name = self.userobj[2]
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
				self.userobj.create_design(title, self.my_id, self.first_name + " " + self.last_name, price)
				print("Your design has been submitted into the store!")
			elif choice == '2':
				design_list = DB.get_design_stats(self.my_id)
				if design_list == None:
					print("I'm sorry but you don't have any stats at this time.")
				else:
					Views.design_stats(design_list)
			elif choice == '3':
				notification_list = DB.get_notifications(self.my_id)
				if notification_list == None:
					print("Sorry you have no notifications at this time.")
				else:
					Views.view_notifications(notification_list)
			elif choice == '4':
				self.sign_in()
			else:
				Views.invalid_choice()



	def main_menu_customer(self):
		while(True):
			choice = Views.main_menu_customer()
			if choice == '1':
				design_list = DB.get_all_designs()
			if design_list == None:
					print("I'm sorry the store is empty at this time.")
			else:
				choice = Views.view_store(design_list)
				if choice.isdigit():
					design_id = design_list[int(choice)-1][0]
					self.userobj.add_to_inventory(design_id, self.my_id)
				else:
					Views.invalid_choice()
			elif choice == '2':
				inventory_list = DB.get_inventory(self.my_id)
				if inventory_list == None:
					print("I'm sorry but your inventory is empty at this time.")
				else:
					Views.inventory_view(inventory_list)
			elif choice == '3':
				notification_list = DB.get_notifications(self.my_id)
				if notification_list == None:
					print("Sorry you have no notifications at this time.")
				else:
					Views.view_notifications(notification_list)
			elif choice == '4':
				artist_name = Views.subscribe_to_artist()

			elif choice == '5':
				self.sign_in()
			else:
				Views.invalid_choice()

shirt_con = Controller()
shirt_con.sign_in()