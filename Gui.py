import Bl_upp



def info_mess():
    print("\033[34m" + "Info:",end="\t")
def your_mess():
    print("\033[32m" + "Your:", end="\t")
def eror_mess():
    print("\033[31m" + "Eror:", end="\t")


def start_work():
    info_mess()
    print("Начало работы...")
    info_mess()
    print("Запуск прошёл успешно!")
    info_mess()
    print("Добро пожаловать в библиотеку!")

def ending_work():
    info_mess()
    print("Завершение работы!")
    info_mess()
    print("Нажмите Enter, чтобы выйти из консоли.")

def info_com():
    info_mess()
    print("Create catalog - создание каталога")
    info_mess()
    print("Delete catalog- удаление каталога")
    info_mess()
    print("Info catalog - информация о всех каталогах")
    info_mess()
    print("Create and add book - создание и добавление новой книги")
    info_mess()
    print("Read catalog - чтение каталога")
    info_mess()
    print("Search book - поиск книги")
    info_mess()
    print("Delete book - удаление книги")
    info_mess()
    print("stop - завершение работы")


def input_name_catalog():
    info_mess()
    print("Введите имя,которым вы бы хотели назвать каталог для его создания")
    your_mess()
    return input()

def input_new_catalog():
    info_mess()
    print("Введите имя,которым вы бы хотели назвать каталог>>")
    your_mess()
    return input()

def name_add_book():
    info_mess()
    print("Введите название книги,которую хотите добавить>>")
    info_mess()
    print("Вы можете написать название_автор_год_жанр книги по желанию")
    your_mess()
    return input()

def get_path_dir():
    info_mess()
    print("Введите название каталога,куда хотите добавить книгу>>")
    your_mess()
    return input()


def get_com():
    info_mess()
    print("Введите любую из данных команд>>>")
    your_mess()
    return input()

def print_result(result):
    print(result)


def txt():
    return ".txt"

def name_delete_catalog():
    info_mess()
    print("Введите название каталога, который вы хотите удалить>>")
    your_mess()
    return input()

def catalog_read():
    info_mess()
    print("Введите название каталога, который вы хотите прочитать>>")
    your_mess()
    return input()

def search_name_book():
    info_mess()
    print("Введите название книги, которую вы хотите найти>>")
    your_mess()
    return input()

def name_delete_book():
    info_mess()
    print("Введите название книги, которую вы хотите удалить >>")
    your_mess()
    return input()

def name_delete_catalog_for_book():
    info_mess()
    print("Введите название каталога,в котором вы хотите удалить книгу>>")
    your_mess()
    return input()

def search_name_catalog_for_book():
    info_mess()
    print("Введите название каталога, в котором вы хотите найти книгу>>")
    your_mess()
    return input()