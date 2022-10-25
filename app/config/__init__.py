"""This is my program config"""


class Config:
    """Program Configure"""
    data_directory = "data"
    data_file_name = "state_population.csv"
    data_field = "pop"
    sample_files_output = "sample_files_output"
    margin_of_error = (.01, .05, .10)
    z_scores = (1.28, 1.44, 1.65, 1.96, 2.58)
    rounding_precision = 2
