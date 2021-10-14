import kw_rank

def main(career):
    # career_sig : dict = rank.build_career_sig(career)
    career_sig = kw_rank.get_rank(career)
    print(career_sig)
    # courses : list = career_to_sig(career_sig)
    # print(courses)
    pass

if __name__ == '__main__':
    career = input('Input Caeer: ')
    main(career)
