import Gui
import mainLoop
import Bl_upp
import os
import shutil

def create_catalog(com: str) -> str:
    while True:
        new_catalog = Gui.input_new_catalog()
        if new_catalog == "stop":
            return
        elif not new_catalog:
            continue
        elif os.path.isdir(new_catalog + Gui.txt()):
            Gui.eror_mess()
            print("такой каталог уже есть")
            continue
        else:
            os.mkdir(new_catalog)
            Gui.info_mess()
            return f"Отлично, каталог под именем {new_catalog} сохранён"

def delete_catalog(com: str) -> str:
    while True:
        name_delete_catalog = Gui.name_delete_catalog()
        if name_delete_catalog.lower() == "stop":
            return
        elif not name_delete_catalog:
            continue
        elif not os.path.isdir(name_delete_catalog):
            Gui.eror_mess()
            print("такого каталога нет в списке")
        else:
            shutil.rmtree(os.path.abspath(name_delete_catalog))
            Gui.info_mess()
            return f"Отлично, каталог под именем {name_delete_catalog} удалился"


def info_catalogs(com: str) -> str:
    res = os.listdir(os.getcwd())
    for i in res:
        print(i,end=", ")
    Gui.info_mess()
    return f" - все каталоги"

def create_and_add_book(com: str) -> str:
    while True:
        name_book = Gui.name_add_book()
        if name_book == "stop":
            return
        elif not name_book:
            continue
        elif os.path.isdir(name_book + Gui.txt()):
            Gui.eror_mess()
            print("такая книга уже существует")
            continue
        else:
            while True:
                get_path_dir = Gui.get_path_dir()
                if get_path_dir == "stop":
                    return
                elif not get_path_dir:
                    continue
                elif not os.path.isdir(get_path_dir):
                    Gui.eror_mess()
                    print("такого каталога не существует")
                    continue
                else:
                    os.mkdir(get_path_dir + "/" + name_book + Gui.txt())
                    Gui.info_mess()
                    return \
                    f"Отлично,книга под названием {name_book} сохранена в каталоге {get_path_dir}"

def read_catalog(com: str) -> str:
    while True:
        catalog_read = Gui.catalog_read()
        if catalog_read == "stop":
            return
        elif not catalog_read:
            continue
        elif not os.path.isdir(catalog_read):
            Gui.eror_mess()
            print("Такого каталога не существует")
            continue
        else:
            Gui.info_mess()
            res = os.listdir(catalog_read)
            for i in res:
                print(i,end=", ")
            return f" - все книги в каталоге {catalog_read}"

def search_book(com: str) -> str:
            while True:
                catalog = Gui.search_name_catalog_for_book()
                if catalog == "stop":
                    return
                elif not catalog:
                    continue
                elif not os.path.isdir(catalog):
                    Gui.eror_mess()
                    print("такой каталог не найден")
                    continue
                else:
                    cataloges_books = os.listdir(catalog)
                    res = []
                    while True:
                        search_name_book = Gui.search_name_book()
                        if search_name_book == "stop":
                            return
                        elif not search_name_book:
                            continue

                        else:
                            for book in cataloges_books:
                                if search_name_book  in book:
                                    res.append(book)
                            if res == []:
                                Gui.eror_mess()
                                return f"по запросу {search_name_book} ничего не нашлось"
                            else:
                                Gui.info_mess()
                                for i in res:
                                    print(i,end=", ")
                                return f" - все результаты по запросу {search_name_book}"

def delete_book(com) -> str:
    while True:
        catalog_for_book = Gui.name_delete_catalog_for_book()
        if catalog_for_book == "stop":
            return
        elif not catalog_for_book:
            continue
        elif not os.path.isdir(catalog_for_book):
            Gui.eror_mess()
            print("такого каталога не существует")
            continue
        else:
            while True:
                name_delete_book = Gui.name_delete_book()
                if name_delete_book == "stop":
                    return
                elif not name_delete_book:
                    continue
                elif not os.path.isdir(catalog_for_book + "/" + name_delete_book + Gui.txt()):
                    Gui.eror_mess()
                    print("такой книги не существует")
                    continue
                else:
                    os.rmdir(catalog_for_book + "/" + name_delete_book + Gui.txt())
                    Gui.info_mess()
                    return f"Отлично! книга под названием {name_delete_book} успешна удалена"





