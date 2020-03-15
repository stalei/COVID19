import csv
import urllib.request
from datetime import timedelta, date
import matplotlib.pyplot as plt
import numpy as np
#import datetime
#https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports

csvURL='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'#03-12-2020.csv
country="US"


#response = urllib.request.urlopen(urlConfirmed)
#cr = csv.reader(response)

#for row in cr:
#    print(row)

#data = response.read()
#read = csv.DictReader(data)
#next(read)
#import pandas as pd
import io
#import requests

import pandas as pd
#read = pandas.io.parsers.read_csv(urlDeath, ...)
#s=requests.get(urlDeath).content
#c=pd.read_csv(io.StringIO(s.decode('utf-8')))

#print(read)

#csvfile = csv.reader(io.StringIO(data.decode('utf-8')), delimiter=',')
f_date = date(2020, 2, 5)
l_date = date.today()
delta = l_date - f_date
daycount=delta.days
totEachDay=[0]*daycount
fig1 = plt.figure(figsize=plt.figaspect(1./3.))
ax1 = fig1.add_subplot(231)
ax1.set_xlabel('days ago')
ax1.set_ylabel('N')
ax1.set_xlim(daycount, -7)

ax2 = fig1.add_subplot(232)
ax2.set_xlabel('days ago')
ax2.set_ylabel('N')
ax2.set_xlim(daycount, -7)

ax3 = fig1.add_subplot(233)
ax3.set_xlabel('days ago')
ax3.set_ylabel('N')
ax3.set_xlim(daycount, -7)

ax4 = fig1.add_subplot(234)
ax4.set_xlabel('days ago')
ax4.set_ylabel('Growth factor')
ax4.set_xlim(daycount, -7)



i=0
totConfirmed=[0]*daycount
totDeath=[0]*daycount
totRecovered=[0]*daycount
GrowthFactorAll=[0]*daycount
g1=[1]*daycount

totConfPrePreviousDay=0
totConfPreviousDay=0
GrowthFactor=0
totConf=0

daysaxis=range(daycount,0,-1)
for n in range(0,daycount):
    day=(f_date + timedelta(n)).strftime("%m-%d-%Y")
    #print(day)
    csvfile=csvURL+str(day)+'.csv'
    print(csvfile)
    response = urllib.request.urlopen(csvfile)
    data = response.read()
    csvdata = csv.reader(io.StringIO(data.decode('utf-8')), delimiter=',')
    next(csvdata)
    totConfPrePreviousDay=totConfPreviousDay
    totConfPreviousDay=totConf
    totConf=0;
    totRec=0;
    totD=0;
    for row in csvdata:
        if row[1]==country:
            totConf+=int(row[3])
            totD+=int(row[4])
            totRec+=int(row[5])
    print(totConf,totRec,totD)
    totConfirmed[i]=totConf
    totRecovered[i]=totRec
    totDeath[i]=totD
    #ax1.plot(i,np.log10(tot))#,'r',linestyle='-',label="b/a")

    if totConfPreviousDay - totConfPrePreviousDay !=0:
        GrowthFactor=(totConf-totConfPreviousDay)/(totConfPreviousDay-totConfPrePreviousDay)
    #print(GrowthFactor)
    GrowthFactorAll[i]=GrowthFactor
    i+=1
    #plt.show()
    #day2=day.strftime("%Y-%m-%d")
#ax1.plot(daysaxis,totConfirmed,'y',linestyle='-',label="Confirmed")
print(GrowthFactor)
ax1.plot(daysaxis,totConfirmed,'y+',label="Confirmed")
ax2.plot(daysaxis,totRecovered,'go',label="Recovered")
ax3.plot(daysaxis,totDeath,'rx',label="Death")
ax4.plot(daysaxis,GrowthFactorAll,'k',linestyle='-',label="Growth factor")
ax4.plot(daysaxis,g1,'b',linestyle=':',label="Inflection Point")
ax4.annotate('today:'+str(round(GrowthFactor,2)),xy=(daycount-5,GrowthFactor+1.5))
#for i,j in zip(daysaxis,GrowthFactorAll):
#    if j>0.9 and j<1.1:
#        ax4.annotate(str(round(j,2)),xy=(i+0.1,j+0.5))



ax1.legend(loc=2)
ax2.legend(loc=2)
ax3.legend(loc=2)
ax4.legend(loc=2)
plt.show()
#print(countries)
