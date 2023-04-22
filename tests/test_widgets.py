from pages.page_widgets import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage


class TestWidgets:
    class TestAccordian:
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            text_first = accordian_page.checking_section_accordion('first')
            assert text_first[0] == 'What is Lorem Ipsum?' and text_first[1] > 0, 'error in first section'
            text_second = accordian_page.checking_section_accordion('second')
            assert text_second[0] == 'Where does it come from?' and text_second[1] > 0, 'error in second section'
            text_third = accordian_page.checking_section_accordion('third')
            assert text_third[0] == 'Why do we use it?' and text_third[1] > 0, 'error in third section'

    class TestAutoComplete:
        def test_element_addition(self, driver):
            auto_complete_pege = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_pege.open()
            colors_in = auto_complete_pege.color_input('multiple', 3)
            colors_out = auto_complete_pege.checking_entered_colors('multiple')
            assert colors_in == colors_out, 'input error in multiple color'
            color_in = auto_complete_pege.color_input('single')
            color_out = auto_complete_pege.checking_entered_colors('single')
            assert color_in == color_out, 'input error in single color'

        def test_cleansing_entire_field(self, driver):
            auto_complete_pege = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_pege.open()
            auto_complete_pege.color_input('multiple', 3)
            auto_complete_pege.clear_input_field(0)
            colors_out = auto_complete_pege.checking_entered_colors('multiple')
            assert len(colors_out) == 0, 'multiple input field not cleared'
            auto_complete_pege.color_input('single')
            auto_complete_pege.clear_input_field(1)
            colors_out = auto_complete_pege.checking_entered_colors('single')
            assert len(colors_out) == 0, 'single input field not cleared'

        def test_removing_individual_color(self, driver):
            auto_complete_pege = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_pege.open()
            auto_complete_pege.color_input('multiple', 3)
            before_out = auto_complete_pege.checking_entered_colors('multiple')
            auto_complete_pege.remove_color()
            after_out = auto_complete_pege.checking_entered_colors('multiple')
            assert len(before_out) == len(after_out) + 1, 'color not removed'

    class TestDatePicker:
        def test_checking_current_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            current_date = date_picker_page.current_date()
            from_site_date = date_picker_page.getting_date('date')
            assert current_date == from_site_date, 'current date on the site is not correct'
            from_site_date_time = date_picker_page.current_date_with_time()
            date_and_time = date_picker_page.getting_date('date_time')
            assert from_site_date_time in date_and_time, 'current date with time on the site is not correct'

        def test_select_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            date_in = date_picker_page.data_entry_in_select_date()
            date_out = date_picker_page.getting_date('date')
            assert date_out == date_in, 'entered date did not match'

        def test_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            date_in = date_picker_page.date_and_time_change()
            date_out = date_picker_page.getting_date('date_time')
            assert date_out == date_in, "entered date and time did not match"

    class TestSlider:
        def test_slider(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            before, after = slider_page.changing_slider_value()
            assert before != after, 'slider stays in place'

    class TestProgressBar:
        def test_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            value = progress_bar_page.changing_progress_bar_value()
            assert value > 0, "progress bar didn't move"

        def test_reset_function(self, driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            value = progress_bar_page.progress_bar_update()
            assert value == 0, 'progress bar not updated'

    class TestTabs:
        def test_tabs(self, driver):
            tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            title, text = tabs_page.working_with_tabs('what')
            assert title == 'What' and text > 0, 'failed to get data from tab'
            title, text = tabs_page.working_with_tabs('use')
            assert title == 'Use' and text > 0, 'failed to get data from tab'
            title, text = tabs_page.working_with_tabs('origin')
            assert title == 'Origin' and text > 0, 'failed to get data from tab'
            title, text = tabs_page.working_with_tabs('more')
            assert title == 'More' and text > 0, 'failed to get data from tab'

    class TestToolTips:
        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            text_button = tool_tips_page.hover_over_elements("button")
            assert text_button == 'You hovered over the Button', 'no tooltip text on button hover'
            text_input = tool_tips_page.hover_over_elements("input")
            assert text_input == 'You hovered over the text field', 'no tooltip text on input hover'
            text_first = tool_tips_page.hover_over_elements("Contrary")
            assert text_first == 'You hovered over the Contrary', 'no tooltip text on Contrary hover'
            text_second = tool_tips_page.hover_over_elements("1.10.32")
            assert text_second == 'You hovered over the 1.10.32', 'no tooltip text on 1.10.32 hover'
