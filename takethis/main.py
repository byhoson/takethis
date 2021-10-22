import kw_rank
import sig_rank

from operator import itemgetter

def main(career):
    # career_sig : dict = rank.build_career_sig(career)
    career_sig = kw_rank.get_rank(career)
    # print(career_sig)
    courses = sig_rank.get_rank(career_sig)
    # print(courses)
    top_courses = dict(sorted(courses.items(), key = itemgetter(1), reverse = True)[:5])
    print(top_courses)


if __name__ == '__main__':
    career = input('Input Caeer: ')
    main(career)
