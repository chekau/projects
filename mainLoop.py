import Gui
import Bl_upp
import os

def start():
    Gui.start_work()
    main_loop()
    Gui.ending_work()

def main_loop():
    while True:
        name_catalog = Gui.input_name_catalog()
        if name_catalog == "stop":
            Gui.info_mess()
            return
        elif not name_catalog:
            continue
        elif os.path.isdir(name_catalog):
            Gui.eror_mess()
            print("Такой каталог уже создан")
            continue
        else:
            os.mkdir(name_catalog)
            Gui.info_mess()
            print(f"Отлично!Каталог под именем {name_catalog} успешно сохранён!")
            if not start_libary():
                return




def start_libary():
    Gui.info_com()
    while True:
        com = Gui.get_com()
        if com.lower() == "stop":
            return
        elif not com:
            continue
        elif com not in Bl_upp.comm():
            Gui.eror_mess()
            print("Команда не найдена")
            continue
        else:
            result = Bl_upp.analyze_result(com)
            Gui.print_result(result)
