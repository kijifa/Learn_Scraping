

class Scraper:

    def open_browser(self,url,webdriver_path):
        driver = webdriver.Chrome(executable_path=webdriver_path)

        driver.get(url)

        return

    def __init__(self):
        pass
