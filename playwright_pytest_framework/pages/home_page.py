class HomePage:
    def __init__(self, page):
        self.page = page

    def navigate_to(self, url="https://www.google.com"):
        self.page.goto(url)

    def search_for(self, text):
        self.page.fill("textarea[name='q']", text)
        self.page.press("textarea[name='q']", "Enter")