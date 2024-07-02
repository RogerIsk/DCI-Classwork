class ListOfBooks:
    def __init__(self, *args):
        self.__data: tuple = args

    def ls_all(self) -> tuple:
        return self.__data
    
class ListOfStudents:
    def __init__(self, *args):
        self.__data: tuple = args

    def ls_all(self) -> tuple:
        return self.__data
    
class ListOfMusic:
    def __init__(self, *args):
        self.__data: tuple = args

    def ls_all(self) -> tuple:
        return self.__data
    
    def __str__(self):
        return str(list(self.__data))
    

music = ListOfMusic('lala', 'lady')

print(music)

for item in (music):
    print(item.ls_all())