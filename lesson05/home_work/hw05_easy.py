# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os

def createdir():
    dir_path1 = os.path.join(os.getcwd(), 'dir_1')
    dir_path9 = os.path.join(os.getcwd(), 'dir_9')
    try:
        os.mkdir(dir_path1)
        os.mkdir(dir_path9)
        result = os.listdir(path=os.getcwd())
    except FileExistsError:
        result = 'Такая директория уже существует'
    return result

def rmdir():
    dir_path1 = os.path.join(os.getcwd(), 'dir_1')
    dir_path9 = os.path.join(os.getcwd(), 'dir_9')
    try:
        os.rmdir(dir_path1)
        os.rmdir(dir_path9)
        result = os.listdir(path=os.getcwd())
    except FileNotFoundError:
        result = 'Такая директория отсутствует'
    return result

print(createdir())
print(rmdir())

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def lsdir():
    result = ''
    for item in os.listdir(path=os.getcwd()):
        if os.path.isdir(os.path.join(os.getcwd(), item)):
            result = result + item + '\n'
    return result
print('-----список папок-------')
print(lsdir())
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import sys
print('----TASK3------')
from shutil import copyfile
copyfile(sys.argv[0], sys.argv[0]+'_copy')
