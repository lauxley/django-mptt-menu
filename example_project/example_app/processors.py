from mpttmenu.processors import MenuProcessor

class ExampleProcessor(MenuProcessor):
    """
    We want to have this behavior:
    On the home page and pages not present in the menu, only show the root menus;
    On the listing pages, show the root menus as well as as the sibblings of the current node;
    On a detail page behave like the parent listing page.
    """

    def determine_tree(self):
        return self._get_root_and_branch_nodes()

    def get_default_tree(self):
        return self._get_root_nodes()
