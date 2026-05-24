class DemoTestRecord:
    def __init__(self,page):
        self.page = page

    def navigate(self,url):
        self.page.goto(url)

    def login(self,username,password):
        self.page.get_by_role("textbox", name="username").click()
        self.page.get_by_role("textbox", name="Username").fill(username)
        self.page.get_by_role("textbox", name="Username").press("Tab")
        self.page.get_by_role("textbox", name="Password").fill(password)

    def submit(self):
        self.page.get_by_role("button", name="Submit").click()

    def clickOnLink(self,linkName):
        self.page.get_by_role("link", name=linkName).click()




