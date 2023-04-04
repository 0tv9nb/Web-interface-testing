from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class BasePage:
    """Methods for working with the page"""

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_presents(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_presents(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def remove_futer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")

    def option_select(self, text, locator):
        select = Select(self.element_is_visible(locator))
        select.select_by_visible_text(text)
    def action_double_click(self,element):
        action = ActionChains(self.driver)
        action.double_click(element).perform()
    def action_right_click(self,element):
        action = ActionChains(self.driver)
        action.context_click(element).perform()