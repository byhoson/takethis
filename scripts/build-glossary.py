import json
import os

PROJECT_HOME = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

INPUT_FILE = os.path.join(PROJECT_HOME, 'course/cse-courses-db.json')
OUTPUT_FILE = os.path.join(PROJECT_HOME, 'course/glossary.txt')

with open(INPUT_FILE) as json_file:
  items = json.load(json_file)

glossary = set()

for item in items:
    keywords_in_course = [row[0] for row in item['course_keywords']]
    glossary.update(keywords_in_course)

print(glossary)

with open(OUTPUT_FILE, 'w') as f:
    for keyword in glossary:
        f.write(keyword + '\n')
