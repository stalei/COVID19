#  © Shahram Talei @ 2020 The University of Alabama
#you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 3 of the License, or
#(at your option) any later version.
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
# This code is distributed as is and there is no warranty or technical support

import csv
import urllib.request
from datetime import timedelta, date
import matplotlib.pyplot as plt
import numpy as np
import io


USdailyTestURL='http://covidtracking.com/api/us/daily.csv' #ref: https://covidtracking.com/
csvURL='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'
countriesList=["US","Italy","Spain"]
#Numbers we may consider

HospitalBeds=924107 #https://www.washingtonpost.com/business/2020/03/14/hospital-doctors-patients-coronavirus/
Ventilators=160000 #http://www.centerforhealthsecurity.org/resources/COVID-19/200214-VentilatorAvailability-factsheet.pdf
#reference of these numbers:
#
plt.rcParams["font.size"] =13


#some of the early dates have different file structure and you may see an error
f_date = date(2020, 2, 25)
l_date = date.today()
delta = l_date - f_date
daycount=delta.days +1
totEachDay=[0]*daycount
fig1 = plt.figure(figsize=plt.figaspect(1./3.))
fig1.suptitle('COVID-19 - ' + ' ( date (0): '+str(l_date)+')')
ax1 = fig1.add_subplot(231)
#ax1.set_xlabel('days ago')
ax1.set_ylabel('Log(N)')
ax1.set_xlim(daycount-1, -3)
ax1.title.set_text('Confirmed')
ax1.grid(True)
ax2 = fig1.add_subplot(232)
#ax2.set_xlabel('days ago')
ax2.set_ylabel('Log(N)')
ax2.set_xlim(daycount-1, -3)
ax2.title.set_text('Recovered')
ax2.grid(True)
ax3 = fig1.add_subplot(233)
#ax3.set_xlabel('days ago')
ax3.set_ylabel('Log(N)')
ax3.set_xlim(daycount-1, -3)
ax3.title.set_text('Deaths')
ax3.grid(True)
ax4 = fig1.add_subplot(234)
ax4.set_xlabel('days ago')
ax4.set_ylabel('Growth factor')
ax4.set_xlim(daycount-2, -3)
ax4.set_ylim(-2, 10)
ax4.axhspan(1, 10, alpha=0.15, color='red')
ax4.axhspan(-2, 1, alpha=0.15, color='green')

ax4.grid(True)
ax5 = fig1.add_subplot(235)
ax5.set_xlabel('days ago')
ax5.set_ylabel('Recovery ratio')
ax5.set_xlim(daycount-1, -3)
ax5.grid(True)
ax6 = fig1.add_subplot(236)
ax6.set_xlabel('days ago')
ax6.set_ylabel('Death ratio')
ax6.set_xlim(daycount-1, -3)
ax6.grid(True)
#inverse axis for days ago on x
daysaxis=range(daycount-1,-1,-1)
daysaxis_1=range(daycount-2,-1,-1)
g1=[1]*daycount
#ax4.plot(daysaxis,g1,'b',linestyle=':',label="Inflection Point")
ax4.hlines(y=1,xmin=daycount, xmax=-3,color='k',linestyle='-.',label="Inflection Point")
for country in countriesList:
    i=0
    ####### These are lists of the values for all days
    totConfirmed=[0]*daycount
    totDeath=[0]*daycount
    totRecovered=[0]*daycount
    GrowthFactorAll=[0]*daycount
    ## temporary variables to keep the values for each days
    totConfPrePreviousDay=0
    totConfPreviousDay=0
    GrowthFactor=0
    totConf=0
    # the main loop on all files
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
            if row[1]==country: #because the data for US is also displayed for each states separately
                totConf+=int(row[3])
                totD+=int(row[4])
                totRec+=int(row[5])
        print(totConf,totRec,totD)
        totConfirmed[n]=totConf
        totRecovered[n]=totRec
        totDeath[n]=totD
        if totConfPreviousDay - totConfPrePreviousDay !=0:
            GrowthFactor=(totConf-totConfPreviousDay)/(totConfPreviousDay-totConfPrePreviousDay)
        #print(GrowthFactor)
        GrowthFactorAll[n]=GrowthFactor
        i+=1
    #print(GrowthFactor)
    GrowthFactorAll2=GrowthFactorAll[1:daycount+2]
    ax1.plot(daysaxis,np.log10(totConfirmed),'+',label=str(country))
    ax2.plot(daysaxis,np.log10(totRecovered),'o',label=str(country))
    ax3.plot(daysaxis,np.log10(totDeath),'x',label=str(country))
    ax4.plot(daysaxis_1,GrowthFactorAll2,linestyle='-',label=str(country)+'='+str(round(GrowthFactor,2)))
    #ax4.annotate('latest('+str(country)+'):'+str(round(GrowthFactor,2)),xy=(daycount-2,GrowthFactor-2.5))
    ax5.plot(daysaxis,np.divide(totRecovered,totConfirmed),linestyle='-',label=str(country))
    ax6.plot(daysaxis,np.divide(totDeath,totConfirmed),linestyle='-',label=str(country))

#for i,j in zip(daysaxis,GrowthFactorAll):
#    if j>0.9 and j<1.1:
#        ax4.annotate(str(round(j,2)),xy=(i+0.1,j+0.5))
ax1.legend(loc=4)
ax2.legend(loc=4)
ax3.legend(loc=4)
ax4.legend(loc=1)
ax5.legend(loc=1)
ax6.legend(loc=2)
plt.show()
#print(countries)
