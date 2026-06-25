# ========================================================================================
# IMPORT LIBRARIES
# ========================================================================================

import argparse

# ========================================================================================
# ADD ARGUMENTS
# ========================================================================================

def parse_args():
    parser = argparse.ArgumentParser()    
    parser.add_argument('-type',  
                        type=str,
                        choices=['pdf', 'png', 'jpg', 'itv'],
                        default='itv',
                        help="Output format: pdf, png, jpg, or interactive plot [itv]")
    parser.add_argument('-xaxis', 
                        type=str,
                        choices=['mag', 'flux', 'Jy', 'muJy', 'nJy'],
                        default='mag',
                        help="x-axis choice: magnitudes (AB) [mag], flux density [flux], Janskys [Jy], microJanskys [muJy], or nanoJanskys [nJy]")
    parser.add_argument('-yaxis', 
                        type=str,
                        choices=['MJD', 'JD', 'sec', 'day', 'month', 'year'],
                        default='MJD',
                        help="y-axis choice: Modified Julian Date [MJD], Julian Date [JD], seconds [sec], days [day], months [month], or years [year]")
    parser.add_argument('-scale', 
                        type=str,
                        choices=['lin', 'log', 'xlog', 'ylog'],
                        default='log',
                        help="Axis scaling: linear [lin], logarithmic [log], x-axis logarithmic [xlog], or y-axis logarithmic [ylog]")
    parser.add_argument('-date', 
                        action='store_true',
                        help="Show calendar date on top axis")
    parser.add_argument('-xmin', type=float, help="Min x value")
    parser.add_argument('-xmax', type=float, help="Max x value")
    parser.add_argument('-ymin', type=float, help="Min y value")
    parser.add_argument('-ymax', type=float, help="Max y value")    
    return parser.parse_args()

def get_output_format(output_type):
    format_settings = {
        'itv': {'txtsize': 36, 'mrksize': 12},
        'pdf': {'txtsize': 14, 'mrksize': 8},
        'png': {'txtsize': 14, 'mrksize': 8},
        'jpg': {'txtsize': 14, 'mrksize': 8},
    }
    settings = format_settings[output_type]
    return output_type, settings['txtsize'], settings['mrksize']

def apply_axis_scale(ax, scale):
    scale_map = {
        'lin':  ('linear', 'linear'),
        'log':  ('log', 'log'),
        'xlog': ('log', 'linear'),
        'ylog': ('linear', 'log'),
    }
    xscale, yscale = scale_map[scale]
    ax.set_xscale(xscale)
    ax.set_yscale(yscale)

def get_limits(data_min, data_max, user_min=None, user_max=None):
    lower = data_min if user_min is None else user_min
    upper = data_max if user_max is None else user_max
    return lower, upper