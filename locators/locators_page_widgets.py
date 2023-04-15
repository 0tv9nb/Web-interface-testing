from selenium.webdriver.common.by import By


class AccordianLocators:
    # elements
    SECTION_HEADING_FIRST = (By.CSS_SELECTOR, "div[id='section1Heading']")
    SECTION_HEADING_SECOND = (By.CSS_SELECTOR, "div[id='section2Heading']")
    SECTION_HEADING_THIRD = (By.CSS_SELECTOR, "div[id='section3Heading']")
    # text
    SECTION_CONTENT_FIRST = (By.CSS_SELECTOR, "div[id='section1Content']")
    SECTION_CONTENT_SECOND = (By.CSS_SELECTOR, "div[id='section2Content']")
    SECTION_CONTENT_THIRD = (By.CSS_SELECTOR, "div[id='section3Content']")


class AutoCompleteLocators:
    # inputs
    MULTIPLE_COLOR_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteMultipleInput']")
    SINGLE_COLOR_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteSingleInput']")
    # colors
    ENTERED_MULTI_COLOR = (By.CSS_SELECTOR, "div[class='css-12jo7m5 auto-complete__multi-value__label']")
    ENTERED_SINGLE_COLOR = (By.CSS_SELECTOR, "div[class='auto-complete__single-value css-1uccc91-singleValue']")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "div[class='auto-complete__indicators css-1wy0on6']")
    REMOVE_COLOR = (By.CSS_SELECTOR, "div[class='css-xb97g8 auto-complete__multi-value__remove']")


class DatePickerLocators:
    # input
    SELECT_DATE_INPUT = (By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']")
    DATE_AND_TIME = (By.CSS_SELECTOR, "input[id='dateAndTimePickerInput']")