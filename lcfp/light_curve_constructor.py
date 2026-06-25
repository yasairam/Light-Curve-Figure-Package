import numpy as np
import pandas as pd
from astropy.time import Time
import astropy.units as u


def conversion(data, flux_units):
    """Convert the two-column table input data into a five-column table. 

    The first two columns will be provided by the user, and should be 1. Time (in "YEAR-MM-DD'), 2. Flux Density (in Jy/microJy/nanoJy).
    Then, the function will populate the next three columns as: 3. Time Converted to MJD, 4. Time Converted to JD, 5. Flux Converted to AB Magnitudes

    Args:
        data (.csv file): csv (Comma Separated Value file). Path to time-series data of 
            light curve representable astronomical observation (e.g. Quasar/Transit/SNe) with two columns.
            These should be: 1. "Time ("YYYY-MM-DD')" and 2. "Flux Density" (in Jy/microJy/nanoJy).
        
        flux_units (str): python string. User inputted value being either: nJy, uJy, or Jy to reflect the units
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
    light_curve_dataset["MJD"] = Time(time_original.tolist()).mjd

    # Using the first column — which should be formatted as a string 'YYYY-MM-DD', create fourth column as JD
    light_curve_dataset["JD"] = Time(time_original.tolist()).jd

    # Using second column - which can be Flux in uJy/nJy/Jy, convert to AB magnitudes
    if flux_units == "nJy":
        flux = brightness_original.values * u.nJy
    elif flux_units == "uJy":
        flux = brightness_original.values * u.uJy
    else:
        flux = brightness_original.values * u.Jy

    light_curve_dataset["AB Magnitude"] = flux.to(u.ABmag).value

    return light_curve_dataset    
    
def light_curve_generator(data):
    """Create a light curve from astronomical input.

    Based on the input from the user in the CLI, this function will generate a publishable light curve.

    Args:
        data (.csv file): csv (Comma Separated Value file). Path to time-series data of 
            light curve representable astronomical observation (e.g. Quasar/Transit/SNe) with four columns.
            These should be: 1. Time (in "YEAR-MM-DD'), 2. Flux Density (in Jy/microJy/nanoJy), 3. Time Converted
            to MJD, 4. Time Converted to JD, 5. Flux Converted to AB Magnitudes

    Returns:
        None: light curve figure saved to computer.
    """

    


