import os
import math

PROJECT_HOME = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
COURSE_DB = os.path.join(PROJECT_HOME, 'course/cse-courses-db.json') 

def get_course_norm(course):
    course_keywords = course['course_keywords'] # list if pairs
    norm = 0.0
    for kw in course_keywords:
        norm += kw[1] ** 2
    norm = math.sqrt(norm)
    return norm

def get_career_norm(career):
    norm = 0.0
    for kw, score in career.items():
        norm += score ** 2
    norm = math.sqrt(norm)
    return norm

def cosine_sim(course, career):
    course_id = course['course_id']
    course_keywords = course['course_keywords'] # list if pairs
    inner_prod = 0.0
    for kw in course_keywords:
        ineer_prod += kw[1] * career[kw[0]]
    course_norm = get_course_norm(course)
    career_norm = get_career_norm(career)
    sim = inner_prod / (course_norm * career_norm)
    return sim


def sig_sim(course, career, measure=0):
    if measure == 0:
        cosine_sim(course, career)
    elif measure == 1:
        return 0.5
    else:
        return 0.5

def get_rank(career):
    rank = {}
    with open(COURSE_DB) as json_file:
        courses = json.load(json_file)
    for course in courses:
        s = sig_sim(course, career)
        rank[course['course_id']] = s
        
