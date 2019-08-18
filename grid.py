import matplotlib.pyplot as plt

def draw_grid():
	fig = plt.figure()
	ax = plt.axes()
	plt.xlabel("X Axis")
	plt.ylabel("Y Axis")
	plt.rc('grid', linestyle="-", color='black')
	plt.grid(True)
	return fig


def plot_points(fig,d,annotations):
	for coordinate in d:
		x,y = coordinate
		point = plt.scatter(x,y)
		annotation = plt.annotate(d[coordinate],
					xy = (x,y), xycoords = 'data',
					xytext=(x+0.2,y),textcoords = 'data',
					bbox=dict(boxstyle="round", facecolor="w", 
                  	edgecolor="#a3a8a4")
			)
		annotation.set_visible(False)
		annotations.append([point, annotation])

def mouse_move(event):
    visibility_changed = False
    for point, annotation in annotations:
        show_annotation = (point.contains(event)[0] == True)

        if show_annotation != annotation.get_visible():
            visibility_changed = True
            annotation.set_visible(show_annotation)

    if visibility_changed:        
        plt.draw()

d = {
	(-5,-4):"PRR Record\nHEAD_NUM: 1\nSITE_NUM:1\nPART_FLG:0x0\nNUM_TEXT:0\nHARD_BIN:1\nSOFT_BIN:1\nX_COORD:-5\nY_COORD:-4\nTEST_T:515\nPART_ID:1\nPART_TXT:0.000\nPART_FIX: ",
	(-3,-3):None}

fig = draw_grid()
annotations=[]
plot_points(fig,d,annotations)
fig.canvas.mpl_connect('motion_notify_event', mouse_move)
plt.show()


