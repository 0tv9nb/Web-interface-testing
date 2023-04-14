from pages.page_widgets import AccordianPage, AutoCompletePage


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
            auto_complete_pege.remove_colors(0)
            colors_out = auto_complete_pege.checking_entered_colors('multiple')
            assert len(colors_out) == 0, 'multiple input field not cleared'
            auto_complete_pege.color_input('single')
            # auto_complete_pege.remove_colors(1)
            colors_out = auto_complete_pege.checking_entered_colors('single')
            assert len(colors_out) == 0, 'single input field not cleared'
