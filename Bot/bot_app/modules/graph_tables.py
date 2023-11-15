import pandas as pd
import numpy as np


class Lesson:
    def __init__(self, day: str, time: str, week_type: str, name: str, tutor: str, date: str) -> None:
        self.day = day
        self.time = time
        self.week_type = week_type
        self.name = name
        self.tutor = tutor
        self.date = date

class Group:
    def __init__(self, numb: str, lessons_list: list):
        self.numb = numb
        self.lessons_list = lessons_list


def get_not_nan_value(global_index, value_index, data):
    temp = global_index
    while type(data[temp][value_index]) == type(np.nan):
        temp -= 1
    return data[temp][value_index]


def parse_table_graph(src_path: str):
    exceptions = [
        "Физическая культура и спорт", 
        "пр.Элективные дисциплины по физической культуре и спорту", 
        "фвЭлективные дисциплины по физической культуре и спорту",
        "Элективные дисциплины по физической культуре и спорту",
        "пр.Военная подготовка",
        "НИР",
        "фвЭлективные курсы по физической культуре и спорту",
        "пр.Элективные курсы по физической культуре и спорту"
    ]
    df = pd.read_excel(src_path, header=None)
    data_dict = {}
    cut_index = 0
    while df.values[cut_index][0] != "Дни":
        cut_index += 1
    array = df.values[cut_index:]
    names = list(array[0])
    groups = []
    for el in names[3:]:
        if str(el) != "nan":
            groups.append(el)
    for group in groups:
        group_index = names.index(group)
        group_info = Group(numb=group, lessons_list=[])
        lessons = list(array[1:])
        for index in range(0, len(lessons)):
            lesson = lessons[index]
            if type(lesson[group_index]) != type(np.nan):
                day: str = get_not_nan_value(global_index=index, value_index=0, data=lessons).strip().capitalize()
                time = get_not_nan_value(global_index=index, value_index=1, data=lessons).strip()
                week_type = lesson[2]
                info = lesson[group_index].strip().split('\n')
                name = info[0]
                try: 
                    int(info[-1][0])
                    date = info[-1]
                except:
                    date = "Не указано"
                if not info[0].startswith("Декан") and name != '':
                    try:
                        if len(info) < 4:
                            tutor = info[1]
                        else:
                            tutor = info[2] + ", " + info[1]
                    except:
                        tutor = "Не указан"
                    if name in exceptions:
                        tutor = "Не указан"
                    group_info.lessons_list.append(Lesson(day=day, time=time, week_type=week_type, name=name, tutor=tutor, date=date))
                    # if group == '245' and week_type == 'Знам.' and day == 'Среда':
                    #     print(info)
        
        group = group.split(' ')[0]
        group = group.replace('.', '')
        group = "gr_" + group
        data_dict[group] = []
        for lesson in group_info.lessons_list:
            lesson: Lesson
            if type(lesson.week_type) != type(np.nan):
                (data_dict[group]).append([lesson.day, lesson.time, lesson.week_type, lesson.name, lesson.tutor, lesson.date])
    return data_dict



def save_dict(data_dict: dict, dst_path: str):
    import json
    json_path = f"{dst_path}.json"
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data_dict, json_file, ensure_ascii=False, indent=4)
    return json_path


def refresh_graphs_jsons():
    import os
    SRC_PATH = "resources/tables"
    DST_PATH = "temp/graphs"
    array_paths = os.listdir(SRC_PATH)
    destination_paths = []
    for file in array_paths:
        file_name = file.split('.')[0]
        data = parse_table_graph(src_path=f"{SRC_PATH}/{file}")
        path = save_dict(data_dict=data ,dst_path = f"{DST_PATH}/{file_name}")
        destination_paths.append(path)
    return destination_paths


if __name__ == "__main__":
    refresh_graphs_jsons()
