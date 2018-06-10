#insort(sep, item)把变量item插入序列sep中，并保持sep的升序顺序
import bisect
import random

SIZE = 7

#种子生成器，保证每次第一次产生的随机数相同
random.seed(1790)

my_list = []

for i in range(SIZE):
    new_item = random.randrange(start=8, stop=SIZE*3)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)