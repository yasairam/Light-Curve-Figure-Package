import pandas as pd
from astropy.time import Time
import astropy.units as u
import matplotlib.pyplot as plt
import os
from lcfp_cli import apply_axis_scale, get_limits

def conversion(data, flux_units):
    """Convert the two-column table input data into a five-column table. 

    The first two columns will be provided by the user, and should be 1. Time (in "YEAR-MM-DD'), 2. Flux Density (in Jy/microJy/nanoJy).
    Then, the function will populate the next three columns as: 3. Time Converted to MJD, 4. Time Converted to JD, 5. Flux Converted to AB Magnitudes

    Args:
        data (.csv file): csv (Comma Separated Value file). Path to time-series data of 
            light curve representable astronomical observation (e.g. Quasar/Transit/SNe) with two columns.
            These should be: 1. "Time ("YYYY-MM-DD')" and 2. "Flux Density" (in Jy/microJy/nanoJy).
        
        flux_units (str): python string. User selected value being either: nJy, uJy, or Jy to reflect the units
            for the flux densities of the astronomical data.

    Returns:
        pandas DataFrame: Five-column dataframe of 1. Time (format: "YYYY-MM-DD'), 2. Flux Density (in Jy/microJy/nanoJy), 3. Time Converted
            to MJD, 4. Time Converted to JD, 5. Flux Converted to AB Magnitudes
    """
    # Read in data, create a pandas dataframe
    light_curve_dataset = pd.read_csv(data)

    # Validate column names, raise error if file not in specified format
    required_headers = ["Time (YYYY-MM-DD)", "Flux Density"]
    for colname in required_headers:
        if colname not in light_curve_dataset.columns:
            raise ValueError(f"Missing required column name: {colname}")

    # Extract first two user given columns
    time_original = light_curve_dataset["Time (YYYY-MM-DD)"]
    brightness_original = light_curve_dataset["Flux Density"]

    # Using the first column — which should be formatted as a string 'YYYY-MM-DD', create third column as MJD
    light_curve_dataset["Time (MJD)"] = Time(time_original.tolist()).mjd

    # Using the first column — which should be formatted as a string 'YYYY-MM-DD', create fourth column as JD
    light_curve_dataset["Time (JD)"] = Time(time_original.tolist()).jd

    # Using second column - which can be Flux in uJy/nJy/Jy, convert to AB magnitudes
    if flux_units == "nJy":
        flux = brightness_original.values * u.nJy
    elif flux_units == "uJy":
        flux = brightness_original.values * u.uJy
    else:
        flux = brightness_original.values * u.Jy

    light_curve_dataset["Brightness (AB-Magnitude)"] = flux.to(u.ABmag).value

    return light_curve_dataset    
    
