from pages.page_interactions import SortablePage


class TestInteractions:
    class TestSortable:
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            before_list, after_list = sortable_page.mixing_elements('list')
            assert before_list != after_list, 'elements in list are not moved'
            before_grid, after_grid = sortable_page.mixing_elements('grid')
            assert before_grid != after_grid, 'elements in grid are not moved'
