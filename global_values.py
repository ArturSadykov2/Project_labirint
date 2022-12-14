import numpy as np
size_hight=1392
size_width=783
scale_x=size_hight/1024
scale_y=size_width/576
size = np.array([size_hight, size_width])
coord_of_start = np.array([[90,80],[100,80],[1250,75],[100,360]])
size_ball=np.array([50*scale_x, 50*scale_x])
cursor_size=100*scale_x
finish_hight = 50*scale_x
finish_width = 100*scale_x
disk_size = np.array([480*scale_x, 480*scale_x])
