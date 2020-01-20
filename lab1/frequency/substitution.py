# 替换字符
# https://blog.csdn.net/dellzhui/article/details/38542951


# 密文无QXZ
frequency_letter = "ABCDEFGHIJKLMNOPRSTUVWY"                                            # 被替换字母
sub_letter =       "tbidnfghcjklmesproauvwy"                                           # 常用字母频率

c_file = open('c_text.txt')
c_text = c_file.read()
trans = str.maketrans(frequency_letter, sub_letter)
print(c_text.translate(trans))