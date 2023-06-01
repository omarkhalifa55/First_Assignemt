#open_browser
import webdriver_manager
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#open_URl
driver.get("https://magento.softwaretestingboard.com/")
#type_in_filed
driver.find_element(By.ID, "search_mini_form").send_keys("Shirt")
#click_on_button