import os

steps = []  # сюда сохраняем порядок обхода


def scan_folder(path):
    info = {
        "path": path,
        "files": [],
        "folders": []
    }

    steps.append(path)  # сохраняем шаг обхода

    try:
        items = os.listdir(path)
    except:
        return info

    for name in items:
        full_path = os.path.join(path, name)

        if os.path.isdir(full_path):
            folder_data = scan_folder(full_path)
            info["folders"].append(folder_data)
        else:
            info["files"].append(name)

    return info


start_path = input("Введите путь к папке: ")
result = scan_folder(start_path)

print("\nПорядок обхода:")
for s in steps:
    print(s)

print("\nСтруктура директорий:")
print(result)

