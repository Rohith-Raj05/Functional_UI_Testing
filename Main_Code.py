
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def login_to_dealsdray(driver, username, password):
    driver.get("https://demo.dealsdray.com/")
    driver.maximize_window()
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_field.send_keys(username)

    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_field.send_keys(password)

    try:
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        login_button.click()
    except TimeoutException:
        print("Login button not found or not clickable. Please check the login button element.")
        return

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    driver.save_screenshot("1_Screenshot_After_Login.png")
    print("Login successful.")


def navigate_to_orders(driver):
    try:
        main_menu_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "css-sukebr"))
        )
        main_menu_button.click()

        orders_menu_item = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Orders']/parent::button"))
        )
        orders_menu_item.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        print("Navigated to Orders page.")
    except TimeoutException:
        print("Navigation to Orders page timed out. Please check the menu items.")
    except NoSuchElementException:
        print("Navigation to Orders page failed. Menu items not found.")
    driver.save_screenshot("2_Screenshot_After_Orders_page.png")



def click_add_bulk_order(driver):
    try:
        add_bulk_order_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButtonBase-root.css-vwfva9"))
        )
        add_bulk_order_button.click()
        print("Clicked 'Add Bulk Order' button.")
    except TimeoutException:
        print("Add Bulk Order button not found or not clickable. Please check the button element.")
    except NoSuchElementException:
        print("Add Bulk Order button not found. Please check the button element.")
    driver.save_screenshot("3_Screenshot_After_Bulk_order_page.png")



def upload_file(driver, file_path):
    try:
        import_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "mui-7"))
        )
        import_button.send_keys(file_path)
        print("File uploaded.")
    except TimeoutException:
        print("Import button not found or not clickable. Please check the button element.")
    except NoSuchElementException:
        print("Import button not found. Please check the button element.")
    driver.save_screenshot("4_Screenshot_After_Upload_file_page.png")


    
def click_import_button(driver):
    try:
        import_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButtonBase-root.css-6aomwy"))
        )
        import_button.click()
        print("Clicked 'Import' button.")
    except TimeoutException:
        print("Import button not found or not clickable. Please check the button element.")
    except NoSuchElementException:
        print("Import button not found. Please check the button element.")
    driver.save_screenshot("5_Screenshot_After_Clicking_importbutton.png")



def click_validate_data_button(driver):
    try:
        validate_data_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButtonBase-root.css-6aomwy"))
        )
        validate_data_button.click()
        print("Clicked 'Validate Data' button.")

        # Handle the alert
        handle_alert(driver)

    except TimeoutException:
        print("Validate Data button not found or not clickable. Please check the button element.")
    except NoSuchElementException:
        print("Validate Data button not found. Please check the button element.")
    driver.save_screenshot("6_Screenshot_After_Clicking_ValidateButton.png")



def handle_alert(driver):
    try:
        # Wait for the alert to be present
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

        # Accept the alert (clicking OK)
        alert.accept()

        print("Alert accepted.")

    except NoAlertPresentException:
        print("No alert present.")



def take_screenshot(driver, file_path):
    driver.save_screenshot(file_path)
    print(f"Screenshot saved to {file_path}")

    

username = "prexo.mis@dealsdray.com"
password = "prexo.mis@dealsdray.com"
file_path = "D:\DealsDray_Assignment\Automation Test 02 - Functional Testing Case\demo-data.xlsx" 
screenshot_path = "Final_Output_Screenshot.png"

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

login_to_dealsdray(driver, username, password)
navigate_to_orders(driver)
click_add_bulk_order(driver)
upload_file(driver, file_path)
click_import_button(driver)
click_validate_data_button(driver)
take_screenshot(driver, screenshot_path)

driver.quit()

