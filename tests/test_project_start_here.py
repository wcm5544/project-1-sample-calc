"""This is the starting test file"""
import os

import pandas

from app.config import Config
from app.file_ops import FileOperations


def test_main():
    """start  writing code here"""
    total_population_df = pandas.read_csv(
        FileOperations.get_calculate_file_path(Config.data_directory, Config.data_file_name))
    descriptive_stats = Calculator.descriptive_stats(total_population_df, Config.data_field)

    std = .5

    for margin_of_error in Config.margin_of_error:
        for z_score in Config.z_scores:
            population_sample_size = int(PopulationSampleCalc.get_result(z_score, margin_of_error, std,
                                                                         descriptive_stats['population']))
            sample_pop = CreateSampleDataSet.get_sample_data_set(total_population_df, Config.data_field,
                                                                 population_sample_size,
                                                                 descriptive_stats)
            CreateFileFromDataFrame.save_to_csv(sample_pop, z_score, margin_of_error, str(population_sample_size))


class PopulationSampleCalc:
    @staticmethod
    def get_result(z_score: float, margin_error: float, std: float, population: float):
        numerator = (pow(z_score, 2) * std * (1 - std)) / (pow(margin_error, 2))
        denominator = 1 + ((pow(z_score, 2) * std * (1 - std)) / (pow(margin_error, 2) * population))
        return numerator / denominator


class CreateFileFromDataFrame:
    @staticmethod
    def save_to_csv(df: pandas.DataFrame, confidence: str, margin_of_error: str, record_count: str):
        file_name = f"sample_data_number_{confidence}_{margin_of_error}_{record_count}.csv"
        root_directory = FileOperations.get_project_root_directory()
        sample_files_output = Config.sample_files_output
        path = os.path.join(root_directory, sample_files_output, file_name)
        df.to_csv(path, index=False)


class CalculateSampleSize:
    pass


class CreateSampleDataSet:
    @staticmethod
    def get_sample_data_set(df: pandas.DataFrame, data_field: str, sample_size: int, descriptive_stats: dict):
        max_row = pandas.DataFrame(df.loc[df[data_field] == descriptive_stats['max']])
        min_row = pandas.DataFrame(df.loc[df[data_field] == descriptive_stats['min']])
        df = df.drop([max_row.index[0], min_row.index[0]])
        sample_data = PandasSample.result_col_name(df, sample_size - 2)
        sample_data = sample_data.append(max_row)
        sample_data = sample_data.append(min_row)

        return sample_data


class PandasSample:
    @staticmethod
    def result_col_name(df: pandas.DataFrame, number_records_required: int):
        number_records_required = number_records_required
        return df.sample(n=number_records_required)


class PandasDfMean:
    @staticmethod
    def result_col_name(data_frame: pandas.DataFrame, col_name: str):
        return data_frame[col_name].mean()


class PandasDfStdDev:
    @staticmethod
    def result_col_name(data_frame: pandas.DataFrame, col_name: str):
        return data_frame[col_name].std()


class PandasDfMin:
    @staticmethod
    def result_col_name(data_frame: pandas.DataFrame, col_name: str):
        return data_frame[col_name].min()


class PandasDfMax:
    @staticmethod
    def result_col_name(data_frame: pandas.DataFrame, col_name: str):
        return data_frame[col_name].max()


class PandasDfMedian:
    @staticmethod
    def result_col_name(data_frame: pandas.DataFrame, col_name: str):
        return data_frame[col_name].median()


class PandasDfMode:
    @staticmethod
    def result_col_name(data_frame: pandas.DataFrame, col_name: str):
        return data_frame[col_name].mode().iloc[0]


class PandasDfCount:
    @staticmethod
    def result_record_count(data_frame: pandas.DataFrame):
        return data_frame.shape[0]


class Calculator:
    @staticmethod
    def descriptive_stats(pandas_data_frame: pandas.DataFrame, data_field: str):
        descriptive_stats = {"population": PandasDfCount.result_record_count(pandas_data_frame),
                             "mean": PandasDfMean.result_col_name(pandas_data_frame, data_field),
                             "median": PandasDfMedian.result_col_name(pandas_data_frame, data_field),
                             "mode": PandasDfMode.result_col_name(pandas_data_frame, data_field),
                             "min": PandasDfMin.result_col_name(pandas_data_frame, data_field),
                             "max": PandasDfMax.result_col_name(pandas_data_frame, Config.data_field),
                             "std": PandasDfStdDev.result_col_name(pandas_data_frame, data_field)}
        return descriptive_stats
