from pages.page_alerts_frame_windows import BrowserWindowsPage


class TestBrowserWindows:
    def test_browser_windows(self, driver):
        browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
        browser_windows_page.open()
        browser_windows_page.click_button("new_tab")
        browser_windows_page.click_button("new_window")
        browser_windows_page.click_button("new_window_message")
