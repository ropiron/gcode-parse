import pandas as pd
import glob


df0 = pd.read_csv('510test.csv', encoding = "shift-jis", header=0, engine='python')



# for x in glob.glob('510test.csv'):    
#     df0 = pd.read_csv(x, encoding = "shift-jis", header=0, engine='python')
#     d = df0['(1)CAN-CH04'].diff()
#     startpoint = d[d>4]
     
#     for i in startpoint.index:
#         avg = pd.DataFrame(df0[i+59:i+210].mean())
#         std = pd.DataFrame(df0[i+59:i+210].std())
#         df_mn = pd.concat([df_mn,avg], axis=1)
#         df_std = pd.concat([df_std,std], axis=1)


# df_mn.T.to_csv('mean.csv', mode='a',header=False)
# df_std.T.to_csv('std.csv', mode='a',header=False)
