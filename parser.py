# -*- coding: utf-8 -*-

import sys

import ply.lex as lex
import ply.yacc as yacc

from symtab import SymbolTable

#開始はグローバル
flg = 1

# インスタンス化
st = SymbolTable()

# トークン指定
tokens = ('IDENT', 'NUMBER', 'BEGIN', 'DIV', 'DO', 'ELSE', 'END', 'FOR', 'FORWARD',
          'FUNCTION', 'IF', 'PROCEDURE', 'PROGRAM', 'READ', 'THEN', 'TO', 'VAR', 'WHILE', 'WRITE',
          'PLUS', 'MINUS', 'MULT', 'EQ', 'NEQ', 'LE', 'LT', 'GE', 'GT', 'LPAREN', 'RPAREN', 'LBRACKET',
          'RBRACKET', 'COMMA', 'SEMICOLON', 'COLON', 'INTERVAL', 'PERIOD', 'ASSIGN')

# 予約語の定義
reserved = {
    'begin': 'BEGIN',
    'div': 'DIV',
    'do': 'DO',
    'else': 'ELSE',
    'end': 'END',
    'for': 'FOR',
    'forward': 'FORWARD',
    'function': 'FUNCTION',
    'if': 'IF',
    'procedure': 'PROCEDURE',
    'program': 'PROGRAM',
    'read': 'READ',
    'then': 'THEN',
    'to': 'TO',
    'var': 'VAR',
    'while': 'WHILE',
    'write': 'WRITE'
}

# 正規表現
t_PLUS = r'\+'
t_MINUS = '-'
t_MULT = r'\*'
t_EQ = '='
t_NEQ = '<>'
t_LE = '<='
t_LT = '<'
t_GE = '>='
t_GT = '>'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = ','
t_SEMICOLON = ';'
t_COLON = ':'
t_INTERVAL = r'\.\.'
t_PERIOD = r'\.'
t_ASSIGN = ':='

t_ignore_COMMENT = r'\#.*'
t_ignore = ' \t'

def t_IDENT(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'IDENT')
    return t


def t_NUMBER(t):
    r'[1-9][0-9]*|0'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Line %d: integer value %s is too large" % t.lineno, t.value)
        t.value = 0
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("不正な文字「", t.value[0], "」")
    t.lexer.skip(1)

#################################################################
# ここから先に構文規則を書く
#################################################################


def p_program(p):# プログラム全体
    '''
    program : PROGRAM IDENT SEMICOLON outblock PERIOD
    '''


def p_outblock(p):# プログラムの中身
    '''
    outblock : var_decl_part subprog_decl_part statement
    '''

# 変数定義
def p_var_decl_part(p):
    '''
    var_decl_part : var_decl_list SEMICOLON
                  |
    '''


def p_var_decl_list(p):
    '''
    var_decl_list : var_decl_list SEMICOLON var_decl
                  | var_decl
    '''


def p_var_decl(p):
    '''
    var_decl : VAR id_list
    '''

# 手続きの定義
def p_subprog_decl_part(p):
    '''
    subprog_decl_part : subprog_decl_list SEMICOLON
                      |
    '''


def p_subprog_decl_list(p):
    '''
    subprog_decl_list : subprog_decl_list SEMICOLON subprog_decl
                      | subprog_decl
    '''


def p_subprog_decl(p):
    '''
    subprog_decl : proc_decl
    '''


def p_proc_decl(p):
    '''
    proc_decl : PROCEDURE proc_name SEMICOLON proc_decl_action_1 inblock proc_decl_action_2
    '''


def p_proc_decl_action_1(p):
    '''
    proc_decl_action_1 :
    '''
    global flg
    flg =0 #手続き開始


def p_proc_decl_action_2(p):
    '''
    proc_decl_action_2 :
    '''
    global flg
    flg =1 #手続き終了
    st.delete()

def p_proc_name(p):
    '''
    proc_name : IDENT proc_name_action
    '''


