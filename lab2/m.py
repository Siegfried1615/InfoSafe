# Author: Alex

# 加密算法
import math
import random

# 转为二进制
import string


def encode(s):
    return ''.join([bin(ord(c)).replace('0b', '') for c in s])


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


def read_str(msg):
    ascii_sum = 0
    # 计算 ascii 之和
    for char in msg:
        ascii_sum += ord(char)

    # ascii和 * 随机数
    random.seed(msg[0])
    value_1 = ascii_sum * random.random()
    random.seed(value_1)
    msg_list = list(msg)
    random.shuffle(msg_list)
    msg = "".join(msg_list)
    # 明文转为二进制
    b_msg = encode(msg)

    # 明文转为比特串
    by_msg = bytes(msg, encoding='utf-8')

    # 选明文首位字符作为ab

    a = ord(msg[0])
    b = ord(msg[-1])

    return a, b, value_1, msg


def random_all(a, b, y, msg):
    # 椭圆方程
    x = int(math.sqrt(abs((1 - (math.pow(y, 2) / pow(b, 2))) * pow(a, 2))) * 12)
    random.seed(x)

    msg_list = list(msg)
    random.shuffle(msg_list)
    ascii_sum = 0
    for i in range(0, int(len(msg_list) / 2)):
        ascii_sum += ord(msg_list[i])

    random.seed(ascii_sum)
    random.shuffle(msg_list)
    msg = "".join(msg_list)

    return msg


def operate(msg):
    # 补全128倍
    b_msg = encode(msg)
    rst_mod = len(b_msg) % 512
    value = 512 - rst_mod
    random.seed(ord(msg[0]))

    if value != 0:
        r_l = random_int_list(0, 1, value)
        for i in range(0, len(r_l)):
            b_msg += str(r_l[i])

    b_msg = str(b_msg)
    b_msg_l = list(b_msg)
    random.shuffle(b_msg_l)
    b_msg = "".join(b_msg_l)

    times = int(len(b_msg) / 512)

    # print(b_msg)
    # print(len(b_msg))

    step = 16 * times
    b_32 = [b_msg[i:i + step] for i in range(0, len(b_msg), step)]
    # print(len(b_32[0]), len(b_32))

    rst_list = []
    #         十六位数 转为4个四位二进制
    for j in range(0, 32):
        for k in range(0, 16, 16):
            rst_1 = int(b_32[j][k]) * pow(2, 3) + int(b_32[j][k + 1]) * pow(2, 2) + int(b_32[j][k + 2]) * pow(2, 1) + \
                    int(b_32[j][k + 3]) * pow(2, 0)
            rst_2 = int(b_32[j][k + 4]) * pow(2, 3) + int(b_32[j][k + 5]) * pow(2, 2) + int(b_32[j][k + 6]) * pow(2,
                                                                                                                  1) + \
                    int(b_32[j][k + 7]) * pow(2, 0)
            rst_3 = int(b_32[j][k + 8]) * pow(2, 3) + int(b_32[j][k + 9]) * pow(2, 2) + int(b_32[j][k + 10]) * pow(2,
                                                                                                                   1) + \
                    int(b_32[j][k + 11]) * pow(2, 0)
            rst_4 = int(b_32[j][k + 12]) * pow(2, 3) + int(b_32[j][k + 13]) * pow(2, 2) + int(b_32[j][k + 14]) * pow(2,
                                                                                                                     1) + \
                    int(b_32[j][k + 15]) * pow(2, 0)
            rst = rst_1 + rst_2 + rst_3 + rst_4
            rst_list.append(rst)
    # print(rst_list)
    return rst_list


def case_case(int_):
    str_ = ""
    if 0 <= int_ <= 9 or 17 <= int_ <= 40:
        str_ = chr(int_ + 48)
    elif 10 <= int_ <= 16:
        str_ = chr(int_ + 100)
    elif 41 <= int_ <= 47:
        str_ = chr(int_ + 56)
    elif 48 <= int_ <= 57 or 65 <= int_ <= 90 or 97 <= int_ <= 122:
        str_ = chr(int_)
    elif 123 <= int_ <= 181:
        str_ = chr(int_ - 58)
    elif 58 <= int_ <= 64:
        str_ = chr(int_ - 10)

    return str_


def judge(rst):
    final_list = []
    for i in range(0, 32):
        fin_str = case_case(rst[i])
        final_list.append(fin_str)

    return final_list


def hash_0_10(msg, i):
    random.seed(i)
    a = random.sample(string.ascii_letters + string.digits, 1)
    b = random.randint(0, len(msg))
    msg_l = list(msg)
    msg_l[b] = a
    msg = "".join(str(msg_l))
    return msg


def H(msg):
    text_rst = read_str(msg)
    msg_0 = random_all(text_rst[0], text_rst[1], text_rst[2], text_rst[3])
    rst = operate(msg_0)
    m = "".join(judge(rst))
    return m


if __name__ == '__main__':
    msg = input("请输入明文:")
    m1 = H(msg)
    print("h1:", m1)

    for i in range(2, 11):
        msg_0 = hash_0_10(msg, i)
        m1 = H(msg_0)
        print("h{}:".format(i), m1)
