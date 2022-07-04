from seleniumbase import BaseCase

class HomeTest(BaseCase):

    def test_temperature(self):

        self.open("https://www.worldweatheronline.com/geri-weather/nicosia/cy.aspx")
        self.get_title()
        print(self.get_text("div.weather-widget-temperature"))
