from selenium import webdriver
from selenium.webdriver.common.keys import Keys

home_url = "http://pythonchallenge.com"
level_one = "http://pythonchallenge.com/pc/def/0.html"

wait_prompt = "Enter when ready to move to next page..."

print("Getting first level.")
driver = webdriver.Firefox()
driver.get(level_one)

wait_input = input(wait_prompt)

print("Solving problem one...")
result = 2**38
level_two = f"{home_url}/pc/def/{result}.html"
wait_input = input(wait_prompt)

print("Getting level 2")
driver.get(level_two)

wait_input = input(wait_prompt)
