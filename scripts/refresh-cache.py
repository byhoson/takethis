import os
import json
from apiclient.discovery import build

# API_KEY="AIzaSyCZUjk1AQaJE77rbhPntW9ILbVOMy9jvvI"

careers = ['backend developer', 'graphics engineer']

PROJECT_HOME = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

GLOSSARY_PATH = os.path.join(PROJECT_HOME, 'course/glossary.txt')
CACHE_GLOSSARY_PATH = os.path.join(PROJECT_HOME, '.cache/cache_glossary.json')
API_KEY_PATH = os.path.join(PROJECT_HOME, 'API_KEYS.txt')
API_KEY = ""
CX = ""

def google_query(query_string):
    # TODO call API
    # ret: total number of results
    global API_KEY
    global CX
    print(API_KEY)
    print(CX)
    resource = build("customsearch", 'v1', developerKey=API_KEY).cse()
    result = resource.list(q=query_string, cx=CX).execute()

    if result == None:
        print('*** API CALL ERROR ***')
        exit(-1)

    return int(result['searchInformation']['totalResults'])


def main():
    global API_KEY
    global CX

    # open api keys and cx
    try:
        with open(API_KEY_PATH, 'r') as txt_file:
            API_KEY = txt_file.readline().rstrip('\n')
            CX = txt_file.readline().rstrip('\n')
    except:
        print('[refresh_cache]: failed to get api keys')
        exit(1)

    keywords = []
    cache_glossary = dict()

    # open keywords = read glossary
    try:
        with open(GLOSSARY_PATH) as txt_file:
            keywords = txt_file.read().splitlines()
    except:
        print('[refresh_cache]: failed to open glossary')
        exit(1)

    for keyword in keywords:
        cache_glossary[keyword] = google_query(keyword)

    # refresh .cache/cache_glossary.json
    with open(CACHE_GLOSSARY_PATH, 'w') as json_file:
        json.dump(cache_glossary, json_file)
        print('[refresh_cache]: cache_glossary success')


    # refresh each .cache/cache_[carrer].json
    for career in careers:
        cache_career = dict()
        for keyword in keywords:
            cache_career[keyword] = google_query(keyword + ' AND ' + career)

        career_filename = career.replace(' ', '_')
        with open(os.path.join(PROJECT_HOME, '.cache/' + career_filename + '.json'), 'w') as json_file:
            json.dump(cache_career, json_file)
            print('[refresh_cache]: cache_' + career_filename  +  ' success')


if __name__ == '__main__':
    main()
