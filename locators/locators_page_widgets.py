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
    # select
    SELECT_DATE_INPUT = (By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']")
    SELECT_DATE_MONTH = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    SELECT_DATE_YEAR = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    # time
    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, "input[id='dateAndTimePickerInput']")
    DATE_AND_MONTH = (By.CSS_SELECTOR, "div[class='react-datepicker__month-read-view']")
    DATE_AND_MONTH_ITEM = (By.CSS_SELECTOR, "div[class^='react-datepicker__month-option']")
    DATE_AND_YEAR = (By.CSS_SELECTOR, "div[class='react-datepicker__year-read-view']")
    DATE_AND_YEAR_ITEM = (By.CSS_SELECTOR, "div[class^='react-datepicker__year-option']")
    DATE_AND_TIME_ITEM = (By.CSS_SELECTOR, "li[class='react-datepicker__time-list-item '] ")
    DATE_AND_YEAR_ITEM_UP = (By.CSS_SELECTOR, "div[class='react-datepicker__year-option']:first-child")
    DATE_AND_YEAR_ITEM_DOWN = (By.CSS_SELECTOR, "div[class='react-datepicker__year-option']:last-child")


class SliderLocators:
    SLIDER_VALUE = (By.CSS_SELECTOR, "input[id='sliderValue']")
    SLIDER_BUTTON = (By.CSS_SELECTOR, "input[class='range-slider range-slider--primary']")


class ProgressBarLocators:
    PROGRES_BAR_VALUE = (By.CSS_SELECTOR, "div[class='progress-bar bg-info']")
    PROGRES_BAR_BUTTON = (By.CSS_SELECTOR, "button[id='startStopButton']")
    RESET_BUTTON = (By.CSS_SELECTOR, "button[id='resetButton']")

