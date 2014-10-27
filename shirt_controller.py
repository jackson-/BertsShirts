from shirt_views import Views
from shirt_models import DB, User, Customer, Artist, Design, Notification

class Controller:

	def sign_in(self):
		while(True):
			self.username = Views.sign_in()
			self.user = DB.load_user(self.username)
			print(self.user)
			if self.user == None:
				self.registration()
			else:
				self.user_type = DB.check_user_type(self.user[0])[0]
				if self.user_type == 'artist':
					self.userobj = Artist(my_id=self.user[0], first_name=self.user[1], last_name=self.user[2], user_type=self.user_type, username=self.username)
					print(self.userobj.first_name)
					self.main_menu_artist()
				elif self.user_type == 'customer':
					self.userobj = Customer(my_id=self.user[0], first_name=self.user[1], last_name=self.user[2], user_type=self.user_type, username=self.username)
					self.main_menu_customer()


	def registration(self):
		while(True):
			choice = Views.user_prompt("You do not seem to have an account with us. Would you like to make one? Y/N: ")
			if choice == 'y' or choice == 'Y':
				self.user_type = Views.user_prompt("Are you an artist or a customer?: ")
				if self.user_type == 'artist':
					first_name = Views.user_prompt("What is your first name?: ")
					last_name = Views.user_prompt("What is your last name?: ")
					DB.create_artist(first_name, last_name, self.username, self.user_type)
					self.user = DB.load_user(self.username)
					self.userobj = Artist(my_id=self.user[0], first_name=self.user[1], last_name=self.user[2], user_type=self.user_type, username=self.username)
					self.main_menu_artist()

				elif self.user_type == 'customer':
					self.first_name = Views.user_prompt("What is your first name?: ")
					self.last_name = Views.user_prompt("What is your last name?: ")
					DB.create_customer(self.first_name, self.last_name, self.username, self.user_type)
					self.user = DB.load_user(self.username)
					self.userobj = Customer(my_id=self.user[0], first_name=self.user[1], last_name=self.user[2], user_type=self.user_type, username=self.username)
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
				print(self.userobj.first_name)
				title = Views.user_prompt("What is the title of your new design?: ")
				price = Views.user_prompt("What is the price of your new design?: ")
				self.userobj.create_design(title, self.userobj.my_id, self.userobj.first_name + " " + self.userobj.last_name, price)
				subscription_list = DB.get_subscriptions(self.userobj.my_id)
				for index in subscription_list:
					for value in index:
						DB.create_notification(value, ("%s %s has released another design called %s. It is priced at %s." % (self.userobj.first_name, self.userobj.last_name, title, price)))
				print("Your design has been submitted into the storea and all your subscribers know!")
			elif choice == '2':
				design_list = DB.get_design_stats(self.userobj.my_id)
				if design_list == None:
					print("I'm sorry but you don't have any stats at this time.")
				else:
					Views.design_stats(design_list)
			elif choice == '3':
				notification_list = DB.get_notifications(self.userobj.my_id)
				if notification_list == None:
					print("Sorry you have no notifications at this time.")
				else:
					Views.view_notifications(notification_list)
			elif choice == '4':
				self.sign_in()
			else:
				Views.invalid_choice()



	def main_menu_customer(self):
		print(self.userobj.first_name)
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
						self.userobj.buy(design_id, self.userobj.my_id)
						DB.update_purchase_times(design_id)
					else:
						Views.invalid_choice()
			elif choice == '2':
				inventory_list = DB.get_inventory(self.userobj.my_id)
				if inventory_list == None:
					print("I'm sorry but your inventory is empty at this time.")
				else:
					inventory_list = DB.get_inventory(self.userobj.my_id)
					Views.inventory_view(inventory_list)
			elif choice == '3':
				notification_list = DB.get_notifications(self.userobj.my_id)
				if notification_list == None:
					print("Sorry you have no notifications at this time.")
				else:
					Views.view_notifications(notification_list)
			elif choice == '4':
				artist_list = DB.get_all_artist_names()
				artist_name = Views.subscribe_to_artist(artist_list)
				first_name = Views.user_prompt("What is the first name of the artist you want to subscribe to?: ")
				last_name = Views.user_prompt("What is the last name of the artist you want to subscribe to?: ")
				artist_id = DB.get_artist_id(first_name, last_name)
				if artist_id == None:
					Views.invalid_choice()
				else:
					self.userobj.subscribe(self.userobj.my_id, artist_id[0][0])
			elif choice == '5':
				self.sign_in()
			else:
				Views.invalid_choice()

shirt_con = Controller()
shirt_con.sign_in()