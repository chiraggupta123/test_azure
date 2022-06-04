# The sample test script in this section is compatible with JSON wire protocol-based 
# client bindings. Check out our W3C-based scripts in 
# the selenium-4 branch of the same repository.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
desired_cap = {
	'bstack:options' : {
		"os" : "OS X",
		"osVersion" : "Monterey",
		"projectName" : "tt",
		"buildName" : "tr",
		"local" : "false",
		"seleniumVersion" : "3.14.0",
	},
	"browserName" : "Chrome",
	"browserVersion" : "latest",
}

driver = webdriver.Remote(
    command_executor='https://chiraggupta_1Swh8i:TFyzx8ev4ztpJ6Lh4ckx@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap)
try:
    driver.get("https://bstackdemo.com/")
    WebDriverWait(driver, 10).until(EC.title_contains("StackDemo"))
    # Get text of an product - iPhone 12
    item_on_page =  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="1"]/p'))).text
    # Click the 'Add to cart' button if it is visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="1"]/div[4]'))).click()
    # Check if the Cart pane is visible
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME, "float-cart__content")))
    ## Get text of product in cart
    item_in_cart = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]'))).text
    # Verify whether the product (iPhone 12) is added to cart
    if item_on_page == item_in_cart:
        # Set the status of test as 'passed' or 'failed' based on the condition; if item is added to cart
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "iPhone 12 has been successfully added to the cart!"}}')
except NoSuchElementException:
    driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some elements failed to load"}}')
# Stop the driver
driver.quit() 