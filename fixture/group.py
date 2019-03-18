
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group info
        self.fill_group_info(group)
        self.submit_group_creation()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        # select first group
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_home_page()

    # editing group info
    def edit(self, new_group_info):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_info(new_group_info)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    # editing some fields info
    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    # Selecting first group
    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    # Filling out group info
    def fill_group_info(self, group):
        wd = self.app.wd
        self.change_field("group_name", group.name)
        self.change_field("group_header", group.header)
        self.change_field("group_footer", group.footer)

    def submit_group_creation(self):
        wd = self.app.wd
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        # group page
        wd.find_element_by_link_text("home").click()

    def open_group_page(self):
        wd = self.app.wd
        # open groups page
        wd.find_element_by_link_text("groups").click()
