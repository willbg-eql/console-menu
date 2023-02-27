from consolemenu.items import MenuItem


class SubmenuItem(MenuItem):
    """
    A menu item to open a submenu
    """

    def __init__(self, text, submenu, menu=None, should_exit=False, menu_char=None):
        """
        :ivar str text: The text shown for this menu item
        :ivar ConsoleMenu submenu: The submenu to be opened when this item is selected
        :ivar ConsoleMenu menu: The menu to which this item belongs
        :ivar bool should_exit: Whether the menu should exit once this item's action is done
        """
        super(SubmenuItem, self).__init__(text=text, menu=menu, should_exit=should_exit, menu_char=menu_char)

        self.submenu = submenu
        if menu:
            self.get_submenu().parent = menu

    def set_menu(self, menu):
        """
        Sets the menu of this item.
        Should be used instead of directly accessing the menu attribute for this class.

        :param ConsoleMenu menu: the menu
        """
        self.menu = menu
        self.get_submenu().parent = menu

    def set_up(self):
        """
        This class overrides this method
        """
        self.menu.pause()
        self.menu.clear_screen()

    def action(self):
        """
        This class overrides this method
        """
        self.get_submenu().start()

    def clean_up(self):
        """
        This class overrides this method
        """
        self.get_submenu().join()
        self.menu.clear_screen()
        self.menu.resume()

    def get_return(self):
        """
        :return: The returned value in the submenu
        """
        return self.get_submenu().returned_value

    def get_submenu(self):
        """
        We unwrap the submenu variable in case it is a reference to a method that returns a submenu
        """
        return self.submenu if not callable(self.submenu) else self.submenu()
