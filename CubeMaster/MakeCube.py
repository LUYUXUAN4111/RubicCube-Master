from matplotlib import pyplot as plt
import numpy as np
#matplotlibを使って、キューブを表示させる
def makeCube(cube,ax,txt,r):
    colors = cube[0]
    ax.cla()
    #F
    for o in range(3):
        for c in range(3):
            x = np.linspace( 3 -1*o,  3 - (1 + 1*o), 3)
            y = np.linspace(1*c, 1 + 1*c, 3)
            X, Y = np.meshgrid(x, y)
            ax.plot_surface(X = X*0 + 3,
                            Y = Y,
                            Z = X,
                            color=colors[o][c],
                            alpha=1
                            )
    colors = cube[1]
    #L
    for o in range(3):
        for c in range(3):
            x = np.linspace( 1*c,1 + 1*c, 3)
            y = np.linspace( 3 - 1*o,3- (1 + 1*o), 3)
            X, Y = np.meshgrid(x, y)
            ax.plot_surface(X,
                            Y = X*0,
                            Z = Y,
                            color=colors[o][c],
                            alpha=1
                            )
    colors = cube[2]
    #B
    for o in range(3):
        for c in range(3):
            x = np.linspace(3 -1*o,3- (1 + 1*o), 3)
            y = np.linspace( 3 - 1*c,3- (1 + 1*c), 3)
            X, Y = np.meshgrid(x, y)
            ax.plot_surface(X = X*0,
                            Y = Y,
                            Z = X,
                            color=colors[o][c],
                            alpha=1
                            )


    colors = cube[3]
    #R
    for o in range(3):
        for c in range(3):
            x = np.linspace( 3 -1*c,3 - (1 + 1*c), 3)
            y = np.linspace( 3 - 1*o,3- (1 + 1*o), 3)
            X, Y = np.meshgrid(x, y)
            ax.plot_surface(X,
                            Y = X*0 + 3,
                            Z = Y,
                            color=colors[o][c],
                            alpha=1
                            )
    colors = cube[4]
    #U
    for o in range(3):
        for c in range(3):
            x = np.linspace(1*o, 1 + 1*o, 3)
            y = np.linspace(1*c, 1 + 1*c, 3)
            X, Y = np.meshgrid(x, y)
            ax.plot_surface(X,
                            Y,
                            Z=X * 0 + 3,
                            color=colors[o][c],
                            alpha=1
                            )

    colors = cube[5]
    #D
    for o in range(3):
        for c in range(3):
            x = np.linspace(3-1*o, 3-(1 + 1*o), 3)
            y = np.linspace( 1*c,1 + 1*c, 3)
            X, Y = np.meshgrid(x, y)
            ax.plot_surface(X,
                            Y,
                            Z=X * 0,
                            color=colors[o][c],
                            alpha=1
                            )
    colors = cube[0]
    ax.set(xlabel='X',
           ylabel='Y',
           zlabel='Z',
           xlim=(0, 3),
           ylim=(0, 3),
           zlim=(0, 3),
           xticks=np.arange(0, 3, 1),
           yticks=np.arange(0, 3, 1),
           zticks=np.arange(0, 3, 1)
           )

    ax.view_init(elev=r,
                 azim=r
                 )
    plt.xticks()
    plt.yticks()
    plt.title(txt)
    plt.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
    plt.pause(0.1)
