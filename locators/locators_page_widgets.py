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


class TabsLocators:
    # tab
    TAB_WHAT = (By.CSS_SELECTOR, "a[id='demo-tab-what']")
    TAB_USE = (By.CSS_SELECTOR, "a[id='demo-tab-use']")
    TAB_MORE = (By.CSS_SELECTOR, "a[id='demo-tab-more']")
    TAB_ORIGIN = (By.CSS_SELECTOR, "a[id='demo-tab-origin']")
    # text
    TAB_WHAT_TEXT = (By.CSS_SELECTOR, "div[id='demo-tabpane-what']")
    TAB_USE_TEXT = (By.CSS_SELECTOR, "div[id='demo-tabpane-use']")
    TAB_MORE_TEXT = (By.CSS_SELECTOR, "div[id='demo-tabpane-more']")
    TAB_ORIGIN_TEXT = (By.CSS_SELECTOR, "div[id='demo-tabpane-origin']")


class ToolTipsLocators:
    # element for hover
    BUTTON_FOR_HOVER = (By.CSS_SELECTOR, "button[id='toolTipButton']")
    INPUT_FOR_HOVER = (By.CSS_SELECTOR, "input[id='toolTipTextField']")
    FIRST_TEXT_HOVER = (By.CSS_SELECTOR, "div[id='texToolTopContainer'] a:first-child")
    SECOND_TEXT_HOVER = (By.CSS_SELECTOR, "div[id='texToolTopContainer'] a:last-child")
    # tex
    TEXT = (By.CSS_SELECTOR, "div[class='tooltip-inner']")


class MenuLocators:
    MENU_ITEMS = (By.CSS_SELECTOR, "ul[id='nav'] li a")
