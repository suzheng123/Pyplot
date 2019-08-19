import matplotlib.pyplot as plt

def draw_grid():
	fig = plt.figure()
	ax = plt.axes()
	plt.xlabel("X Axis")								# add label as 'X Axis' to x-axis
	plt.ylabel("Y Axis")								# add label as 'Y Axis' to y-axis
	plt.rc('grid', linestyle="-", color='black')		# draw the grid
	plt.grid(True)
	return fig


def plot_points(fig,d,point_annotation):
	for coordinate in d:
		x,y = coordinate
		point = plt.scatter(x,y)						# plot the point according to coordinate 
		annotation = plt.annotate(d[coordinate],		# create annotation for point
					xy = (x,y), xycoords = 'data',
					xytext=(x+0.2,y),textcoords = 'data',
					bbox=dict(boxstyle="round", facecolor="#e8ebe9", 
                  	edgecolor="#a3a8a4")
			)
		annotation.set_visible(False) 					# default to not show annotation
		point_annotation.append([point, annotation])    # push point-annotation pair to the list   

def hover(event):
    for point, annotation in point_annotation:
        show_annotation = (point.contains(event)[0] == True)	# bool: if mouse on the point T or F

        if show_annotation != annotation.get_visible(): # if mouse on the point && annotation is not visible
            annotation.set_visible(show_annotation)		# set annotation visible
            plt.draw()									# draw the annotation 


def coordinate_annotation(d):
	fig = draw_grid()
	plot_points(fig,d,point_annotation)
	connect_id = fig.canvas.mpl_connect('motion_notify_event', hover) # create connect_id for each hover event


if __name__ == '__main__':
	info_d = {
		(-5,-4):"PRR Record\nHEAD_NUM: 1\nSITE_NUM:1\nPART_FLG:0x0\nX_COORD:-5\nY_COORD:-4\nTEST_T:515\nPART_ID:1\n",
		(-2,-3):"test data",
		(-3,-3):"test data2"}

	point_annotation = [] #  pairs of point and corresponding annotation

	coordinate_annotation(info_d)

	plt.show()


