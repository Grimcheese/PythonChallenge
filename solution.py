from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import requests

home_url = "http://pythonchallenge.com"
level_one = "http://pythonchallenge.com/pc/def/0.html"

wait_prompt = "Enter when ready to move to next page..."

driver = webdriver.Firefox()

def go_level_one():
    """Go to the first level and get solution."""

    print("Getting first level.")

    driver.get(level_one)

    print("Solving problem one...")
    result = 2**38
    level_two = f"{home_url}/pc/def/{result}.html"

    wait_input = input(wait_prompt)
    return level_two

def go_level_two(url):
    """Go to level 2 and work on solution."""
    print("Getting level 2")
    driver.get(url)

    wait_input = input(wait_prompt)

def run_main():
    solution = go_level_one()
    solution = go_level_two(solution)

if __name__  == "__main__":
    run_main()
