from selenium.webdriver.common.by import By


class BrowserWindowsLocators:
    # buttons
    NEW_TAB = (By.CSS_SELECTOR, "button[id = 'tabButton']")
    NEW_WINDOW = (By.CSS_SELECTOR, "button[id = 'windowButton']")
    NEW_WINDOW_MESSAGE = (By.CSS_SELECTOR, "button[id = 'messageWindowButton']")


class AlertsLocators:
    # buttons
    ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='alertButton']")
    TIMER_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
    PROMT_BUTTON = (By.CSS_SELECTOR, "button[id='promtButton']")
    # message
    CONFIRM_BUTTON_MESSAGE = (By.CSS_SELECTOR, "span[id = 'confirmResult']")
    PROMT_BUTTON_MESSAGE = (By.CSS_SELECTOR, "span[id = 'confirmResult']")
