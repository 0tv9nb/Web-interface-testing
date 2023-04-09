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
    PROMT_BUTTON_MESSAGE = (By.CSS_SELECTOR, "span[id = 'promptResult']")


class FramesLocators:
    # frames
    BIG_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    SMOL_FRAME = (By.CSS_SELECTOR, "iframe[id='frame2']")
    # text
    FRAME_TEXT = (By.CSS_SELECTOR, "h1[id='sampleHeading']")


class NestedFramesLocators:
    # frames
    OUTER_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    INNER_FRAME = (By.CSS_SELECTOR, "iframe")
    # text
    FRAME_TEXT = (By.CSS_SELECTOR, "body")


class ModalDialogsLocators:
    # buttons
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='showSmallModal']")
    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='showLargeModal']")
    SMALL_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[id='closeSmallModal']")
    LARGE_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[id='closeLargeModal']")
    # texts
    SMALL_MODAL_TITEL = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-sm']")
    LARGE_MODAL_TITEL = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-lg']")
    MODAL_TEXT = (By.CSS_SELECTOR, "div[class='modal-body']")