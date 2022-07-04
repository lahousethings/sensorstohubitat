from seleniumbase import BaseCase
from selenium.webdriver.common.keys import Keys

class HomeTest(BaseCase,Keys):

    def test_geri_temperature(self):

        self.open("https://www.worldweatheronline.com/geri-weather/nicosia/cy.aspx")
        self.get_text("div.weather-widget-temperature")
        geriweather = self.get_text("div.weather-widget-temperature")[:2]
        self.open_url("http://192.168.90.254/apps/api/1241/devices/7257/setTemperature/"+geriweather+"?access_token=d1303322-7a9c-474a-a385-b37ef32b2103")

    def test_pool_temperature(self):

        self.open("https://oxymaticapp.hydrover.eu/")
        self.send_keys("user","Lahome")
        self.send_keys("password","8mIHfx4A")

        self.click("send")

    def test_cmi_temperature(self):

        #Login
        self.open("https://cmi.ta.co.at/")
        self.send_keys("name=username", "argyrou@gmail.com")
        self.send_keys("name=passwort", "I6F5X98@xYfP")
        self.click(".mb-2")

        #Get Values
        self.goto("https://cmi027950.cmi.ta.co.at/webi/schema.html#1")

        # Set Values as Variables
        poolcmi = self.get_text("#pos11")[:4]

        # Update Values in Hubitat
        self.open_url("http://192.168.90.254/apps/api/1241/devices/6964/setTemperature/"+poolcmi+"?access_token=d1303322-7a9c-474a-a385-b37ef32b2103")














