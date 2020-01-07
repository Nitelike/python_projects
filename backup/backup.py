import os
import time
from zipfile import ZipFile

initial_dir = 'C:\\Users\\ИОН\\Desktop\\python'
target_dir = 'D:\\python_backup'
today_folder = target_dir + os.sep + time.strftime('%Y') + '.' + time.strftime('%m') + '.' + time.strftime('%d')
comment = input('Введите комменарий: ')

if len(comment) > 0:
    target = today_folder + os.sep + time.strftime('%H') + '.' + time.strftime('%M') + '_' + comment.replace(' ', '_') + '.zip'
else:
    target = today_folder + os.sep + time.strftime('%H') + '.' + time.strftime('%M') + '.zip'

if not os.path.exists(today_folder):
    os.mkdir(today_folder)

with ZipFile(target, 'w') as zip_folder:
    for folder_name, subfolders, filenames in os.walk(initial_dir):
        for filename in filenames:
            file_path = os.path.join(folder_name, filename)
            zip_folder.write(file_path)

print('Резервная копия успешно создана в', today_folder)
