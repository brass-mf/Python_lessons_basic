# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("ls - отображение пути текущей директории")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")

def rm():
    return None

def cd():
    return None

def ls():
    print(os.getcwd())

def cp():
    #from shutil import copyfile
    print(file_name)
    if not file_name:
        print('Необходимо указать имя файла вторым параметром')
        return
    file_name = os.path.join(os.getcwd(), file_name)
    try:
        copyfile(file_name, file_name + '_copy')
        print('файл {} создан'.format(file_name))
    except FileExistsError:
        print('файл {} уже существует'.format(file_name))

def make_dir():
        print("Необходи
    if not dir_name:мо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "ls": ls,
    "cp": cp,
    "rm": rm,
    "cd": cd
}

try:
    if sys.argv[1]=='mkdir':
        dir_name = sys.argv[2]
    elif sys.argv[1]=='cp':
        file_name = sys.argv[2]
        print(file_name)
except IndexError:
    dir_name = None
    file_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
