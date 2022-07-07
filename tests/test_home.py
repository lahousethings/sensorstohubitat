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
        self.send_keys("name=user","Lahome")
        self.send_keys("name=password","8mIHfx4A")

        self.click(".send")
        self.click("//*[@main-id=2052]")
        self.wait(15)
        pool_numbers = self.find_elements("//*[starts-with(@class,'big-number')]")
        for index, pool_number in enumerate(pool_numbers,1):
            if index == 1:
                pool_number_1 = pool_number.text.replace(",",".")
                print(pool_number_1)
                self.open_url("http://192.168.90.254/apps/api/1241/devices/7041/setTemperature/"+pool_number_1+"?access_token=d1303322-7a9c-474a-a385-b37ef32b2103")





def test_cmi_temperature(self):

        #Login
        self.open("https://cmi.ta.co.at/")
        self.send_keys("name=username", "argyrou@gmail.com")
        self.send_keys("name=passwort", "I6F5X98@xYfP")
        self.click(".mb-2")

        #Get Values
        self.goto("https://cmi027950.cmi.ta.co.at/webi/schema.html#1")

        # Set Values as Variables
        temppoolcmi = self.get_text("#pos11")[:4]
        tempbasement = self.get_text("#pos31")[:4]
        temp0outsideveranda = self.get_text("#pos32")[:4]
        temp0groundfloor = self.get_text("#pos34")[:4]
        temp1stfloor = self.get_text("#pos33")[:4]


        # Update Values in Hubitat
        self.open_url("http://192.168.90.254/apps/api/1241/devices/6964/setTemperature/"+temppoolcmi+"?access_token=d1303322-7a9c-474a-a385-b37ef32b2103")
        self.open_url("http://192.168.90.254/apps/api/1241/devices/7044/setTemperature/"+tempbasement + "?access_token=d1303322-7a9c-474a-a385-b37ef32b2103")
        self.open_url("http://192.168.90.254/apps/api/1241/devices/7045/setTemperature/"+temp0outsideveranda + "?access_token=d1303322-7a9c-474a-a385-b37ef32b2103")
        self.open_url("http://192.168.90.254/apps/api/1241/devices/7043/setTemperature/" + temp0groundfloor + "?access_token=d1303322-7a9c-474a-a385-b37ef32b2103")
        self.open_url("http://192.168.90.254/apps/api/1241/devices/7042/setTemperature/" + temp1stfloor + "?access_token=d1303322-7a9c-474a-a385-b37ef32b2103")















