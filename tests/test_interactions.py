from pages.page_interactions import SortablePage, SelectablePage


class TestInteractions:
    class TestSortable:
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            before_list, after_list = sortable_page.mixing_elements('list')
            assert before_list != after_list, 'elements in list are not moved'
            before_grid, after_grid = sortable_page.mixing_elements('grid')
            assert before_grid != after_grid, 'elements in grid are not moved'
    class TestSelectable:
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            selectable_page.interaction_with_elements()