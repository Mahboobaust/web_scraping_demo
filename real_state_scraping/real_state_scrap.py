import config
import csv
import json
from selenium import webdriver
from selenium.webdriver.common.by import By


real_state_company_infos =[]


print(len(config.real_state_links))



# Set up the web driver (you need to provide the path to your WebDriver executable)
driver = webdriver.Chrome()
driver.maximize_window()

for link in config.real_state_links:
    driver.get(link)
    name_element= driver.find_element(by=By.XPATH,value='//*[@id="table_in_file"]/tbody/tr[1]/td/span')
    print(name_element.text)
    address_element = driver.find_element(by=By.XPATH, value='//*[@id="table_in_file"]/tbody/tr[11]/td[3]')
    print(address_element.text)
    phone_element = driver.find_element(by=By.XPATH, value='//*[@id="table_in_file"]/tbody/tr[12]/td[3]')
    print(phone_element.text)
    email_element = driver.find_element(by=By.XPATH, value='//*[@id="table_in_file"]/tbody/tr[15]/td[3]')
    print(email_element.text)
    print('___________________________________________________________________________')
    real_state_company_info = {
        "name":name_element.text,
        "address":address_element.text,
        "phone":phone_element.text,
        "email":email_element.text
    }
    real_state_company_infos.append(real_state_company_info)

print(real_state_company_infos)
file_name = "data.json"

# Open the file for writing
with open(file_name, "w") as json_file:
    # Write the JSON data to the file
    json.dump(real_state_company_infos, json_file)

#print(f"JSON data has been written to {file_name}")
csv_file_name = "data.csv"
with open('data.json', 'r') as json_file:
    # Load the JSON data from the file
    json_data = json.load(json_file)
with open(csv_file_name, 'w', newline='') as csvfile:
    # Create a CSV writer
    csvwriter = csv.writer(csvfile)

    # Write the header row based on the JSON keys
    header = json_data[0].keys()
    csvwriter.writerow(header)

    # Write the JSON data to the CSV file
    for row in json_data:
        csvwriter.writerow(row.values())


