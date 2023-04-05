from pages.page_alerts_frame_windows import BrowserWindowsPage


class TestBrowserWindows:
    def test_browser_windows(self, driver):
        browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
        browser_windows_page.open()
        browser_windows_page.click_button("new_tab")
        url_tab = browser_windows_page.checking_transition_to_new_window(2)
        assert url_tab == 'https://demoqa.com/sample'
        browser_windows_page.click_button("new_window")
        url_window = browser_windows_page.checking_transition_to_new_window(3)
        assert url_window == 'https://demoqa.com/sample'
        # browser_windows_page.click_button("new_window_message")
        # browser_windows_page.checking_transition_to_new_window()
        # assert url_window_message == 'https://demoqa.com/sample'
