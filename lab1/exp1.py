def one_word(c_text):
    char_list = list(c_text)  # 转化为列表，每个字母为一个元素

    # 统计加密字符串中各个字母的出现次数
    #  Q X Z
    tempSet = set(char_list)  # 抓转为集合去重

    # 保存为字典，key:字母，value:出现次数
    tempDict = {}
    for i in tempSet:
        tempDict[i] = char_list.count(i)

    # 列表排序, 以元组形式
    dict_sorted = sorted(tempDict.items(), key=lambda x: x[1], reverse=True)
    # print(dict_sorted)
    frequency_list = []
    print("字母", "出现次数", "频率")
    for i in dict_sorted:
        print(i[0], "\t", i[1], "\t", i[1] / len(c_text))
        frequency_list.append(i[0])     # 按照出现频率写入到列表

    return frequency_list


def two_word(c_text):
    char_list = list(c_text)  # 转化为列表，每个字母为一个元素
    word_list2 = []
    temp_list = []

    try:
        for i in range(0, len(char_list)-1):
            temp_list.append(char_list[i])
            temp_list.append(char_list[i + 1])
            temp_str = "".join(temp_list)
            word_list2.append(temp_str)
            temp_list = []
    except StopIteration:
        print()

    # 统计加密字符串中各个二元字母的出现次数
    tempSet = set(word_list2)  # 抓转为集合去重

    # 保存为字典，key:字母，value:出现次数
    tempDict = {}
    for i in tempSet:
        tempDict[i] = word_list2.count(i)

    # 列表排序, 以元组形式
    dict_sorted = sorted(tempDict.items(), key=lambda x: x[1], reverse=True)
    # print(dict_sorted)

    frequency_list = []
    print("2元字母", "出现次数", "\t频率")
    for i in dict_sorted:
        print(i[0], "\t\t", i[1], "\t\t", i[1] / len(c_text))
        frequency_list.append(i[0])  # 按照出现频率写入到列表

    return frequency_list


def three_word(c_text):
    char_list = list(c_text)    # 转化为列表，每个字母为一个元素
    word_list3 = []
    temp_list = []

    try:
        for i in range(0, len(char_list)-2):
            temp_list.append(char_list[i])
            temp_list.append(char_list[i + 1])
            temp_list.append(char_list[i + 2])
            temp_str = "".join(temp_list)
            word_list3.append(temp_str)
            temp_list = []
    except StopIteration:
        print()

    # 统计加密字符串中各个二元字母的出现次数
    tempSet = set(word_list3)  # 抓转为集合去重

    # 保存为字典，key:字母，value:出现次数
    tempDict = {}
    for i in tempSet:
        tempDict[i] = word_list3.count(i)

    # 列表排序, 以元组形式
    dict_sorted = sorted(tempDict.items(), key=lambda x: x[1], reverse=True)
    # print(dict_sorted)

    frequency_list = []
    print("3元字母", "出现次数", "\t频率")
    for i in dict_sorted:
        print(i[0], "\t\t", i[1], "\t\t", i[1] / len(c_text))
        frequency_list.append(i[0])  # 按照出现频率写入到列表

    return frequency_list


if __name__ == '__main__':
    c_file = open('c_text.txt')  # 读取文件
    c_text = c_file.read()       # 读取文本

    one_word(c_text)
    two_word(c_text)
    three_word(c_text)