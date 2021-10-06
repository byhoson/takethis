import os
import csv
import json

PROJECT_HOME = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
DATA = os.path.join(PROJECT_HOME, 'course/cse-courses.csv') 

print("parsing cse-courses.csv...")

results = []

with open(DATA) as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  for row in csv_reader:
    result = {}
    result['course_id'] = row[0]
    result['course_text'] = row[3]
    results.append(result)

with open(os.path.join(PROJECT_HOME, 'course/cse-courses.json'),'w') as json_file:
  json.dump(results, json_file)

print("Parsed cse-courses.csv. Result saved as cse-course.json")
