class CreateTeamPage:
    def __init__(self, page):
        self.page = page
        self.name_input = page.locator('input[name="name"]')
        self.create = page.locator("text='Add'")

    def navigate(self):
        self.page.goto("https://e.se1.hr.dmerej.info/add_team")

    def fill(self):
       team_name = "test team"
       self.name_input.fill(team_name)
       self.create.click()