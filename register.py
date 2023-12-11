import random, string, sys, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def haha(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_email(email):
    username, domain = email.split('@')
    return f"{username}+{haha(6)}@{domain}"

class Browser():
    def __init__(self, headless=True):
        chrome_options = Options()
        if headless:
            chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(options=chrome_options)
        self.vars = {}

    def scratch(self):
        username = haha(10)
        password = haha(10)

        self.driver.get("https://scratch.mit.edu/join")
        self.driver.set_window_size(1285, 765)
        
        self.wait_and_click(By.ID, "username")
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.wait_and_click(By.ID, "password")
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.wait_and_click(By.ID, "passwordConfirm")
        self.driver.find_element(By.ID, "passwordConfirm").send_keys(password)
        self.wait_and_click(By.CSS_SELECTOR, ".modal-flush-bottom-button")
        self.wait_and_click(By.ID, "country")
        self.driver.find_element(By.ID, "country").click()
        dropdown = self.driver.find_element(By.ID, "country")
        dropdown.find_element(By.XPATH, "//option[. = 'United States of America']").click()
        self.wait_and_click(By.CSS_SELECTOR, ".next-step-title")
        self.wait_and_click(By.ID, "birth_month")
        dropdown = self.driver.find_element(By.ID, "birth_month")
        dropdown.find_element(By.XPATH, "//option[. = 'June']").click()
        self.wait_and_click(By.ID, "birth_year")
        dropdown = self.driver.find_element(By.ID, "birth_year")
        dropdown = self.driver.find_element(By.ID, "birth_year")
        dropdown.find_element(By.XPATH, "//option[. = '2000']").click()
        self.wait_and_click(By.CSS_SELECTOR, ".modal-flush-bottom-button")
        self.wait_and_click(By.CSS_SELECTOR, ".col-sm-9:nth-child(4)")
        self.wait_and_click(By.CSS_SELECTOR, ".modal-flush-bottom-button")
        element = self.driver.find_element(By.CSS_SELECTOR, ".modal-flush-bottom-button")
        actions = ActionChains(self.driver)
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        self.driver.find_element(By.ID, "email").send_keys(generate_email(shit))
        self.wait_and_click(By.CSS_SELECTOR, ".next-step-title")
        time.sleep(7)
        print(f"Account {username} created.")
        with open('accounts.txt', 'a') as file:
            file.write(f"{username} / {password}\n")
            file.close()

    def wait_and_click(self, by, value):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((by, value))
        ).click()

    def wait_and_send_keys(self, by, value, keys):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by, value))
        ).send_keys(keys)

shit = input("Gmail Address: ")
dang = Browser(headless=False)
dang.scratch()
sys.exit()
