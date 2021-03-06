from django.test import TestCase
from django.test import Client
from .views import index, addStatus, DeleteStatus, profile
from .models import Statuy
from django.urls import resolve

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Create your tests here.
class Lab6Test(TestCase):
	def test_request_lab6(self):
		response = Client().get('/lab-6/status/')
		self.assertEqual(response.status_code,200)
	
	# def test_template_lab6(self):
	# 	response = Client().get('/lab-6/status')
	# 	self.assertTemplateUsed(response, 'status.html')

	# def test_func_lab6(self):
	# 	found = resolve('/lab-6/status/')
	# 	self.assertEqual(found.func, response)

	def test_model_can_create_new_status(self):
		new_status = Statuy.objects.create(isi_status = 'Bikin Kopi')
		counting_status = Statuy.objects.all().count()
		self.assertEqual(counting_status, 1)

	def test_profile_url_is_exist(self):
		response = Client().get('/lab-6/')
		self.assertEqual(response.status_code, 200)

	# def test_template_profile(self):
	# 	response = Client().get('/lab-6')	
	# 	self.assertTemplateUsed(response, 'profile.html')

	def test_func_profile(self):
		found = resolve('/lab-6/')
		self.assertEqual(found.func, profile)


class Lab6_FunctionalTest(TestCase):

	def setUp(self):
		chrome_options = Options()
		chrome_options.add_argument('--dns-prefetch-disable')
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('disable-gpu')
		self.selenium = webdriver.Chrome(
			'./chromedriver', chrome_options=chrome_options
		)
		super(Lab6_FunctionalTest, self).setUp()

	def tearDown(self):
		self.selenium.quit()
		super(Lab6_FunctionalTest, self).tearDown()

	def test_input_todo(self):
		selenium = self.selenium

		selenium.get('http://ppw-b-bramantio.herokuapp.com/lab-6/status')
		status = selenium.find_element_by_id('id_status')
		isi = selenium.find_element_by_id('id_isi_status')
		delete = selenium.find_element_by_id('delete_status')

		status.send_keys('Mengerjakan Lab PPW')
		isi.send_keys('Sedang berpikir')

		isi.send_keys(Keys.ENTER)

		self.assertIn('Mengerjakan Lab PPW', selenium.page_source)
		self.assertIn('Sedang berpikir', selenium.page_source)
		self.assertIn('delete_status', selenium.page_source)
		# super(Lab6_FunctionalTest, self).test_input_todo()

	# def test_position_and_css_form(self):
	# 	selenium = self.selenium

	# 	selenium.get('http://ppw-b-bramantio.herokuapp.com/lab-6/status')
		
	# 	delete = selenium.find_element_by_id('delete_status')
	# 	add = selenium.find_element_by_name('Add Status')
	# 	content = selenium.find_element_by_css_selector('table').value_of_css_property('color')

	# 	self.assertIn('Delete All', selenium.text)
	# 	self.assertIn('Add Status', selenium.text)

	# 	delete_button_use_class = "btn-default" in delete.get_attribute("class")
	# 	add_button_use_class = "btn-default" in add.get_attribute("class")

	# 	self.assertTrue(delete_button_use_class)
	# 	self.assertTrue(add_button_use_class)
