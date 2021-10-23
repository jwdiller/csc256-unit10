"""
James Diller
2021FA.CSC.256.0001
Unit 10- RESTful API and PyTest
2021/10/24
"""

import requests
import pytest

presidents = [
    "Washington",
    "Adams",
    "Jefferson",
    "Madison",
    "Monroe",
    "Jackson",
    "Buren",
    "Harrison",
    "Tyler",
    "Polk",
    "Taylor",
    "Fillmore",
    "Pierce",
    "Buchanan",
    "Lincoln",
    "Johnson",
    "Grant",
    "Hayes",
    "Garfield",
    "Arthur",
    "Cleveland",
    "McKinley",
    "Roosevelt",
    "Taft",
    "Wilson",
    "Harding",
    "Coolidge",
    "Hoover",
    "Truman",
    "Eisenhower",
    "Kennedy",
    "Johnson",
    "Nixon",
    "Ford",
    "Carter",
    "Reagan",
    "Bush",
    "Clinton",
    "Obama",
    "Trump",
    "Biden"
    ]

url = "https://api.duckduckgo.com/?q=\"presidents of the united states\"&format=json&t=JamesDillerCSC256testApp"
#This test uses DuckDuckGo
ducky = requests.get(url)
topicList = ducky.json()
topicList = topicList["RelatedTopics"]

def test_request_good():
    assert ducky.status_code == 200, "Request denied"

def test_all_presidents():
    allgood = True
    errorMsg = ""
    for smuck in presidents:
        minorgood = False
        for topic in topicList:
            if topic["FirstURL"].count(smuck) > 0:
                minorgood = True
                break
        if not minorgood:
            allgood = False
            errorMsg += smuck + " not found\n"
    assert allgood, errorMsg
