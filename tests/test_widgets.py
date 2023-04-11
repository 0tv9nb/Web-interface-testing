from pages.page_widgets import AccordianPage


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
