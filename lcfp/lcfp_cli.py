# ========================================================================================
# IMPORT LIBRARIES
# ========================================================================================

import argparse

# ========================================================================================
# ADD ARGUMENTS
# ========================================================================================

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file',
                        help="Path to the input file")
    parser.add_argument('-type',
                        dest='output_type',  
                        type=str,
                        choices=['pdf', 'png', 'jpg', 'itv'],
                        default='itv',
                        help="Output format: pdf, png, jpg, or interactive plot [itv]")
    parser.add_argument('-xaxis', 
                        type=str,
                        choices=['MJD', 'JD', 'sec', 'day', 'mon', 'yr'],
                        default='MJD',
                        help="x-axis choice: Modified Julian Date [MJD], Julian Date [JD], seconds [sec], days [day], months [mon], or years [yr]")
    parser.add_argument('-yaxis', 
                        type=str,
                        choices=['mag', 'flux'],
                        default='mag',
                        help="y-axis choice: AB magnitudes [mag] or flux density [flux]")
    parser.add_argument('-flux_units',
                        type=str,
                        choices=['Jy', 'uJy', 'nJy'],
                        default='Jy',
                        help="Flux density units: Janskys [Jy], microJanskys [uJy], or nanoJanskys [nJy]")
    parser.add_argument('-scale', 
                        type=str,
                        choices=['lin', 'log', 'xlog', 'ylog'],
                        default='lin',
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
        'itv': {'filetype': None,  'interactive': True,  'txtsize': 36, 'mrksize': 12},
        'pdf': {'filetype': 'pdf', 'interactive': False, 'txtsize': 14, 'mrksize': 8},
        'png': {'filetype': 'png', 'interactive': False, 'txtsize': 14, 'mrksize': 8},
        'jpg': {'filetype': 'jpg', 'interactive': False, 'txtsize': 14, 'mrksize': 8},
    }
    return format_settings[output_type]

def get_xaxis_units(xunit):
    xaxis_settings = {
        'MJD': {'column': 'Time (MJD)', 'xlabel': 'Time [MJD]',    'file_label': 'MJD'},
        'JD' : {'column': 'Time (JD)',  'xlabel': 'Time [JD]',     'file_label': 'JD'},
        'sec': {'column': 'Time (sec)', 'xlabel': 'Time [s]',      'file_label': 'sec'},
        'day': {'column': 'Time (day)', 'xlabel': 'Time [days]',   'file_label': 'day'},
        'mon': {'column': 'Time (mon)', 'xlabel': 'Time [months]', 'file_label': 'mon'},
        'yr' : {'column': 'Time (yr)',  'xlabel': 'Time [yr]',     'file_label': 'yr'},
    }
    return xaxis_settings[xunit]
    
#def get_yaxis_units(yunit):
#    yaxis_settings = {
#        'mag': {'column': 'Brightness (AB-Magnitude)', 'ylabel': 'Brightness [mag AB]',   'file_label': 'mag', 'invert': True},
#        'Jy' : {'column': 'Flux Density',              'ylabel': 'Brightness [Jy]',       'file_label': 'Jy',  'invert': False},
#        'uJy': {'column': 'Flux Density',              'ylabel': r'Brightness [$\mu$Jy]', 'file_label': 'uJy', 'invert': False},
#        'nJy': {'column': 'Flux Density',              'ylabel': 'Brightness [nJy]',      'file_label': 'nJy', 'invert': False},
#    }
#    return yaxis_settings[yunit]

def get_yaxis_units(yunit, fluxunit):
    yaxis_settings = {
        'mag' : {'column': 'Brightness (AB-Magnitude)', 'ylabel': 'Brightness [mag AB]',      'file_label': 'mag',  'invert': True},
        'flux': {'column': 'Flux Density',              'ylabel': f'Brightness [{fluxunit}]', 'file_label': 'flux', 'invert': False}, 
    }
    return yaxis_settings[yunit]

def apply_axis_scale(ax, scale):
    scale_map = {
        'lin' : ('linear', 'linear'),
        'log' : ('log', 'log'),
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