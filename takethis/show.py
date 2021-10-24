import json
import csv
import os

PROJECT_HOME = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
CSV_PATH = os.path.join(PROJECT_HOME, 'course/cse-courses.csv')


def show_result(career, courses):
    course_map = dict()
    try:
        with open(CSV_PATH, 'r', encoding='utf-8-sig') as csv_file:
            reader = csv.reader(csv_file)
            course_map = {rows[0]:rows[1] for rows in reader}
    except:
        print('[show]: missing career csv file')
        exit(1)

    result = dict()
    for code in courses:
        result[code] = [course_map[code], courses[code]]
    print('\n' + '='*100)
    print('Top 5 relevant courses you should take for ' + career + ':' + '\n' + '='*100)
    print(f"{'COURSE_ID' : <14}{'COURSE_NAME' : ^60}{'SCORE' : >10}")
    for course_id in result:
        print(f"{course_id : <14}{result[course_id][0] : <60}{result[course_id][1] : >10.4f}")

    print()
