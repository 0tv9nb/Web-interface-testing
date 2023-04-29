from selenium.webdriver.common.by import By


class SortableLocators:
    # tab
    TAB_LIST = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    TAB_GRID = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    # item
    ITEM_LIST = (By.CSS_SELECTOR, "div[id='demo-tabpane-list'] div[class='list-group-item list-group-item-action']")
    ITEM_GRID = (By.CSS_SELECTOR, "div[id='demo-tabpane-grid'] div[class='list-group-item list-group-item-action']")


class SelectableLocators:
    # tab
    TAB_LIST = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    TAB_GRID = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    # container
    LIST_CONTAINER = (By.CSS_SELECTOR, "li[class='mt-2 list-group-item list-group-item-action']")
    GRID_CONTAINER = (By.CSS_SELECTOR, "li[class='list-group-item list-group-item-action']")
