import jieba
import pandas as pd
import os

# 文件个数 TODO 应该是要自动统计指定目录下的文件个数的，但尝试失败
file_num = 2

# 空文件个数
empty_file_num = 0

# 对无甚意义的词进行过滤
banlist = ['图书馆', '图书馆员', 'www','com', 'html', 'Abstract', 'the', 'and', 'http']

print('总计' + str(file_num) + '个文件\n处理中...')
pd.set_option('max_rows',5000)
seg_list = []

def segFilter(t):   
# 只对长度大于2的词进行统计
# 对banlist中的词不作统计   
# 对纯数字字符串(例如年份等)不作统计
    if len(t) >= 3 and t not in banlist and not t.isdigit():
        return True
    else: 
        return False

def pushSegs(n):
    global empty_file_num
    f = open('txts/' + str(n) + '.txt', 'r', encoding='UTF-8')
    lines = f.readlines()
    if len(lines) <= 0:
        print(str(n) + '.txt is empty')
        empty_file_num = empty_file_num + 1

    single_seg = []
    for line in lines:
        line_seg = jieba.cut_for_search(line)
        line_seg = list(filter(segFilter, line_seg))
        single_seg.extend(line_seg)
        seg_list.extend(line_seg)
    f.close()
    single_result = pd.value_counts(single_seg)
    single_saveFile = open('outputs/' + str(n) + '.txt', mode='w', encoding='utf-8')
    single_saveFile.write(str(single_result))
    single_saveFile.close()

for n in range(file_num):
    pushSegs(n + 1) 

result = pd.value_counts(seg_list)
saveFile = open('outputAll.txt', mode='w', encoding='utf-8')
saveFile.write(str(result))
saveFile.close()

print('处理完毕\n总计处理' + str(file_num) + '个文件\n其中' + str(empty_file_num) + '个空文件')