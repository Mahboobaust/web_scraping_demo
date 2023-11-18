from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the web driver (you need to provide the path to your WebDriver executable)
driver = webdriver.Chrome()
driver.maximize_window()

# Open the URL
url = "https://www.rehab-bd.org/index.php?page=members&rowPerPage=16"
driver.get(url)

def get_links():
    # Find all anchor elements (links) on the page
    links = driver.find_elements(by=By.TAG_NAME,value='a')

    # Extract and print the URLs
    for link in links:
        href = link.get_attribute("href")
        if href:
            if href.__contains__('companyID'):
                print(href)


dropdown_element = driver.find_element(by=By.XPATH,value='//*[@id="table14"]/tbody/tr/td/select')

driver.execute_script("arguments[0].scrollIntoView();", dropdown_element)

for page_number in range(1, 52):
    choose_element = driver.find_element(by=By.XPATH,value=f'//*[@id="table14"]/tbody/tr/td/select/option[{page_number}]')
    choose_element.click()
    btn_element = driver.find_element(by=By.XPATH,value='//*[@id="table14"]/tbody/tr/td/input[1]')
    choose_element.click()
    get_links()

# Close the browser
driver.quit()
# # Find the elements containing the data you want to scrape
# table_element = driver.find_element(by=By.XPATH,value='//*[@id="table_in_file"]')
# if table_element.is_displayed():
#     membership_no_element = table_element.find_element(by=By.XPATH,value='//td[contains(text(), "Membership No")]/b/a')
#     company_name_element = table_element.find_element(by=By.XPATH,value='//td/b/a')
#     address_element = table_element.find_element(by=By.XPATH,value='//font[contains(text(), "Phone")]/preceding-sibling::font')
#     phone_element = table_element.find_element(by=By.XPATH,value='//font[contains(text(), "Phone:")]/preceding-sibling::font')
#     email_element = table_element.find_element(by=By.XPATH,value='//font[contains(text(), "E-mail:")]/preceding-sibling::font')
#     website_element = table_element.find_element(by=By.XPATH,value='//font[contains(text(), "Web:")]/preceding-sibling::font')
#
#     # Extract the text from the elements
#     membership_no = membership_no_element.text
#     company_name = company_name_element.text
#     address = address_element.text
#     phone = phone_element.text
#     email = email_element.text
#     website = website_element.get_attribute("href")
#
#     # Print the extracted data
#     print("Membership No:", membership_no)
#     print("Company Name:", company_name)
#     print("Address:", address)
#     print("Phone:", phone)
#     print("Email:", email)
#     print("Website:", website)
#
# # Close the browser
# driver.quit()
