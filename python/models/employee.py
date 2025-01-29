class AddEmployeePage:
    def __init__(self, page):
        self.page = page
        # Initialize locators for each input field
        self.name_input = page.locator('input[name="name"]')
        self.email_input = page.locator('input[name="email"]')
        self.address_input = page.locator('#id_address_line1')
        self.city_input = page.locator('input[name="city"]')
        self.zip_code_input = page.locator('input[name="zip_code"]')
        self.hiring_date_input = page.locator('input[name="hiring_date"]')
        self.job_title_input = page.locator('input[name="job_title"]')
        self.add_button = page.locator("button:has-text('Add')")

    def navigate(self):
        self.page.goto("https://e.se1.hr.dmerej.info/add_employee")

    def fill(self):
        # Hardcoded employee data
        employee_name = "test employee"
        employee_email = "test@employee.fr"
        employee_address = "123 Test Street"
        employee_city = "Testville"
        employee_zip_code = "12345"
        employee_hiring_date = "2023-01-01"
        employee_job_title = "Software Engineer"
        # Fill in the Name field
        self.name_input.fill(employee_name)
        # Fill in the Email field
        self.email_input.fill(employee_email)
        # Fill in the Address field
        self.address_input.fill(employee_address)
        # Fill in the City field
        self.city_input.fill(employee_city)
        # Fill in the Zip Code field
        self.zip_code_input.fill(employee_zip_code)
        # Fill in the Hiring Date field
        self.hiring_date_input.fill(employee_hiring_date)
        # Fill in the Job Title field
        self.job_title_input.fill(employee_job_title)
        self.add_button.click()