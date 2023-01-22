from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import requests

home_url = "http://pythonchallenge.com"
challenge_url = "http://pythonchallenge.com/pc/def/"
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

def level_two_decode(code):

    alpha = "abcdefghijklmnopqrstuvwxyz"
    translate = "cdefghijklmnopqrstuvwxyzab"
    table = code.maketrans(alpha, translate)

    decoded = ""
    for char in code:
        new_char = char
        if ord(char) in table.keys():
            new_char = chr(table[ord(char)])
        
        decoded = f"{decoded}{new_char}"

    return decoded

def go_level_two(url):
    """Go to level 2 and work on solution."""
    print("Getting level 2")
    driver.get(url)

    r = requests.get(url)
    print(r.text)

    print("Solving level 2")
    actual_url = f"{home_url}/pc/def/map.html"


    code = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj." 
    decoded = level_two_decode(code)
    print(decoded)

    new_url_ext = level_two_decode("map")
    print(new_url_ext)

    level_three_url = f"{challenge_url}{new_url_ext}.html"
    
    wait_input = input(wait_prompt)

    return level_three_url

def go_level_three(url):
    print("Getting level 3")
    driver.get(url)

    wait_input = input(wait_prompt)

def run_main():
    solution = go_level_one()
    solution = go_level_two(solution)
    solution = go_level_three(solution)

if __name__  == "__main__":
    run_main()

