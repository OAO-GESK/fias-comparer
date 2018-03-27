# -*- coding: utf-8 -*-

from fix_housenum import HNumFixer

fixer = HNumFixer('houseinfo', 'zaur_mkd', 'houseno', 'korpusno')
fixer.JoinNumsAndLetters('houseandletter')
