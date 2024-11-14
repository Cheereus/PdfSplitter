import jieba
import pandas as pd
import os

# 自动统计指定目录下的文件个数
# 获取文本文件目录
input_dir = 'txts'
output_dir = 'outputs'

# 检查并创建输出目录
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 获取文件数量（只统计 .txt 文件）
txt_files = [file for file in os.listdir(input_dir) if file.endswith('.txt')]
file_num = len(txt_files)

# 空文件个数
empty_file_num = 0

# 对无甚意义的词进行过滤
banlist = ['图书馆', '图书馆员', 'www', 'com', 'html', 'Abstract', 'the', 'and', 'http']

print('总计' + str(file_num) + '个文件\n处理中...')
pd.set_option('max_rows', 5000)
seg_list = []

def segFilter(t):
    # 只对长度大于2的词进行统计
    # 对banlist中的词不作统计   
    # 对纯数字字符串(例如年份等)不作统计
    if len(t) >= 3 and t not in banlist and not t.isdigit():
        return True
    else: 
        return False

def pushSegs(file_path, output_path):
    global empty_file_num
    try:
        with open(file_path, 'r', encoding='UTF-8') as f:
            lines = f.readlines()
            if len(lines) == 0:
                print(f"{file_path} is empty")
                empty_file_num += 1
                return

            single_seg = []
            for line in lines:
                line_seg = jieba.cut_for_search(line)
                line_seg = list(filter(segFilter, line_seg))
                single_seg.extend(line_seg)
                seg_list.extend(line_seg)

            # 统计单个文件的词频
            single_result = pd.value_counts(single_seg)
            with open(output_path, mode='w', encoding='utf-8') as single_saveFile:
                single_saveFile.write(str(single_result))
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

# 处理所有文本文件
for txt_file in txt_files:
    file_path = os.path.join(input_dir, txt_file)
    output_path = os.path.join(output_dir, txt_file)
    pushSegs(file_path, output_path)

# 总体词频统计并保存
result = pd.value_counts(seg_list)
output_all_path = 'outputAll.txt'
try:
    with open(output_all_path, mode='w', encoding='utf-8') as saveFile:
        saveFile.write(str(result))
except Exception as e:
    print(f"Error saving overall result: {e}")

print(f'处理完毕\n总计处理{file_num}个文件\n其中{empty_file_num}个空文件')
