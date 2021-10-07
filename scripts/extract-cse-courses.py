import json
import os
from keybert import KeyBERT

PROJECT_HOME = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
DATA = os.path.join(PROJECT_HOME, 'course/cse-courses.json')

kw_model = KeyBERT()

with open(DATA) as json_file:
  items = json.load(json_file)

for item in items:
  item['course_keywords'] = kw_model.extract_keywords(item['course_text'])
  print(item['course_id'], ':', item['course_keywords'])
  item.pop('course_text', None)

with open(os.path.join(PROJECT_HOME, 'course/cse-courses-db.json'), 'w') as json_file:
  json.dump(items, json_file)
  
