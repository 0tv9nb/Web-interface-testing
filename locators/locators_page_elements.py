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
    ACTIVE_CHECK_BOX = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    ANCESTOR_ACTIVE_CHECK_BOX = ".//ancestor::span[@class='rct-text']"


class RadioButtonLocators:
    RADIO_YES = (By.CSS_SELECTOR, "label[for='yesRadio']")
    RADIO_IMPRESSIVE = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    RADIO_NO = (By.CSS_SELECTOR, "label[for='noRadio']")
    OUTPUT_SELECTED = (By.CSS_SELECTOR, "span[class='text-success']")


class WebTablesLocators:
    # add form
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    FIRST_NAME = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE = (By.CSS_SELECTOR, "input[id='age']")
    SALARY = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")
    # table
    SEARCH = (By.CSS_SELECTOR, "input[id='searchBox']")
    EDIT = (By.CSS_SELECTOR, "span[class='mr-2']")
    DELETE = (By.CSS_SELECTOR, "span[id^='delete-record']")
    ROW_DATA = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    ROW_PERENTS = ".//ancestor::div[@class='rt-tr-group']"
    NO_DATA = (By.CSS_SELECTOR, "div[class='rt-noData']")
    # drop_down_list
    SELECT_LIST = (By.CSS_SELECTOR, "select[aria-label='rows per page']")


class ButtonsLocators:
    # buttons
    BUTTONS = (By.CSS_SELECTOR, "button[class='btn btn-primary']")
    # message
    DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")
    RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, "p[id='rightClickMessage']")
    CLICK_MESSAGE = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")


class LinkLocators:
    SIMPLE_LINK = (By.CSS_SELECTOR, "a[id='simpleLink']")
    BAD_REQUEST = (By.CSS_SELECTOR, "a[id='bad-request']")
    TEST = (By.CSS_SELECTOR, "div[class='card mt-4 top-card']")


class UploadAndDownloadLocators:
    UPLOAD_FILE = (By.CSS_SELECTOR, "input[id='uploadFile']")
    UPLOAD_INFA = (By.CSS_SELECTOR, "p[id='uploadedFilePath']")
    DOWNLOAD_FILE = (By.CSS_SELECTOR, "a[id='downloadButton']")