def p_proc_name_action(p):
    '''
    proc_name_action :
    '''
    st.insert(p[-1], 2) #proc_nameは手続き名


def p_inblock(p): #手続き内の処理
    '''
    inblock : var_decl_part statement
    '''

# 状態定義
def p_statement_list(p):
    '''
    statement_list : statement_list SEMICOLON statement
                   | statement
    '''


def p_statement(p): # 状態
    '''
    statement : assignment_statement
              | if_statement
              | while_statement
              | for_statement
              | proc_call_statement
              | null_statement
              | block_statement
              | read_statement
              | write_statement
    '''


def p_assignment_statement(p):
    '''
    assignment_statement : IDENT assignment_statement_action ASSIGN expression
    '''


def p_assignment_statement_action(p):
    '''
    assignment_statement_action :
    '''
    st.lookup(p[-1])


def p_if_statement(p):
    '''
    if_statement : IF condition THEN statement else_statement
    '''


def p_else_statement(p):
    '''
    else_statement : ELSE statement
                   |
    '''

def p_while_statement(p):
    '''
    while_statement : WHILE condition DO statement
    '''


def p_for_statement(p):
    '''
    for_statement : FOR IDENT for_statement_action ASSIGN expression TO expression DO statement
    '''


def p_for_statement_action(p):
    '''
    for_statement_action :
    '''
    st.lookup(p[-1])


def p_proc_call_statement(p):
    '''
    proc_call_statement : proc_call_name
    '''


def p_proc_call_name(p):
    '''
    proc_call_name : IDENT proc_call_name_action
    '''


def p_proc_call_name_action(p):
    '''
    proc_call_name_action :
    '''
    st.lookup(p[-1])


def p_block_statement(p):
    '''
    block_statement : BEGIN statement_list END
    '''


def p_read_statement(p):
    '''
    read_statement : READ LPAREN IDENT read_statement_action RPAREN
    '''


def p_read_statement_action(p):
    '''
    read_statement_action :
    '''
    st.lookup(p[-1])

def p_write_statement(p):
    '''
    write_statement : WRITE LPAREN expression RPAREN
    '''


def p_null_statement(p):
    '''
    null_statement :
    '''


def p_condition(p): # Bool
    '''
    condition : expression EQ expression
              | expression NEQ expression
              | expression LT expression
              | expression GT expression
              | expression LE expression
              | expression GE expression
    '''


def p_expression(p):
    '''
    expression : term
               | PLUS term
               | MINUS term
               | expression PLUS term
               | expression MINUS term
    '''


def p_term(p):
    '''
    term : factor
         | term MULT factor
         | term DIV factor
    '''


def p_factor(p):
    '''
    factor : var_name
           | NUMBER
           | LPAREN expression RPAREN
    '''


def p_var_name(p):
    '''
    var_name : IDENT var_name_action
    '''


def p_var_name_action(p):
    '''
    var_name_action :
    '''
    st.lookup(p[-1])


def p_arg_list(p):
    '''
    arg_list : expression
             | arg_list COMMA expression
    '''


def p_id_list(p):# 変数宣言
    '''
    id_list : IDENT id_list_action_1
            | id_list COMMA IDENT id_list_action_2
    '''


def p_id_list_action_1(p):
    '''
    id_list_action_1 :
    '''
    st.insert(p[-1], flg) #変数の宣言時

def p_id_list_action_2(p):
    '''
    id_list_action_2 :
    '''
    st.insert(p[-1], flg) #変数の宣言時

#################################################################
# 構文解析エラー時の処理
#################################################################

def p_error(p):
    if p:
        print('{} {} {}'.format(p.lineno, p.type, p.value))
        # p.type, p.value, p.linenoを使ってエラーの処理を書く



#################################################################
# メインの処理
#################################################################


if __name__ == "__main__":
    lexer = lex.lex(debug=0)  # 字句解析器
    yacc.yacc()  # 構文解析器

    # ファイルを開いて
    data = open(sys.argv[1]).read()
    # 解析を実行
    yacc.parse(data, lexer=lexer)
