import pandas as pd
import numpy as np


def parse_table_graph(src_path: str, dst_path: str):
    excel_file_path = src_path
    df = pd.read_excel(excel_file_path, header=None)
    array = df.values
    transposed_array = np.transpose(array)
    column_arrays = [column.tolist()[2:] for column in transposed_array]
    keys = []
    values = []
    for i in range(len(column_arrays)):
        key = column_arrays[i][0]
        value = column_arrays[i][1:]
        if str(key).startswith('.'):
            key = key[1:]
        filled_array = value
        if i == 2:
            filled_array = pd.Series(value).fillna(method='ffill').tolist()
            key = 'Числитель/Знаменатель'
        if i == 1 or i == 0:
            filled_array = pd.Series(value).fillna(method='ffill').tolist()
        if type(key) != np.nan:
            keys.append(key)
            values.append(filled_array)
    data_dict = dict(zip(keys, values))
    for key in data_dict.keys():
        print(key, data_dict[key])

    graph = {}
    for key in data_dict.keys():
        if key not in ("Дни", "Часы", "Числитель/Знаменатель") and type(key) != float:
            group = key
            array = data_dict[group]
            group_dict = {}
            for lesson in array:
                if type(lesson) != type(np.nan):
                    index = array.index(lesson)
                    day = data_dict['Дни'][index]
                    hour = data_dict['Часы'][index]
                    week_type = data_dict['Числитель/Знаменатель'][index]
                    group_dict[lesson] = {'week_type': week_type, 'day': day, 'hour': hour}
            graph[group] = group_dict

    import json

    with open(f"{dst_path}.json", 'w', encoding='utf-8') as json_file:
        json.dump(graph, json_file, ensure_ascii=False, indent=4)
                
for index in range(1, 6):
    parse_table_graph(src_path=f'dev/tables/{index}_course.xlsx', dst_path=f'dev/graphs/{index}_course')
