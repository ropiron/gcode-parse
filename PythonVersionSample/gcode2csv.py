# csv to g-code text

import pandas as pd
import re

# csv の読み込み
df = pd.read_csv('.\\501.csv')
# セルに入力があるかどうかのマーカーを取得
dfnull = df.isnull()

# 初期化
lines = list();

# 行ごとに処理
for count in df.index.values:

  # 行の初期化
  line = ''

  # 行内の要素ごとに処理
  if dfnull.at[count, 'N'] == False:
    value = int(df.at[count, 'N'])
    line += 'N' + format(value, "04d") + '  '

  if dfnull.at[count, 'G'] == False:
    value = int(df.at[count, 'G'])
    line += 'G' + format(value, "02d") + ' '

  if dfnull.at[count, 'X'] == False:
    value = float(df.at[count, 'X'])
    line += 'X' + re.sub("0*$", "", format(value, ".6f")) + ' '

  if dfnull.at[count, 'Z'] == False:
    value = float(df.at[count, 'Z'])
    line += 'Z' + re.sub("0*$", "", format(value, ".6f")) + ' '

  if dfnull.at[count, 'R'] == False:
    value = float(df.at[count, 'R'])
    line += 'R' + re.sub("0*$", "", format(value, ".6f")) + ' '

  if dfnull.at[count, 'F'] == False:
    value = int(df.at[count, 'F'])
    line += 'F' + format(value, "d") + ' '

  if dfnull.at[count, 'OTHER'] == False:
    line += df.at[count, 'OTHER'] + ' '

  # 改行を追加し出力
  lines.append(line.strip() + '\n')

# 終端を出力
lines.append('%\n')

# 書き込み
f = open('.\\501_.txt', 'w')
f.writelines(lines)
f.close()
