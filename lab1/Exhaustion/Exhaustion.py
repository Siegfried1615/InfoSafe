"""
穷举法

26！ =  403291461126605635584000000
以现有的计算运算能力 10亿/秒
得 12683916年
"""

COUNT = 0


# 全排列
def perm(index, begin, end):
    global COUNT
    if begin >= end:
        # print(index)
        rst = "".join(index)
        print(rst)
        COUNT += 1
    else:
        i = begin
        for num in range(begin, end):
            index[num], index[i] = index[i], index[num]
            perm(index, begin + 1, end)
            index[num], index[i] = index[i], index[num]


# str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str = "ABC"
n = list(str)
perm(n, 0, len(n))
print("全排列结果共{}种".format(COUNT))

sub_letter = ""  # 全排列密钥
frequency_letter = ""  # 密文字母
c_file = open('c_text.txt')
c_text = c_file.read()
char_list = list(c_text)

# 替换
trans = str.maketrans(frequency_letter, sub_letter)
print(c_text.translate(trans))