def light_curve_generator(data, flux_units, time_sel, brightness_sel, scale_sel, output_sel, xmin=None, xmax=None, ymin=None, ymax=None, show_date=False):
    """Create a light curve from astronomical input.

    Based on the input from the user in the CLI, this function will generate a publishable light curve.

    Args:
        data (.csv file): csv (Comma Separated Value file). Path to time-series data of 
            light curve representable astronomical observation (e.g. Quasar/Transit/SNe) with two columns.
            These should be: 1. "Time ("YYYY-MM-DD')" and 2. "Flux Density" (in Jy/microJy/nanoJy).
        
        flux_units (str): Python string. User selected value being either: nJy, uJy, or Jy to reflect the units
            for the flux densities of the astronomical data.
        
        time_sel (str): Python string. User selected value being either: yyyy_mm_dd, MJD, or JD to reflect the units
            for the time, or x-axis, for the final light curve.
        
        brightness_sel (str): Python string. User selected value being either: flux or ab_mag to reflect the units
            for the brightness, or y-axis, for the final light curve.
        
        log_sel_x (str): Python string. User selected value being either: yes or no to select a logarithmic
            scale to be used for the x-axis. Only works if time_sel == MJD or JD.
        
        log_sel_y (str): Python string. User selected value being either: yes or no to select a logarithmic
            scale to be used for the y-axis. Only works if brightness_sel == flux.
        
        file_type_sel (str): Python string. User selected value being either: png, pdf, or jpeg no as the output
            for the light curve to be saved.
        
        itv (str): Python string. User selected value being either: no or yes for if they wish to have an interactive view or not.

    Returns:
        None: light curve figure saved to computer as either a png, pdf, or jpeg.
    """

    # Get the converted dataset from the user data
    light_curve_data = conversion(data, flux_units)

    # Get each of the column data:
    #time_yyyy_mm_dd = light_curve_data["Time (YYYY-MM-DD)"]
    #brightness_flux_density = light_curve_data["Flux Density"]
    #time_MJD = light_curve_data["Time (MJD)"]
    #time_JD = light_curve_data["Time (JD)"]
    #brightness_ab_magnitude = light_curve_data["Brightness (AB-Magnitude)"]

    x_column = time_sel["column"]
    y_column = brightness_sel["column"]
    x = light_curve_data[x_column]
    y = light_curve_data[y_column]

    ## Plot light curve
    fig, ax = plt.subplots(figsize=(12,8))

    # Select scheme for the light-curve based on user parameters

    # Time selection
    #if time_sel == "yyyy_mm_dd":
    #    x = time_yyyy_mm_dd
    #    ax.set_xlabel("Date [YYYY-MM-DD]", fontsize=16, weight='bold')
    #    ax.tick_params(axis="x", labelrotation=75)
    #elif time_sel == "MJD":
    #    x = time_MJD
    #    ax.set_xlabel("MJD", fontsize=16, weight='bold')
    #elif time_sel == "JD":
    #    x = time_JD
    #    ax.set_xlabel("JD", fontsize=16, weight='bold')

    # Set log_scale for x-axis:
    #if log_sel_x == "yes" and (time_sel == "MJD" or time_sel == "JD"):
    #    ax.set_xscale("log")
    #
    # Brightness selection
    #if brightness_sel == "flux":
    #    if log_sel_y == "yes":
    #        y = brightness_flux_density
    #        ax.set_yscale("log")
    #        ax.set_ylabel(f"Brightness [{flux_units}]", fontsize=16, weight='bold')
    #    else:
    #        y = brightness_flux_density
    #        ax.set_ylabel(f"Brightness [{flux_units}]", fontsize=16, weight='bold')
    #elif brightness_sel == "ab_mag":
    #    y = brightness_ab_magnitude
    #    ax.set_ylabel("Brightness [AB Magnitude]", fontsize=16, weight='bold')
    #    ax.invert_yaxis() # Only invert y-axis if AB magnitude is chosen
    
    # Plot light curve:
    ax.scatter(x, y, color='black', s=output_sel['mrksize'])
    
    ax.set_xlabel(time_sel['xlabel'], fontsize=output_sel['txtsize'], weight='bold')
    ax.set_ylabel(brightness_sel['ylabel'], fontsize=output_sel['txtsize'], weight='bold')
    apply_axis_scale(ax, scale_sel)
    if brightness_sel['invert']:
        ax.invert_yaxis()
    xmin, xmax = get_limits(x.min(), x.max(), xmin, xmax)
    ymin, ymax = get_limits(y.min(), y.max(), ymin, ymax)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    # Making light curve look nice
    ax.tick_params(axis='both',
                   which='major',
                   labelsize=24,
                   width=2,
                   length=8,
                   direction='in',
                   top=True,
                   right=True)
    
    ax.tick_params(axis='both',
                   which='minor',
                   width=1,
                   length=4,
                   direction='in',
                   top=True,
                   right=True)
    
    ax.minorticks_on()

    for spine in ax.spines.values():
        spine.set_linewidth(2)

    plt.rcParams["font.family"] = "serif"

    plt.tight_layout()
    
    # Create output directory if it doesn't exist
    filetype = output_sel['filetype']
    if filetype is not None:
        os.makedirs("output", exist_ok=True)    
        plt.savefig(
            f"output/light_curve_time={time_sel['file_label']}_brightness={brightness_sel['file_label']}.{filetype}",
            dpi=300,
            bbox_inches="tight"
        )
    
    if output_sel['interactive']:
        plt.show()
        
    return fig, ax