from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup, Comment

import requests

import re

import urllib
from urllib import parse


home_url = "http://pythonchallenge.com"
challenge_url = "http://pythonchallenge.com/pc/def/"
levels = ["http://pythonchallenge.com/pc/def/0.html"]

wait_prompt = "Enter when ready to move to next page..."

driver = webdriver.Firefox()

def go_level_zero():
    """Go to the first level (0) and get solution."""

    print("Getting level zero.")
    driver.get(levels[0])

    print("Solving level zero...")
    result = 2**38
    next_level = f"{challenge_url}{result}.html"

    print("Level zero solution found!")
    input(wait_prompt)
    
    write_solutions(0, next_level)
    
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
    
    print("Getting level one.")
    driver.get(url)

    print("Solving level one...")

    code = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj." 
    decoded = level_one_decode(code)
    print(decoded)

    new_url_ext = level_one_decode("map")
    print(f"Url ext: {new_url_ext}")

    next_url = f"{challenge_url}{new_url_ext}.html"
    print("Level one solution found!")
    input(wait_prompt)

    write_solutions(1, next_url)
    
    return next_url

def go_level_two(url):
    """Go to level 2 and work on solution."""
    
    print("Getting level two")
    driver.get(url)

    print("Solving level two...")
    
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
    print("Level two solution found!")
    input(wait_prompt)
    
    write_solutions(2, next_url)
    return next_url

def go_level_three(url):
    """Go to level three and find the solution."""

    print("Getting level three")
    driver.get(url)

    print("Solving level three...")

    # Get string from web page

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    comment = soup.find_all(text=lambda text:isinstance(text, Comment))[0]
    # Solution alg -
    # Find three upper case characters one lower case and then three uppercase.

    pattern = re.compile("[a-z]+[A-Z]{3,3}([a-z]{1,1})[A-Z]{3,3}[a-z]+")
    result = pattern.findall(comment)

    answer = "".join(result)
    
    print("Level three solution found!")
    input(wait_prompt)

    next_url = f"{challenge_url}{answer}.php"
    write_solutions(3, next_url)
    
    return next_url


def get_next_nothing(in_url):
    """Get the next set of nothing numbers from a given url."""

    r = requests.get(in_url)

    url_parts = urllib.parse.urlparse(in_url)
    query = url_parts.query
    
    
def go_level_four(url):
    """Go to and solve fourth level."""

    print("Getting level four.")
    driver.get(url)
    
    print("Solving level four...")
    
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.prettify)
    links = soup.find_all('a', href=True)
    print(links[0]['href'])
    
    
    # Start nothing linked-list
    
    # get_next_nothing(next_nothing_url)

    input(wait_prompt)
    
def write_solutions(level, solution, fname="found_solutions.txt"):
    """Write a solution url to file so it can be accessed later.
    
    Args:
        level: An integer representing the level number to write to be written.
        solution: A string with the solution url.
    """
    
    level_string = f"Level {level}"
    
    # Check if level solution already exists
    exists = False
    try:
        with open(fname, 'r') as f:
            file_lines = f.readlines()
            for line in file_lines:
                first, second = line.split(":", 1)
                if first.strip() == level_string:
                    exists = True
    except FileNotFoundError:
        print("File does not exist.")
        
    if not exists:
        print(f"Writing level {level} solution to file...")
        with open(fname, 'a') as f:
            full_string = f"{level_string}:{solution}\n"
            f.write(full_string)
            
            print("Added level to file!")
        
def read_solutions(fname="found_solutions.txt"):
    """Read the file to find all stored solutions.
    
    Args: An optional argument specifying the file name to read.
    
    Returns: A dictionary containing levels and their urls
    """
    
    solutions = {}
    with open(fname, 'r') as f:
        for line in f:
            level, url = line.split(":", 1)
            discard, level = level.split() 
            solutions[level] = url.strip()
    
    print(solutions)
    return solutions


def choose_level(solutions):
    """Let the user choose one of the solutions that have already been found.
    
    Args:
        solutions: A dictionary containing the level and url of each previously
            found solution.
    Returns: The level that the user has chosen to start at.
    """
    
    if len(solutions) == 0:
        print("No solutions found starting at zero.")
        return 0
    
    # Find lowest level
    lowest = 0
    
    # Find highest level and display available levels to user
    print("Available levels: ")
    
    highest = 0
    for level in solutions.keys():
        print(f"Level {level} at {solutions[level]}")
        if int(level) > highest:
            highest = int(level)
    
    chosen_level = -1
    valid = False
    while not valid:
        try:
            chosen_level = int(input("Please enter a level number: "))
            if lowest <= chosen_level and chosen_level <= highest:
                valid = True
            else:
                print(f"Number must be between {lowest} and {highest}")
        except ValueError:
            print("Not a valid number.")

    print(f"Chose: {chosen_level}")
    return chosen_level


def run_main():
    solutions = read_solutions()
    
    level = choose_level(solutions)
    
    solution = go_level_zero()
    solution = go_level_one(solution)
    solution = go_level_two(solution)
    solution = go_level_three(solution)
    solution = go_level_four(solution)
    
    print("No more solutions.")

if __name__  == "__main__":
    run_main()

