from selenium import webdriver

driver=webdriver.Firefox(executable_path="C:\\Users\Giota\PycharmProjects\pythonProject1\pythonSelenium\geckodriver.exe")

driver.get(" https://www.workearly.gr")

driver.refresh()

links= driver.find_elements_by_tag_name('a')

print(len(links))


driver.close()

