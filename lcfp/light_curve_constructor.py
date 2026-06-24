
def light_curve_generator(data):
    """Create a the light curve from the astronomical input.

    Based on the input from the user in the CLI, this function will generate a publishable light curve.

    Args:
        data (.csv file): csv (Comma Separated ) Reference against which cross
            correlation is calculated.

    Returns:
        array: cross-correlation function
    """