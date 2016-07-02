# coding=utf-8

#Copyright (C) 2016 Viktor Horsmanheimo <vhh790@gmail.com>

#This program is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 2 of the License, or (at 
#your option) any later version.

#This program is distributed in the hope that it will be useful, but
#WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#General Public License for more details.


import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as mdates
import datetime
from yahoo_finance import Currency

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
currencies = Currency('usdeur')
spot = 1

xar=[]
yar=[]
ymin = float(currencies.get_rate())-0.0005
ymax = ymin + 0.0010

def animate(i):
    global xar, yar, ymin, ymax

    #gets the course
    currencies.refresh()
    y = currencies.get_rate()
    x = datetime.datetime.now()

    #makes the y axis larger if needed
    if float(y) > ymax:
        ymax = float(y)+0.0005
    if float(y) < ymin:
        ymin = float(y) - 0.0005

    print str(x) +": " + str(y)

    xar.append(x)
    yar.append(float(y))

    if len(xar) > 240:
        del xar[0]
        del yar[0]

    ax1.clear()
    ax1.yaxis.grid(True)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H.%M.%S'))
    ax1.plot(xar,yar)
    plt.autoscale('both')
    plt.gcf().autofmt_xdate()
    ax1.set_ylim([ymin,ymax])
    plt.title("Course right now: "+str(y))


ani = animation.FuncAnimation(fig,animate, interval=2000)
plt.show()
