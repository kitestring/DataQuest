import pandas as pd
import numpy as np

nba = pd.read_csv("nba_2013.csv")
print(nba.head(3))

print(nba.info())

#          player pos  age bref_team_id   g  gs    mp   fg  fga    fg.  \
# 0    Quincy Acy  SF   23          TOT  63   0   847   66  141  0.468   
# 1  Steven Adams   C   20          OKC  81  20  1197   93  185  0.503   
# 2   Jeff Adrien  PF   27          TOT  53  12   961  143  275  0.520   
 
#       ...      drb  trb  ast  stl  blk  tov   pf  pts     season  season_end  
# 0     ...      144  216   28   23   26   30  122  171  2013-2014        2013  
# 1     ...      190  332   43   40   57   71  203  265  2013-2014        2013  
# 2     ...      204  306   38   24   36   39  108  362  2013-2014        2013  
 
# [3 rows x 31 columns]
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 481 entries, 0 to 480
# Data columns (total 31 columns):
# player          481 non-null object
# pos             481 non-null object
# age             481 non-null int64
# bref_team_id    481 non-null object
# g               481 non-null int64
# gs              481 non-null int64
# mp              481 non-null int64
# fg              481 non-null int64
# fga             481 non-null int64
# fg.             479 non-null float64
# x3p             481 non-null int64
# x3pa            481 non-null int64
# x3p.            414 non-null float64
# x2p             481 non-null int64
# x2pa            481 non-null int64
# x2p.            478 non-null float64
# efg.            479 non-null float64
# ft              481 non-null int64
# fta             481 non-null int64
# ft.             461 non-null float64
# orb             481 non-null int64
# drb             481 non-null int64
# trb             481 non-null int64
# ast             481 non-null int64
# stl             481 non-null int64
# blk             481 non-null int64
# tov             481 non-null int64
# pf              481 non-null int64
# pts             481 non-null int64
# season          481 non-null object
# season_end      481 non-null int64
# dtypes: float64(5), int64(22), object(4)
# memory usage: 116.6+ KB
# None

