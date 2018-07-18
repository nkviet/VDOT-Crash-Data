import pandas as pd
#import numpy as np
import os,sys

os.chdir('/Users/nkviet/Documents') # Windows path('C:\\VDOT\SA_Code')
sys.path.append('/Users/nkviet/Documents') # Windows path("C:\\VDOT\SA_Code")


df = pd.read_csv("data/rns_crash_tbl_crash_q3.csv")
df.head()

df1 = df[['CRASH_DT','GPS_LATITUDE_NBR','GPS_LONGITUDE_NBR',"CRASH_DSC"]]

df1.head()

df1['Activity']='Crash'

df1.head()

df1.columns = ['Date','Lat','Lon','Description','Activity']

df1.head()
#df = df1
df1.to_csv('data/CrashLatLong.csv', sep='\t')#, encoding='utf-8')
