import pandas as pd

def remove_specific_row_from_csv(file, column_name, *args):
    '''
    :param file: file to remove the rows from
    :param column_name: The column that determines which row will be
           deleted (e.g. if Column == Name and row-*args
           contains "Gavri", All rows that contain this word will be deleted)
    :param args: Strings from the rows according to the conditions with
                 the column
    '''
    row_to_remove = []
    for row_name in args:
        row_to_remove.append(row_name)
    try:
        df = pd.read_csv(file)
        for row in row_to_remove:
            df = df[eval("df.{}".format(column_name)) != row]
        df.to_csv(file, index=False)
    except Exception  as e:
        raise Exception("Error message....")
