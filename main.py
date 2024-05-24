# txtファイルから問ごとの区切ったリストを作成する

import os
import re
import sys

# ファイルの読み込み

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines

# 問いが始まり次の問いが始まるインデックスを取得しその間のテキストを取得
def get_questions(lines):
    questions = []
    for i in range(len(lines)):
        # 問いが始まるインデックスを取得
        if re.match(r'^問\d+', lines[i]):
            start_index = i
            # 次の問いが始まるインデックスを取得
            if i != len(lines) - 1:
                end_index = i + 1
                while not re.match(r'^問\d+', lines[end_index]):
                    if end_index == len(lines) - 1:
                        break
                    end_index += 1
                questions.append(lines[start_index:end_index])
            else:
                questions.append(lines[start_index:])
    # import pdb; pdb.set_trace()
    return questions

# 問題のリストを新しいファイルに書き込む

def write_question_list(file_path, question_list):
    new_file_path = file_path.replace('.txt', '_question.txt')
    with open(new_file_path, 'w', encoding='utf-8') as f:
        for i, question in enumerate(question_list):
            q = "".join(question)
            f.write(q)
            f.write('\n')
    print(f'{new_file_path}を作成しました')

def write_csv(file_path, question_list):
    new_file_path = file_path.replace('.txt', '_question.csv')
    with open(new_file_path, 'w', encoding='utf-8') as f:
        f.write('問題,\n')
        for i, question in enumerate(question_list):
            # 空白を削除
            qa = "".join(question).replace('\n', '').replace(",", "")
            #import pdb; pdb.set_trace()
            f.write(qa)
            f.write(',\n')
    print(f'{new_file_path}を作成しました')

# メイン関数

def main():
    args = sys.argv
    if len(args) != 2:
        print('引数にファイルパスを指定してください')
        sys.exit()
    file_path = args[1]
    if not os.path.exists(file_path):
        print('ファイルが存在しません')
        sys.exit()
    lines = read_file(file_path)
    question_list = get_questions(lines)
    # write_question_list(file_path, question_list)
    # csvファイルに書き込む
    write_csv(file_path, question_list)

if __name__ == '__main__':
    main()