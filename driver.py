from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import DRIVER

class Browser(object):
    try:
        options = Options()
        # options.add_argument('--headless')
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(DRIVER, options=options)
        driver.implicitly_wait(30)
        driver.set_page_load_timeout(30)
        print("[BUILD] Driver created successfully.")
    except RuntimeError as e:
        raise AssertionError("[ERROR] -- Driver can not be created.")

    def close(self):
        print("\n[FINISHED] -- TEST CASE EXECUTED.")
        self.driver.close()
        self.driver.quit()
