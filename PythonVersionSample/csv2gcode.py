# g-code text to csv

import pandas as pd
import re

# データフレームの作成とカラムの作成
df = pd.DataFrame()

# カラムの作成
# (この書き方はインチキくさいので、正しい方法が知りたい)
df['N'] = ''
df['G'] = ''
df['X'] = ''
df['Z'] = ''
df['R'] = ''
df['F'] = ''
df['OTHER'] = ''

# G-Code ファイルの読み込み
f = open('..\\501.txt', 'r')
lines = f.readlines()
f.close()

# 初期化
count = 0

# 行ごとに処理
for line in lines:

  # 改行文字削除
  line = line.replace("\n", "")

  # 終端検出
  if line == '%':
    break

  # 行の初期化
  count += 1
  df.loc[count] = ''

  # 要素の取り出し
  elements = line.split()

  # 行内の要素ごとに処理
  for element in elements:

    # 先頭の英字部分を key. その後を value とする
    match = re.match('(^[A-Za-z]+)(.*$)', element)
    key = match.group(1)
    value = match.group(2)

    if key == 'N': 
      df.at[count, key] = int(value)

    elif key == 'G':
      df.at[count, key] = int(value)

    elif key == 'X':
      df.at[count, key] = float(value)

    elif key == 'Z':
      df.at[count, key] = float(value)

    elif key == 'R':
      df.at[count, key] = float(value)

    elif key == 'F': 
      df.at[count, key] = int(value)

    else:
      # 不明な要素は key value 分割前の element を連結して出力
      df.at[count, 'OTHER'] = " ".join([df.at[count, 'OTHER'], element])

# CSV ファイルを出力
df.to_csv('.\\501.csv', index=False)
