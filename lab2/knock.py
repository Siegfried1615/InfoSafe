# Author: Alex
# 碰撞检测

from m import H
from itertools import combinations_with_replacement
from tqdm import tqdm
import logging


logging.basicConfig(level=logging.NOTSET)
# 碰撞检测
constant = "H"

# 计算32位哈希值的总可能性
num = 10 + 26 + 26
all = pow(26, 32)
print("本算法共有 %d 种哈希值组合\n" % all)

c1 = H(constant)
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*() <>=+-*/[]{}:",.-_'
list_all = list(alphabet)

test_str = ""
# 使用combinations_with_replacement迭代所有组合
g_num = 0
flag = 0
print("使用的字符集为\n{}".format(alphabet))
for k in range(1, all):
    print("\n正在进行 {} 个字符组合".format(k))
    for c in tqdm(combinations_with_replacement(list_all, k)):
        test_str = "".join(c)
        g_num += 1
        if g_num % 10000 == 0:
            logging.info("\n已计算{}次\n".format(g_num))
        if H(test_str) == c1 and test_str != "H":
            print("\n原字符串{}， 哈希值{}".format(constant, c1))
            print("发生碰撞的字符串{}".format(H(test_str)))
            print("计算了{}次".format(g_num))
            print("碰撞概率为{}".format(int(g_num/all)))
