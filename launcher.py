import os
import subprocess

''' When run, this program will initialize all the necessary components for a Flask application.
	Those components include:
	- create new directory 
	- create virtual environment
	- pip install Flask
	- app.py
	- .gitignore
	- templates folder
		- layout.html
		- home.html
	- static folder
		- main.css

	This program will also include a terminal menu where the user will input the name of the project.
	The user will also be able to select from what default bootstrap template they would like to use.
'''
class FlaskInitializer:
	def __init__(self):
		self.app_name = ''

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

				# Get the bootstrap style
				style = ''
				print('Choose the bootstrap style')
				bootstrap = input("1) Cover\n2) Album\n3) Carousel\n4) Pricing")
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

	# ---------------------
	# Create New Directories
	# ---------------------
	def create_directories(self, app_name):
		print('Creating Directories')
		os.makedirs(f'C:/Users/spenc/OneDrive/Desktop/Coding/Python/{app_name}')
		os.makedirs(f'C:/Users/spenc/OneDrive/Desktop/Coding/Python/{app_name}/templates')
		os.makedirs(f'C:/Users/spenc/OneDrive/Desktop/Coding/Python/{app_name}/static')
		print('Directories Created')

	# ---------------------
	# Create html
	# ---------------------
	def create_html(self, app_name, template_name):
		# Get the html
		layout_html = open(f'C:/Users/spenc/OneDrive/Desktop/Coding/Python/FlaskInitializer/{template_name}/layout.html', 'r')
		home_html = open(f'C:/Users/spenc/OneDrive/Desktop/Coding/Python/FlaskInitializer/{template_name}/home.html', 'r')
		
		# Read files
		layout_boiler_plate = layout_html.read()
		home_boiler_plate = home_html.read()

		# Create html file 
		print('Creating HTML')
		layout = open(f'C:/Users/spenc/OneDrive/Desktop/Coding/Python/{app_name}/templates/layout.html', 'w')
		home = open(f'C:/Users/spenc/OneDrive/Desktop/Coding/Python/{app_name}/templates/home.html', 'w')

		# Write to files
		layout.write(layout_boiler_plate)
		home.write(home_boiler_plate)
		print('HTML Done')

	# ---------------------
	# Create CSS
	# ---------------------
	def create_css(self, app_name, template_name):
		# Get the CSS
		home_html = open(f'C:/Users/spenc/OneDrive/Desktop/Coding/Python/FlaskInitializer/{template_name}/main.css', 'r')
		boiler_plate = home_html.read()

		# Create CSS file with content
		print('Creating css')
		home = open(f'C:/Users/spenc/OneDrive/Desktop/Coding/Python/{app_name}/static/main.css', 'w')
		home.write(boiler_plate)
		print('css Done')

	# ---------------------
	# Create App.py
	# ---------------------
	def create_app(self, app_name):
		# Get the py
		app = open(f'C:/Users/spenc/OneDrive/Desktop/Coding/Python/FlaskInitializer/app.py', 'r')
		boiler_plate = app.read()

		# Create py file with content
		print('Creating App.py')
		app = open(f'C:/Users/spenc/OneDrive/Desktop/Coding/Python/{app_name}/app.py', 'w')
		app.write(boiler_plate)
		print('App Done')

	# ---------------------
	# Create Virtual Env
	# ---------------------
	def create_venv(self, app_name):
		print('Creating virtual environment')
		subprocess.Popen('python -m venv env', cwd=f'C:/Users/spenc/OneDrive/Desktop/Coding/Python/{app_name}')
		print('Created virtual environment')

	def install_package(self):
		subprocess.Popen('touch test.txt', cwd=f'C:/Users/spenc/OneDrive/Desktop/Coding/Python/{app_name}')
		subprocess.Popen('pip install Flask', cwd=f'C:/Users/spenc/OneDrive/Desktop/Coding/Python/{app_name}')


# ---------------------
# Testing
# ---------------------
def main():
	i = FlaskInitializer()
	i.main_menu()

if __name__ == '__main__':
	main()