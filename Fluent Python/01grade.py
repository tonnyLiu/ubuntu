import bisect

def grade(score, grades='FDCBA'):
    breakpoints = [60, 70, 80 ,90]
    i = bisect.bisect(breakpoints, score)
    return grades[i]

if __name__ == '__main__':
    print([grade(score) for score in [33, 44, 65, 78, 98, 74]])