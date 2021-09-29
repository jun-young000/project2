import pandas as pd
import numpy as np

df=pd.read_csv('Report.csv',encoding='utf-8')

df=df.drop(columns=['세대', '인구.1',"인구.2","인구.3","인구.4","인구.5","세대당인구","65세이상고령자"], axis=1)

df.columns=['년도','지역구','전체인구','등록_외국인','남자_외국인','여자_외국인']

df=df.drop(columns=['남자_외국인','여자_외국인'], axis=1)

df_index=df.drop([0,1])

df_end=df_index.set_index(["년도","지역구"],inplace=False)

df_end

df_end.to_csv('df_end.csv')











