# -*- coding: utf-8 -*-

from enum import Enum

class Scope(Enum):
    LOCAL = 0
    GLOBAL = 1
    FUNC = 2


class SymbolTable(object):
    def __init__(self):
        self.symbols = []

    def insert(self, token: str, flg):
        print('----insert----')  #ここから
        #受け取ったトークンとその属性を追加
        self.symbols.append([token, Scope(flg).name])
        for data in self.symbols:
            print('{} {}\n'.format(str(data[0]), data[1]))


    def lookup(self, token: str):
        print('----lookup----')#ここから
        for data in reversed(self.symbols):
            # トークンの検索
            if str(data[0]) == token :
                print('{} {}\n'.format(str(data[0]), data[1]))
                break

    def delete(self):
        print('----delete----')
        for data in self.symbols:
            #局所変数なら削除
            if data[1] == 'LOCAL':
                self.symbols.remove(data)
            #それ以外なら出力
            else:
                print('{} {}\n'.format(str(data[0]), data[1]))





