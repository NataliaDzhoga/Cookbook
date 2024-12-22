dict_files = {}


def get_info_about_file(name):

    with open(name, encoding='UTF-8') as f:
        data = f.read()
        dict_files[len(data.strip().split('\n'))] = [name, data]


get_info_about_file('1.txt')
get_info_about_file('2.txt')
get_info_about_file('3.txt')
sorted_dict_files = dict(sorted(dict_files.items()))


with open('new_file.txt', 'w', encoding='UTF-8') as f:
    for file in sorted_dict_files.keys():
        f.write(sorted_dict_files[file][0] + '\n')
        f.write(str(file) + '\n')
        f.write(sorted_dict_files[file][1] + '\n')
