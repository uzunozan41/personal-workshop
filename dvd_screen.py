import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.animation import FuncAnimation

from random import randint


fig,ax=plt.subplots(figsize=(50,100))

colors=["red","blue","green","orange","black","purple","pink"]

data={"X":randint(10,90),"Y":randint(5,45),"x":0.5,"y":0.5,"color":colors[randint(0,6)]}

def dvd(i):
    plt.cla()

    ax.add_patch(Rectangle((5,5),95,45,edgecolor="black",facecolor="none"))

    X=data["X"]
    Y=data["Y"]
       
    if X==98:
        data["x"]=-0.5
        data["color"]=colors[randint(0,6)]
    if X==7:
        data["x"]=0.5
        data["color"]=colors[randint(0,6)]

    if Y==49:
        data["y"]=-0.5
        data["color"]=colors[randint(0,6)]
    if Y==5:
        data["y"]=0.5
        data["color"]=colors[randint(0,6)]

    x=data["x"]
    y=data["y"]

    X=X+x
    Y=Y+y

    data["X"]=X
    data["Y"]=Y

    color=data["color"]

    ax.plot(X,Y,".",color="black",markersize=0.1)

    ax.text(X,Y,"DVD",fontsize=15,horizontalalignment="center",color=color,weight="bold")

    print(data)



def on_close(event):
    print('Closed Screen!')
    exit()

fig.canvas.mpl_connect('close_event', on_close)

        


anim=FuncAnimation(fig,dvd,interval=75)

plt.show()




