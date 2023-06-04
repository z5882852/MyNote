def read_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
        return data

def read_data_split(file_path, split):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
        data_1 = []
        for dat in data:
            data_1.append(dat.split(split))
        return data_1