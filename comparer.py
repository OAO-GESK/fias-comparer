# -*- coding: utf-8 -*-

import MySQLdb


class StreetsComparer:
    """
    Класс реализует функционал анализа соответствия наименований улиц из таблицы пользовательской БД 
    значениям таблицы адресных объектов системы ФИАС.
    Имя пользовательской БД,  таблицы и наименование поля с наименованием улицы передаются в конструкторе.
    Условие: в пользовательской таблице, содержащей названия улиц, должны быть созданы поля:
    - `fias_aoguid` типа char(36)
    - `fias_offname` типа varchar(255)
    """

    def __init__(self, dbname, tablename, fieldname):
        self.dbc_user = MySQLdb.connect(host="locahost", user="root", passwd="", charset="", db=dbname)
        self.user_tab = tablename
        self.street_field = fieldname
