import pytest
from models.employee import AddEmployeePage
from models.team import CreateTeamPage

@pytest.fixture(scope="function")
def reset_db(page):
    page.goto("/reset_db")
    proceed_button = page.locator("button:has-text('proceed')")
    proceed_button.click()

def test_rm_team(reset_db,page):
    createTeam_page = CreateTeamPage(page)
    createTeam_page.navigate()
    createTeam_page.fill()

    addEmployee_page = AddEmployeePage(page)
    addEmployee_page.navigate()
    addEmployee_page.fill()

    employee_row = page.locator('table.table tbody tr', has_text="test employee")
    edit_button = employee_row.locator('a:has-text("Edit")')
    edit_button.click()

    team_adding_button = page.locator('a:has-text("Add to team")')
    team_adding_button.click()

    team_dropdown = page.locator('select[name="team"]')
    # Select the team by its visible text or value
    team_dropdown.select_option(label=team_name+ " team")    

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
    add_page = AddEmployeePage(page)
    add_page.navigate()
    add_page.fill()

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