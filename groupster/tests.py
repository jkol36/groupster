from selenium.webdriver.firefox.webdriver import WebDriver
from django.test import LiveServerTestCase

class MySeleniumTest(LiveServerTestCase):
	name = "Jon Kolman"
	gender = "Male"
	college = "Drexel"
	year_in_college = "Freshman"
	college_email = "Jon@drexel.edu"
	positions_interested_in = "Administrative Aid Intern"
	affiliated_with_greek_life = "Absolutely"
	why_groupster = "Because Groupster is awesome"
	skills = "Backend and front end engineer"
	why_hire = "Because I'm awesome!"



	def testJobForm(self):
		self.selenium.get('%s%s' %(self.live_server_url, '/job/'))
		#name_input = self.selenium.find_element_by_name('name')
		#name_input.send_key()
		#gender_select = self.selenium.find_element_by_name('gender')

