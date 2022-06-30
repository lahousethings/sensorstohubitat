from seleniumbase import BaseCase

class HomeTest(BaseCase):
    def test_home_page(self):

        self.open("https://practice.automationbro.com/")

        self.assert_title("Practice E-Commerce Site – Automation Bro")

        self.click("#get-started")
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url,"https://practice.automationbro.com/#get-started")

        self.assert_text("Think different. Make different." , "h1")

        self.scroll_to_bottom()
        self.assert_text("Copyright © 2020 Automation Bro",".tg-site-footer-section-1")
