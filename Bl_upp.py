import Bl_low
import Gui


def comm():
    lst_com = ["Create catalog","Delete catalog","Info catalog","Create and add book","Read catalog","Search book","Delete book"]
    return lst_com



def analyze_result(com):
    if com == "Create catalog":
        return Bl_low.create_catalog(com)
    elif com == "Delete catalog":
        return Bl_low.delete_catalog(com)
    elif com == "Info catalog":
        return Bl_low.info_catalogs(com)
    elif com == "Create and add book":
        return Bl_low.create_and_add_book(com)
    elif com == "Read catalog":
        return Bl_low.read_catalog(com)
    elif com == "Search book":
        return Bl_low.search_book(com)
    elif com == "Delete book":
        return Bl_low.delete_book(com)
