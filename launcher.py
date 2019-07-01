import os
import subprocess

''' When run, this program will initialize all the necessary components for a basic Flask application.
	Those components include:
	- create new directories
		- templates folder
			- layout.html
			- home.html
		- static folder
			- main.css
	- app.py
	- .gitignore


	This program will also include a terminal menu where the user will input the name of the project.
	The user will also be able to select from what default bootstrap template they would like to use.
'''
class FlaskInitializer:
	def __init__(self):
		self.app_name = ''
		self.path = ''

	# # ---------------
	# Main Menu
	# ---------------
	def main_menu(self):
		run = True
		print('Welcome to the Initializer')
		while(run):
			user_input = input('1) Create Flask App\n2) Quit\n')
			print(f'You entered {user_input}')
			if user_input == '1':
				# Collect app name
				self.app_name = input('Enter the name of your Flask app: ')
				print(f'App Name: {self.app_name}')

				# Collect User Path
				self.path = input('Enter the path for the project location: ')
				print(f'Path: {self.path}')

				# Get the bootstrap style
				style = ''
				print('Choose the bootstrap style')
				bootstrap = input("1) Cover\n2) Album\n3) Carousel\n4) Pricing\n")
				if bootstrap == '1':
					print('You chose cover')
					style = 'cover'
				elif bootstrap == '2':
					print('You chose album')
					style = 'album'
				elif bootstrap == '3':
					print('You chose carousel')
					style = 'carousel'
				elif bootstrap == '4':
					print('You chose pricing')
					style = 'pricing'

				# Create template
				self.create_template(self.app_name ,style)

			elif user_input == '2':
				print("Ok Bye!")
				run = False 
				break

	# ---------------------
	# Create Template
	# ---------------------
	def create_template(self, app_name, template_name):
		self.create_directories(app_name)
		self.create_html(app_name, template_name)
		self.create_css(app_name, template_name)
		self.create_app(app_name)
		self.create_gitignore(app_name)

	# ---------------------
	# Create New Directories
	# ---------------------
	def create_directories(self, app_name):
		print('Creating Directories')
		os.makedirs(f'{self.path}/{app_name}')
		os.makedirs(f'{self.path}/{app_name}/templates')
		os.makedirs(f'{self.path}/{app_name}/static')
		print('Directories Created')

	# ---------------------
	# Create html
	# ---------------------
	def create_html(self, app_name, template_name):
		# Get the html
		layout_html = open(f'./{template_name}/layout.html', 'r')
		home_html = open(f'./{template_name}/home.html', 'r')
		
		# Read files
		layout_boiler_plate = layout_html.read()
		home_boiler_plate = home_html.read()

		# Create html file 
		print('Creating HTML')
		layout = open(f'{self.path}/{app_name}/templates/layout.html', 'w')
		home = open(f'{self.path}/{app_name}/templates/home.html', 'w')

		# Write to files
		layout.write(layout_boiler_plate)
		home.write(home_boiler_plate)
		print('HTML Done')

	# ---------------------
	# Create CSS
	# ---------------------
	def create_css(self, app_name, template_name):
		# Get the CSS
		home_html = open(f'./{template_name}/main.css', 'r')
		boiler_plate = home_html.read()

		# Create CSS file with content
		print('Creating css')
		home = open(f'{self.path}/{app_name}/static/main.css', 'w')
		home.write(boiler_plate)
		print('css Done')

	# ---------------------
	# Create App.py
	# ---------------------
	def create_app(self, app_name):
		# Get the py
		app = open(f'./app.py', 'r')
		boiler_plate = app.read()

		# Create py file with content
		print('Creating App.py')
		app = open(f'{self.path}/{app_name}/app.py', 'w')
		app.write(boiler_plate)
		print('App Done')

	# ---------------------
	# Create .GitIgnore
	# ---------------------
	def create_gitignore(self, app_name):
		exclude = ['__pycache__', 'env']
		gitignore = open(f'{self.path}/{app_name}/.gitignore', 'w')
		for i in exclude:
			gitignore.write(i + '\n')

# ---------------------
# Testing
# ---------------------
def main():
	i = FlaskInitializer()
	i.main_menu()

if __name__ == '__main__':
	main()
