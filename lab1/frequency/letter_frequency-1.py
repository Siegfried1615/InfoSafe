# 统计频率

def getLetterList():
    c_file = open('c_text.txt')  # 读取文件
    c_text = c_file.read()  # 读取文本
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

getLetterList()