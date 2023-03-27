from selenium.webdriver.common.by import By


class TextBoxLocators:
    # input
    FULL_NAME = (By.CSS_SELECTOR, 'input[id="userName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')
    # output
    OUTPUT = (By.CSS_SELECTOR, "div[id='output']")


class CheckBoxLocators:
    EXPAND_ALL = (By.CSS_SELECTOR, "button[class='rct-option rct-option-expand-all']")
    COLLAPSE_ALL = (By.CSS_SELECTOR, "button[class='rct-option rct-option-collapse-all']")
    CHECK_BOX_LIST = (By.CSS_SELECTOR, "span[class='rct-checkbox']")
    RESULT = (By.CSS_SELECTOR, "div[id='result']")
