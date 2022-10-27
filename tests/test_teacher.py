"""This is the starting test file"""
import os


def test_main():
    # pylint: disable=line-too-long
    """My Main Test"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sample_files_output_dir = os.path.join(base_dir, '..', 'sample_files_output')
    sample_files_output_directory_contents = os.listdir(sample_files_output_dir)
    assert len(sample_files_output_directory_contents) - 1 == 15, "There is an incorrect number of files"
    correct_data_file_names = ("sample_data_number_1.28_0.1_22.csv",
                               "sample_data_number_1.28_0.01_51.csv",
                               "sample_data_number_1.28_0.05_39.csv",
                               "sample_data_number_1.44_0.1_25.csv",
                               "sample_data_number_1.44_0.01_51.csv",
                               "sample_data_number_1.44_0.05_41.csv",
                               "sample_data_number_1.65_0.1_29.csv",
                               "sample_data_number_1.65_0.01_51.csv",
                               "sample_data_number_1.65_0.05_43.csv",
                               "sample_data_number_1.96_0.1_33.csv",
                               "sample_data_number_1.96_0.01_51.csv",
                               "sample_data_number_1.96_0.05_45.csv",
                               "sample_data_number_2.58_0.1_39.csv",
                               "sample_data_number_2.58_0.01_51.csv",
                               "sample_data_number_2.58_0.05_48.csv")

    for filename in correct_data_file_names:
        assert filename in sample_files_output_directory_contents, "A filename is incorrect"
