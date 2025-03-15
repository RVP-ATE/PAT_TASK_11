# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


# Function to perform the drag and drop operation
def perform_drag_and_drop():
    #Initialize the WebDriver (using Chrome in this case)
    driver = webdriver.Chrome()

    #Open the URL
    driver.get("https://jqueryui.com/droppable/")

    #Maximize the browser window
    driver.maximize_window()

    #Wait for the page to load properly
    time.sleep(2)  # Giving time for the page to load completely

    #Switch to the iframe that contains the draggable elements
    driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="content"]/iframe'))

    #Step 5: Locate the white rectangular box (the draggable element)
    draggable = driver.find_element(By.XPATH, '//*[@id="draggable"]')

    #Locate the yellow rectangular box (the droppable target)
    droppable = driver.find_element(By.XPATH, '//*[@id="droppable"]')

    #Create an ActionChain to perform the drag and drop
    action = ActionChains(driver)

    #Perform drag and drop operation
    action.drag_and_drop(draggable, droppable).perform()

    #Optional: Wait to observe the action before closing the browser
    time.sleep(2)

    #Close the browser
    driver.quit()


#Main function to execute the script
if __name__ == "__main__":
    perform_drag_and_drop()