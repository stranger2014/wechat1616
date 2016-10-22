from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
'''user=User.objects.create_user(username='abc',password='123',email='')
user.save
fixtures=['productdata.json']
c=Client()
response=c.post('/a/login',{'username':'zsw','password':'abc12345'})
statuscode=response.status_code
print(response)
#response=c.get('/a/activity/list')
if "activity_list" in response.content:
    print("ok")
else:
    print("gameover")
#TestCase.assertIn(response,"activity")
#TestCase.assertContains(response,"activity_list")


from django.contrib.auth.models import User
from django.test.client import Client

# store the password to login later
password = 'mypassword'

my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', password)

c = Client()

# You'll need to log him in before you can send requests through the client
c.login(username=my_admin.username, password=password)
print('***********************')'''
#print(response.content)
# Create your tests here.
from django.test import LiveServerTestCase
from django.contrib.auth.models import User

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import urllib.request
import urllib.parse
import http.cookiejar
import os

class AdminTestCase(LiveServerTestCase):
    def setUp(self):
        # setUp is where you instantiate the selenium webdriver and loads the browser.
        ''
        #self.selenium=webdriver.Firefox()
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        super(AdminTestCase, self).setUp()

    def tearDown(self):
        # Call tearDown to close the web browser
        self.selenium.quit()
        super(AdminTestCase, self).tearDown()

    def test_create_user(self):
        self.myadmin = User.objects.create_superuser(
            username='abc',
            password='123',
            email='admin@example.com'
        )
        self.c=Client()
        #reponse=self.c.login(username=self.myadmin.username,password='123')
        self.assertTrue(self.c.login(username=self.myadmin.username,password='123'))
        """
        Django admin create user test
        This test will create a user in django admin and assert that
        page is redirected to the new user change form.
        """
        # Open the django admin page.
        # DjangoLiveServerTestCase provides a live server url attribute
        # to access the base url in tests
        '''self.selenium.get(
            '%s%s' % (self.live_server_url,  "/a/login")
        )

        # Fill login information of admin
        username = self.selenium.find_element_by_id("inputUsername")
        username.send_keys("abc")
        password = self.selenium.find_element_by_id("inputPassword")
        password.send_keys("123")

        # Locate Login button and click it
        self.selenium.find_element_by_xpath('//input[@id="loginnow"]').click()
        #WebDriverWait(self.browser, 10)
        self.selenium.get(
            '%s%s' % (self.live_server_url, "/a/activity/list")
        )'
        WebDriverWait(self.browser,10)

        self.assertIn("活动列表 - 紫荆之声", self.selenium.title)

        WebDriverWait(self.browser,10)
       # response=self.selenium.find_element_by_id("asdfg")

        self.selenium.get(
            '%s%s' % (self.live_server_url, "/a/activity/list")
        )
        print("*********************ok at this place*************************");

        # Fill the create user form with username and password
        self.selenium.find_element_by_id("id_username").send_keys("test")
        self.selenium.find_element_by_id("id_password1").send_keys("test")
        self.selenium.find_element_by_id("id_password2").send_keys("test")

        # Forms can be submitted directly by calling its method submit
        self.selenium.find_element_by_id("user_form").submit()'''
    def test_user_logout(self):
        self.selenium.get(
            '%s%s' % (self.live_server_url, "/a/activity/list")
        )

        #WebDriverWait(self.browser, 10)

        self.assertIn("活动列表 - 紫荆之声", self.selenium.title)
