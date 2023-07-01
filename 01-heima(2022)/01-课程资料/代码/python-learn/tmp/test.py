import os


def get_files_recursion_from_dir(path):
    """
    从指定文件夹中获取全部文件，使用递归
    :param path: 文件夹路径
    :return: list，包含全部的文件，如果目录不存在或无文件，返回空list
    """
    file_list = []
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path = path + "/" + f
            if os.path.isdir(new_path):
                file_list += get_files_recursion_from_dir(new_path)
            else:
                file_list.append(new_path)
    else:
        print(f"指定目录：{path}，不存在")
        return []

    return file_list


files = get_files_recursion_from_dir("D:/test")
for f in files:
    print(f)
    print(os.path.exists(f))

