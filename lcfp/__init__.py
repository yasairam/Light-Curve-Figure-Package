import os

__version__ = "3.10.20"

# set Python env variable to keep track of example data dir
lcfp_dir = os.path.dirname(__file__)
DATADIR = os.path.join(lcfp_dir, "test_data/")