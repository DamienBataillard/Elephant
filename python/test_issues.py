import pytest
from models.employee import AddEmployeePage

@pytest.fixture(scope="function")
def reset_db(page):
    page.goto("/reset_db")
    proceed_button = page.locator("button:has-text('proceed')")
    proceed_button.click()

def test_rm_team(reset_db,page):
    # Create a team 
    page.goto("/")
    page.goto("/add_team")
    name_input = page.locator('input[name="name"]')
    team_name = "my team"
    name_input.fill(team_name)
    page.click("text='Add'")

    add_page = AddEmployeePage(page)
    add_page.navigate()
    add_page.fill()

    add_button = page.locator("button:has-text('Add')")
    add_button.click()

    employee_row = page.locator('table.table tbody tr', has_text="test employee")
    edit_button = employee_row.locator('a:has-text("Edit")')
    edit_button.click()

    team_adding_button = page.locator('a:has-text("Add to team")')
    team_adding_button.click()

    team_dropdown = page.locator('select[name="team"]')
    # Select the team by its visible text or value
    team_dropdown.select_option(label=team_name+ " team")    
    add_button.click()

    # Goto the team list
    page.goto("/teams")

    # Delete team with employee
    team_row = page.locator('table.table tbody tr', has_text=team_name)

    # Locate the "Delete" link within that row
    delete_button = team_row.locator('a.btn.btn-danger')

    # Click the "Delete" button
    delete_button.click()

    proceed_button = page.locator("button:has-text('proceed')")
    proceed_button.click()

    # Goto the team list
    page.goto("/employees")

    # Check if member is still there after deleting the team
    assert page.is_visible(f"td:has-text('{employee_name}')"), f"Error: Employee with name '{employee_name}' is not visible on the page it has been delete when team was deleted"

def test_update_hiring_date(reset_db,page):
    # Create an employee
    page.goto("/")
    page.goto("/add_employee")

    # Fill in the Name field
    name_input = page.locator('input[name="name"]')
    employee_name = "test employee"
    name_input.fill(employee_name)

    # Fill in the Email field
    email_input = page.locator('input[name="email"]')
    employee_email = "test@employee.fr"
    email_input.fill(employee_email)

    # Fill in the Address field
    address_input = page.locator('#id_address_line1')
    employee_address = "123 Test Street"
    address_input.fill(employee_address)

    # Fill in the City field
    city_input = page.locator('input[name="city"]')
    employee_city = "Testville"
    city_input.fill(employee_city)

    # Fill in the Zip Code field
    zip_code_input = page.locator('input[name="zip_code"]')
    employee_zip_code = "12345"
    zip_code_input.fill(employee_zip_code)

    # Fill in the Hiring Date field
    hiring_date_input = page.locator('input[name="hiring_date"]')
    employee_hiring_date = "2023-01-01"  # Format may vary (e.g., YYYY-MM-DD)
    hiring_date_input.fill(employee_hiring_date)

    # Fill in the Job Title field
    job_title_input = page.locator('input[name="job_title"]')
    employee_job_title = "Software Engineer"
    job_title_input.fill(employee_job_title)

    add_button = page.locator("button:has-text('Add')")
    add_button.click()

    employee_row = page.locator('table.table tbody tr', has_text="test employee")
    edit_button = employee_row.locator('a:has-text("Edit")')
    edit_button.click()

    contract_update_button = page.locator('a:has-text("Update contract")')
    contract_update_button.click()

    hiring_date_input = page.locator('input[name="hiring_date"]')
    new_hiring_date = "2025-01-30"

    readonly = hiring_date_input.get_attribute("readonly")
    assert readonly is None, "Error: The Hiring Date field is read-only."

