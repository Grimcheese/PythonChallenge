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

    r = requests.get(url)
    print(r.text)

    actual_url = f"{home_url}/pc/def/map.html"

    code = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj." 

    code = code.upper()
    for i in range(65, 90):
        old_character = chr(i)
        new_character = chr(i + 2)
        code = code.replace(old_character, new_character)

    code = code.lower()
    print(code)

    wait_input = input(wait_prompt)

def run_main():
    solution = go_level_one()
    solution = go_level_two(solution)

if __name__  == "__main__":
    run_main()
