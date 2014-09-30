from tests.integration.test_base import BaseIntegrationTest


class TestCustomDataDragAndDropRendering(BaseIntegrationTest):
    PAGE_TITLE = 'Drag and Drop v2'
    PAGE_ID = 'drag_and_drop_v2'

    def setUp(self):
        super(TestCustomDataDragAndDropRendering, self).setUp()

        scenario_xml = self._get_custom_scenario_xml("integration/data/test_html_data.json")
        self._add_scenario(self.PAGE_ID, self.PAGE_TITLE, scenario_xml)

        self.browser.get(self.live_server_url)
        self._page = self.go_to_page(self.PAGE_TITLE)

        header1 = self.browser.find_element_by_css_selector('h1')
        self.assertEqual(header1.text, 'XBlock: ' + self.PAGE_TITLE)

    def test_items_rendering(self):
        items = self._get_items()

        self.assertEqual(len(items), 3)
        self.assertEqual(self.get_element_html(items[0]), "<b>A</b>")
        self.assertEqual(self.get_element_html(items[1]), "<i>B</i>")
        self.assertEqual(self.get_element_html(items[2]), '<span style="color:red">X</span>')