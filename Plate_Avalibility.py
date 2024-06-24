import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def main(url, symbols):
    global driver
    driver.get(url)
    while True:
        try:
                Plate_Input = input('What Custom Plate Would You Like To Test?: ').strip().upper()

                if validate_plate(Plate_Input, symbols) == 1:
                    test_plate(Plate_Input)
                    if find_if_valid() == 1:
                        print(f"Your Custom Plate ({Plate_Input}) Is Valid!")
                    else:
                        print(f"Your Custom Plate ({Plate_Input}) Is Not Valid!")
                else:
                    print("Please Enter A Valid Custom Plate (Between 2-6 Characters with no spaces and special chars)")
                    print()

                driver.find_element(By.CLASS_NAME, 'button__text quick-combo__reset-text').click()
        except:
            print(f"Please Enter A Valid Custom Number Plate: ")

def find_if_valid():
    global driver
    driver.find_element(By.CLASS_NAME, 'button__text').click()
    time.sleep(1.25)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    title_element = soup.find('h2', class_='quick-combo__title quick-combo__title--available')
    if title_element and title_element.text.strip() == "Your combo is available!":
        return 1
    return 0

def test_plate(Plate_Input):
    global driver
    input_chars = driver.find_element(By.ID, 'quick-combo__combo')
    input_chars.clear()
    input_chars.send_keys(Plate_Input)

def validate_plate(Plate_Input, symbols):
    global driver
    if len(Plate_Input) >= 2 and len(Plate_Input) <= 6 and all(char not in symbols for char in Plate_Input):
        return 1
    return 0

    
if __name__ == '__main__':
    symbols = ['`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', '\\', '|', ';', ':', "'", '"', ',', '<', '.', '>',, '/', '?']
    url = 'https://vplates.com.au/'
    driver = selenium.webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.set_window_position(-2000, 0)#move the window off screen, as i tried to use headless but for some reason it wouldn't work whilst using headless... rip, couldn never find the element
    main(url, symbols)


