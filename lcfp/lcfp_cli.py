# ========================================================================================
# IMPORT LIBRARIES
# ========================================================================================

import argparse

# ========================================================================================
# ADD ARGUMENTS
# ========================================================================================

parser = argparse.ArgumentParser()
parser.add_argument('-type',  type=str, 
                    help="output format:"+'\n'+"file [pdf], [png], [jpg], or interactive plot [itv]")
parser.add_argument('-xaxis', type=str, 
                    help="x-axis choice:"+'\n'+"magnitudes (AB) [mag], flux density [flux], Janskys [Jy], microJanskys [muJy], or nanoJanskys [nJy]")
parser.add_argument('-yaxis', type=str,
                    help="y-axis choice:"+'\n'+"Modified Julian Date [MJD], Julian Date [JD], seconds [sec], days [day], months [mon], or years [yr]")
parser.add_argument('-scale', type='str',
                    help="axis scaling:"+'\n'+"linear [lin], logarithmic [log], x-axis logarithmic [xlog], or y-axis logarithmic [ylog]")
parser.add_argument('-date', type=str,
                    help="calendar date on top axis:"+'\n'+"true [True] or false [False]")
parser.add_argument('-xmin', type=float, help="min x value")
parser.add_argument('-xmax', type=float, help="max x value")
parser.add_argument('-ymin', type=float, help="min y value")
parser.add_argument('-ymax', type=float, help="max y value")

args = parser.parse_args()