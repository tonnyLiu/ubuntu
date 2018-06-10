#此程序是对bisect模块的应用，这是一个排序插入位置的模块
import bisect

def grade(score, grades='FDCBA'):
    '''
    :param score: 输入的分数
    :param grades: 划定的等级
    :return: 分数的等级
    '''
    breakpoints = [60, 70, 80 ,90]
    i = bisect.bisect(breakpoints, score)
    return grades[i]

if __name__ == '__main__':
    print([grade(score) for score in [33, 44, 65, 78, 98, 74]])