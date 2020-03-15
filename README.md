# COVID19
This is a simple code for online data scarping of the virus spread and growth factor. Nothing fancy<br/>
Data is read from:<br/>
https://github.com/CSSEGISandData/COVID-19 <br/>
Updated by Johns Hopkins university. You don't need to download or add any csv file. They are online. <br/>
For a nice and simple explanation of the growth see this video: <br/>
https://www.youtube.com/watch?v=Kas0tIxDvrg&feature=youtu.be
<br/>
<br/>
You can simply run: <br/>
<br/>
python c19.py<br/>
for a single country and:<br/>
<br/>
python c19_Multiple.py<br/>
<br/>
for multiple countries. Feel free to create your own country list <br/>
to see the result. <br/>
you can edit the country name but it is for the United States by default. <br/>
We plot total confirmed, recovered and death. There is also a plot for growth factor which is defined as: <br/>
   f=N_today/N_yesterday <br/>
where N is the total number of new cases (today is compared to yesterday).<br/>
<br/>
Thanks and let's flatten the curve!
