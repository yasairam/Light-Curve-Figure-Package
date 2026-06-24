
def light_curve_generator(data):
    """Create a the light curve from the astronomical input.

    Based on the input from the user in the CLI, this 
        function will generate a publishable light curve.

    Args:
        data (.csv file): csv (Comma Separated Value file). Time-series data of 
            light curve representable astronomical observation (e.g. Quasar/Transit/SNe)

    Returns:
        None: light curve figure is saved to computer.
    """