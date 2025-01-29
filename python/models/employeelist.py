class EmployeeListPage:
    def __init__(self, page):
        self.page = page
        self.employee_table = page.locator("table")
        self.employee_rows = page.locator("table tr")  # Selects all rows
        self.version_text = page.locator("text=Version")  # Version information

    def navigate(self):
        self.page.goto("https://e.se1.hr.dmerej.info/employees")