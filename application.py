from selenium import webdriver

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def fill_group_info(self, group):
        wd = self.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group info
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        self.submit_group_creation()

    def submit_group_creation(self):
        wd = self.wd
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        wd = self.wd
        # group page
        wd.find_element_by_link_text("group page").click()

    def logout(self):
        wd = self.wd
        # logout
        wd.find_element_by_link_text("Logout").click()

    def open_group_page(self):
        wd = self.wd
        # open groups page
        wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def stop(self):
        self.wd.quit()
