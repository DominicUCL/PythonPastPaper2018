from numpy import *
import matplotlib.pyplot as plt
import argparse
import numpy as np
Xdim=800
Ydim=600
ComplexX=-0.7
ComplexY=0.27015

def get_pixel_value(x,y,Xdim,Ydim,ComplexX,ComplexY):
    zx=1.5*scale_to_size(x,Xdim)
    zy=scale_to_size(y,Ydim)
    colour_code=255
    while (zx*zx+zy*zy<4) and (colour_code>1):
        temporary_x=zx*zx-zy*zy+ComplexX
        zy=2.0*zx*zy+ComplexY
        zx=temporary_x
        colour_code=colour_code-1
    return colour_code

def scale_to_size(pixel_coord,Dimension_Pixel_Count):
    return 1.0*(pixel_coord-Dimension_Pixel_Count/2)/(0.5*Dimension_Pixel_Count)

def generate_grid(Xdim,Ydim,ComplexX,ComplexY):
    Grid = zeros([Ydim,Xdim])
    for (y,x), value in np.ndenumerate(Grid):
            Grid[y][x]=get_pixel_value(x,y,Xdim,Ydim,ComplexX,ComplexY)            
    plt.imshow(Grid)
    plt.savefig("yoyoy.png")
    plt.show()
    

if __name__ == "__main__":
    # command line interface
    parser = argparse.ArgumentParser(description="Produce a Julia pattern")
    parser.add_argument('x_axis_limit', type=int,
                        help='x_dimension of Julia graph')
    parser.add_argument('y_axis_limit', type=int,
                        help='y_dimension of Julia graph')
    parser.add_argument('--ComplexX', type=float,
                        help='ComplexX value')
    parser.add_argument('--ComplexY', type=float,
                        help='ComplexY value')

    arguments = parser.parse_args()

    generate_grid(arguments.x_axis_limit,arguments.y_axis_limit,arguments.ComplexX,arguments.ComplexY)

