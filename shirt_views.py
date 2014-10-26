class Views:

	@staticmethod
	def user_prompt(string):
		return input(string)

	@staticmethod
	def invalid_choice():
		print("That was an invalid choice. Try again.")

	@staticmethod
	def sign_in():
		return input('''
			  WELCOME TO BERTS SHIRTS!


			        __.-.__.-.__
			      .'\ '-.__.-' /'.
			     /  |    ,_    |  \\
			    /   |  _/| \_  |   \\
			    '-._/ \.-""-./ \_.-'
			        | ( ^ _\^) |
			        |  \ == /  |
			        |  /'--'\  |
			        |          |
			        '._      _.'
			           `""""`


			What is your username: ''')


	@staticmethod
	def main_menu_customer():
		return input('''
			[1] Shop for designs
			[2] Check your inventory
			[3] Check notifications
			[4] Subscribe to an artist
			[5] Logout


			What would you like to do?: ''')


	@staticmethod
	def main_menu_artist():
		return input('''
			[1] Submit design
			[2] Check your design stats
			[3] Check notifications
			[4] Logout


			What would you like to do?: ''')

	@staticmethod
	def design_stats(design_list):
		for i in design_list:
			print("Your design {0} has been bought {1} times.".format(i[0], i[1]))


	@staticmethod
	def view_notifications(notification_list):
		for i in enumerate(notification_list):
			print(i[0], i[1][0])


	@staticmethod
	def view_store(design_list):
		item_num = 0
		for index in design_list:
			item_num += 1
			print('''
			{0}
			Artist Name: {1}
			Design Title: {2}
			Price: {3}
				'''.format(item_num, index[1], index[2], index[3]))
		return input("What design number would you like to buy?")


	@staticmethod
	def inventory_view(inventory_list):
		print("Here is you inventory: \n")
		for index in inventory_list:
			for value in range(1):
				print('''

			Design Title: {0}
			Artist Name: {1}

				'''.format(index[0], index[1]))


	@staticmethod
	def subscribe_to_artist(artist_list):
		for index in artist_list:
			print('''
			First Name: {0}
			Last Name: {1}


				'''.format(index[0], index[1]))