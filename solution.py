from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup, Comment

import requests

home_url = "http://pythonchallenge.com"
challenge_url = "http://pythonchallenge.com/pc/def/"
level_one = "http://pythonchallenge.com/pc/def/0.html"

wait_prompt = "Enter when ready to move to next page..."

driver = webdriver.Firefox()

def go_level_zero():
    """Go to the first level (0) and get solution."""

    print("Getting level zero.")

    driver.get(level_one)

    print("Solving problem one...")
    result = 2**38
    next_level = f"{home_url}/pc/def/{result}.html"

    input(wait_prompt)
    return next_level

def level_one_decode(code):

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

def go_level_one(url):
    """Go to level 1 and work on solution."""
    print("Getting level 1")
    driver.get(url)

    r = requests.get(url)
    print(r.text)

    print("Solving level 1")
    actual_url = f"{home_url}/pc/def/map.html"


    code = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj." 
    decoded = level_one_decode(code)
    print(decoded)

    new_url_ext = level_one_decode("map")
    print(new_url_ext)

    next_url = f"{challenge_url}{new_url_ext}.html"
    
    input(wait_prompt)

    return next_url

def go_level_two(url):
    print("Getting level 2")
    driver.get(url)

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    comment = soup.find_all(text=lambda text:isinstance(text, Comment))

    # Count the number of times each character appears in a string
    in_string = comment[1]

    char_count = {}

    for character in in_string:
        if character in char_count.keys():
            char_count[character] += 1
        else:
            char_count[character] = 1
    
    print("Characters found:")
    for key in char_count.keys():
        print(f"{key} : {char_count[key]}")
    print("Solution: equality")
    next_url =  f"{challenge_url}equality.html"

    input(wait_prompt)

    return next_url

def go_level_three(url):
    """The third challenge to solve."""

    print("Getting level 3")
    driver.get(url)

    input(wait_prompt)

def run_main():
    solution = go_level_zero()
    solution = go_level_one(solution)
    solution = go_level_two(solution)
    solution = go_level_three(solution)

if __name__  == "__main__":
    run_main()

