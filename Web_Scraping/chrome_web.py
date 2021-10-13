from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://chromedriver.storage.googleapis.com/index.html?path=94.0.4606.61/")
