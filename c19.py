import csv
import urllib.request
from datetime import date
import matplotlib.pyplot as plt
import numpy as np
#import datetime
#https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports

urlConfirmed='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
urlRecovered='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv'
urlDeath='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv'
country="US"


response = urllib.request.urlopen(urlConfirmed)
#cr = csv.reader(response)

#for row in cr:
#    print(row)

data = response.read()
read = csv.DictReader(data)
#next(read)
#import pandas as pd
import io
#import requests

import pandas as pd
#read = pandas.io.parsers.read_csv(urlDeath, ...)
#s=requests.get(urlDeath).content
#c=pd.read_csv(io.StringIO(s.decode('utf-8')))

#print(read)

csvfile = csv.reader(io.StringIO(data.decode('utf-8')), delimiter=',')
next(csvfile)
f_date = date(2020, 1, 22)
l_date = date.today()
delta = l_date - f_date
daycount=delta.days
#print(csvfile[1,'Lat'])
fig1 = plt.figure(figsize=plt.figaspect(1))
ax1 = fig1.add_subplot(111)
ax1.set_xlabel('days')
ax1.set_ylabel('N')
#ax11.set_ylim(0,1.2)
i=5
tot=0
for row in csvfile:
    countries=row[1]
    if row[1]==country:
        #tot+=int(row[i])#
        all=np.array(row[4:i])
        A = all.astype(int)
        print(len(A))
        ax1.plot(i,A[i-4],'r',linestyle='-',label="b/a")#str(h.id))
        #ax1.plot(i,np.sum(A),'r',linestyle='-',label="b/a")#str(h.id))
        #ax11.plot(R,c_a,'b',linestyle='-',label="c/a")#str(h.id))
        i+=1
    #a = date(2011,11,24)
    #print()
#ax1.legend(loc=4)
plt.show()
print(countries)
