import pandas as pd
import xlrd

VALID_FILE_EXTENSION = ['xls', 'xlsx', 'csv']

def read_file(filename, **kwargs):

    """Read file with **kwargs; files supported: xls, xlsx, csv"""

    read_map = {'xls': pd.read_excel, 'xlsx': pd.read_excel, 'csv': pd.read_csv}
    file_extension = filename.name.split(".")[1]
    if file_extension in ['xls', 'xlsx']:
        filename = xlrd.open_workbook(file_contents=filename.read())
    return read_map[file_extension](filename, **kwargs)


MODULES_NAME = {
    'PRODUCT': 'Products',
    'AGGREGATION_MODEL_SET': 'Aggregation Keys',
    'MODEL_CATALOG': 'Model Catalog',
}
