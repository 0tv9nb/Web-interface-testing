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
    # input
    MULTIPLE_COLOR_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteMultipleInput']")
    SINGLE_COLOR_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteSingleInput']")
