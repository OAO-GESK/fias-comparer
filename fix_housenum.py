# -*- coding: utf-8 -*-

import MySQLdb

class HNumFixer:

    def __init__(self, db_name, tab_name, fld_num, fld_letter):
        self.db = db_name
        self.tab = tab_name
        self.fld_num = fld_num
        self.fld_letter = fld_letter
        self.dbc = MySQLdb.connect(host='localhost', user='root', passwd='', charset='utf8', db=db_name)

    def __del__(self):
        self.dbc.close()

    def JoinNumsAndLetters(self, fld_to_save):
        curs = self.dbc.cursor()
        curs2 = self.dbc.cursor()
        curs.execute( "select id, %s, %s from %s order by id" % (self.fld_num, self.fld_letter, self.tab) )
        while True:
            row = curs.fetchone()
            if not row: break
            hnum = row[1].strip().upper()
            hnum = hnum.replace('"', '').replace(' ', '')
            hltr = row[2].strip().upper()
            hltr = hltr.replace('"', '').replace(' ', '')
            if hltr.isalpha():
                # В поле корпуса только буква
                hnum += hltr
                hltr = ''
            curs2.execute( "update %s set houseandletter='%s', onlykorp='%s' where id=%s" % (self.tab, hnum, hltr, row[0]) )
        # Закрыть курсоры
        self.dbc.commit()
        curs.close()
        curs2.close()


