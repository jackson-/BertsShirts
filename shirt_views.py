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
			WELCOME TO BERTS SHIRTS BITCH!


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
