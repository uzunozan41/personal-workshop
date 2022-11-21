import geopandas as gpd
import pandas as pd
import math

import matplotlib.pyplot as plt
from matplotlib.widgets import Button

class show:
    indx=0
    last_click=""

    def show_right(self,event):
        ax.cla()
              

        if self.last_click=="l":
            self.indx=self.indx+1
            self.indx=self.indx%len(name_list)

        df.boundary.plot(ax=ax,color="black")
        name=name_list[self.indx]

        district=df[df["name"]==name]
        district.plot(ax=ax,color="lightskyblue")
           
        population=district["population"].values[0]

        self.indx=self.indx+1
        self.indx=self.indx%len(name_list)
        
        ax.grid()
        ax.set_title(name,fontsize=24)        
        ax.set_xlabel("Population: {}".format(population))
        ax.set_title(title2, loc='left', y=0.02, x=0.73, fontsize='small',color="royalblue")

        self.last_click="r"

        ax.set_xticklabels(xlabels)
        ax.set_yticklabels(ylabels)

    def show_left(self,event):
        ax.cla()
        

        if self.last_click=="r":
            self.indx=self.indx-1
            
        
        self.indx=self.indx-1
        self.indx=self.indx%len(name_list)

        
        df.boundary.plot(ax=ax,color="black")
        name=name_list[self.indx]

        district=df[df["name"]==name]
        district.plot(ax=ax,color="lightskyblue")
           
        population=district["population"].values[0]

        ax.grid()
        ax.set_title(name,fontsize=24)        
        ax.set_xlabel("Population: {}".format(population))
        ax.set_title(title2, loc='left', y=0.02, x=0.73, fontsize='small',color="royalblue")

        
        ax.set_xticklabels(xlabels)
        ax.set_yticklabels(ylabels)

        self.last_click="l"

    def reset(self,event):
        ax.cla()

        total_population=sum(pd.to_numeric(df["population"]).values)

        ax.grid()
        ax.set_title("Kocaeli",fontsize=24)
        ax.set_xlabel("population: {}".format(total_population))
        ax.set_title(title2, loc='left', y=0.02, x=0.73, fontsize='small',color="royalblue")

        ax.set_xticklabels(xlabels)
        ax.set_yticklabels(ylabels)


        df.plot(ax=ax,color="lightskyblue",edgecolor="black")

        self.last_click=""
        self.indx=0

def transfrom_degree(x):
    x=float(x)
    deg=math.floor(x)
  
    min1=round((x-deg),2)*60
    min2=math.floor(min1)

    if min2<10:
        min2="0"+str(min2)

    return "{}\u00b0{}'".format(deg,min2)


fig,ax=plt.subplots(figsize=(7,6))
plt.subplots_adjust(bottom=0.25)


df=gpd.read_file("C:\Python\geopandas\kocaeli.geojson")

name_list=list(df["name"].values)
name_list.sort()



ax_right=plt.axes([0.55,0.07,0.15,0.06])
ax_left=plt.axes([0.3,0.07,0.15,0.06])
ax_reset=plt.axes([0.475,0.07,0.05,0.06])

Show=show()

button_right=Button(ax_right,">>>",hovercolor="lightskyblue")
button_left=Button(ax_left,"<<<",hovercolor="lightskyblue")
button_reset=Button(ax_reset,"O",hovercolor="lightskyblue")

button_right.on_clicked(Show.show_right)
button_left.on_clicked(Show.show_left)
button_reset.on_clicked(Show.reset)



total_population=sum(pd.to_numeric(df["population"]).values)

title2="""ozan uzun
github.com/uzunozan41
linkedin.com/in/uzunozan41"""
ax.grid()
ax.set_title("Kocaeli",fontsize=24)
ax.set_title(title2, loc='left', y=0.02, x=0.73, fontsize='small',color="royalblue")
ax.set_xlabel("population: {}".format(total_population),fontsize=15)

df.plot(ax=ax,color="lightskyblue",edgecolor="black")


xlabels=[]
for label in ax.get_xticklabels():
    x_label=label.get_text()
    xlabels.append(transfrom_degree(x_label))

ylabels=[]
for label in ax.get_yticklabels():
    y_label=label.get_text()
    ylabels.append(transfrom_degree(y_label))

    

ax.set_xticklabels(xlabels)
ax.set_yticklabels(ylabels)
plt.show()