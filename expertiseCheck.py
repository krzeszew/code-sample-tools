import json
import sys

fileName = sys.argv[1]

with open(fileName) as file:
    data = json.load(file)

listOfExpertiseValues = ['Getting Started', 'Code Optimization', 'Concepts & Functionality', 'Tutorial', 'Reference Designs and End to End']

if data['expertise'] not in listOfExpertiseValues:
    print("sample.json has invalid expertise field")
    print("Supported expertise values: ", listOfExpertiseValues)
else:
    print("sample.json file has proper expertise value")
