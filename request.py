from selenium import webdriver

R_WEB_DRIVER_PATH = "/usr/local/bin/geckodriver"

class Request:
    def __init__(self):
        profile = webdriver.FirefoxProfile()
        # not good enough without actually modifying the drivers, so commenting it out for now
        # profile.set_preference("general.useragent.override", "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:85.0) Gecko/20100101 Firefox/85.0")
        # profile.set_preference("dom.webdriver.enabled", False)
        # profile.set_preference('useAutomationExtension', False)
        self.driver = webdriver.Firefox(firefox_profile=profile, executable_path=R_WEB_DRIVER_PATH)

    def get(self, url):
        try:
            self.driver.get(url)
            return self.driver
        except Exception as e:
            print(e)
