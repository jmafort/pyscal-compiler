import ply.yacc as yacc

from compiler.lexical_analyzer import LexicalAnalyzer
from ast_nodes import *


class SyntacticAnalyzer:
    tokens = LexicalAnalyzer.tokens

    precedence = (
        ('nonassoc','LESSOREQUAL','LESSTHAN','EQUALS','DOUBLEEQUALS','ARROW','MORETHAN'),
        ('left','PLUS','MINUS'),
        ('left','TIMES','DIVIDE'),
    )

    def p_programa(self, p):
        """
        programa : declaracoes bloco
        """

        p[0] = Programa(p[1], p[2])

    def p_declaracoes(self, p):
        """
        declaracoes : def_const def_tipos def_var def_rot
        """

        p[0] = Declaracoes(p[1], p[2], p[3], p[4])

    def p_def_const(self, p):
        """
        def_const : CONST constante SEMICOLON list_const
                  | empty
        """

        p[0] = DefConst(is_empty=True)
        if len(p) == 5:
            p[0] = DefConst(p[2], p[4])

    def p_list_const(self, p):
        """
        list_const : constante SEMICOLON list_const
                   | empty
        """

        p[0] = ListConst(is_empty=True)
        if len(p) == 4:
            p[0] = ListConst(p[1], p[3])

    def p_constante(self, p):
        """
        constante : ID DOUBLEEQUALS const_valor
        """

        p[0] = Constante(p[1], p[3])

    def p_const_valor(self, p):
        """
        const_valor : STRING
                    | exp_mat
        """

        if isinstance(p[1], str):
            p[0] = ConstValor(string=p[1])
        else:
            p[0] = ConstValor(exp_mat=p[1])

    def p_def_tipos(self, p):
        """
        def_tipos : TYPE tipo SEMICOLON list_tipos
                  | empty
        """

        p[0] = DefTipos(is_empty=True)
        if len(p) == 5:
            p[0] = DefTipos(p[2], p[4])

    def p_list_tipos(self, p):
        """
        list_tipos : tipo SEMICOLON list_tipos
                   | empty
        """

        p[0] = ListTipos(is_empty=True)
        if len(p) == 4:
            p[0] = ListTipos(p[1], p[3])

    def p_tipo(self, p):
        """
        tipo : ID DOUBLEEQUALS tipo_dado
        """

        p[0] = Tipo(p[1], p[3])

    def p_tipo_dado(self, p):
        """
        tipo_dado : INTEGER
                  | REAL
                  | ARRAY LSBRACKET NUMBER RSBRACKET OF tipo_dado
                  | RECORD campos END
                  | ID
        """
        
        if len(p) == 7:
            p[0] = TipoDado(p[1], tipo_do_array=p[6])
        elif len(p) == 4:
            p[0] = TipoDado(p[1], p[2])
        else:
            p[0] = TipoDado(p[1])

    def p_campos(self, p):
        """
        campos : ID COLON tipo_dado
               | ID COLON tipo_dado SEMICOLON campos
        """

        if len(p) == 6:
            p[0] = Campos(p[1], p[3], p[5])
        else:
            p[0] = Campos(p[1], p[3])

    def p_def_var(self, p):
        """
        def_var : VAR variavel SEMICOLON list_var
                | empty
        """

        p[0] = DefVar(is_empty=True)
        if len(p) == 5:
            p[0] = DefVar(p[2], p[4])

    def p_list_var(self, p):
        """
        list_var : variavel SEMICOLON list_var
                 | empty
        """

        p[0] = ListVar(is_empty=True)
        if len(p) == 4:
            p[0] = ListVar(p[1], p[3])

    def p_variavel(self, p):
        """
        variavel : ID lista_id COLON tipo_dado
        """

        p[0] = Variavel(p[1], p[2], p[4])

    def p_lista_id(self, p):
        """
        lista_id : COMMA ID lista_id
                 | empty
        """

        p[0] = ListaId(is_empty=True)
        if len(p) == 4:
            p[0] = ListaId(p[2], p[3])

    def p_def_rot(self, p):
        """
        def_rot : nome_rotina def_var bloco def_rot
                | empty
        """

        p[0] = DefRot(is_empty=True)
        if len(p) == 5:
            p[0] = DefRot(p[1], p[2], p[3], p[4])

    def p_nome_rotina(self, p):
        """
        nome_rotina : FUNCTION ID param_rot COLON tipo_dado
                    | PROCEDURE ID param_rot
        """
        
        if len(p) == 4:
            p[0] = NomeRotina(p[1], p[2], p[3])
        else:
            p[0] = NomeRotina(p[1], p[2], p[3], p[5])

    def p_param_rot(self, p):
        """
        param_rot : LPAREN campos RPAREN
                  | empty
        """

        p[0] = ParamRot(is_empty=True)
        if len(p) == 4:
            p[0] = ParamRot(p[2])

    def p_bloco(self, p):
        """
        bloco : BEGIN comando SEMICOLON lista_com END
              | COLON comando
        """

        if len(p) == 3:
            p[0] = Bloco(p[2])
        else:
            p[0] = Bloco(p[2], p[4])

    def p_lista_com(self, p):
        """
        lista_com : comando SEMICOLON lista_com
                  | empty
        """

        p[0] = ListaCom(is_empty=True) 
        if len(p) == 4:
            p[0] = ListaCom(p[1], p[3])

    def p_comando(self, p):
        """
        comando : ID nome atrib
                | WHILE exp_logica DO bloco
                | IF exp_logica THEN bloco else
                | RETURN exp_logica
                | WRITE exp_mat
                | READ ID nome
        """
        
        if p[1].upper() == 'WHILE':
            p[0] = Comando(p[1], exp_logica=p[2], bloco=p[4])
        elif p[1].upper() == 'IF':
            p[0] = Comando(p[1], exp_logica=p[2], bloco=p[4], else_=p[5])
        elif p[1].upper() == 'RETURN':
            p[0] = Comando(p[1], exp_logica=p[2])
        elif p[1].upper() == 'WRITE':
            p[0] = Comando(p[1], exp_mat=p[2])
        elif p[1].upper() == 'READ':
            p[0] = Comando(p[1], id=p[2], nome=p[3])
        # ID
        else:
            p[0] = Comando(p[1], id=p[1], nome=p[2], atrib=p[3])

    def p_else(self, p):
        """
        else : ELSE bloco
             | empty
        """

        p[0] = Else(is_empty=True)
        if len(p) == 3:
            p[0] = Else(p[2])

    def p_atrib(self, p):
        """
        atrib : ASSIGNMENT exp_mat
              | empty
        """
        
        p[0] = Atrib(is_empty=True)
        if len(p) == 3:
            p[0] = Atrib(p[2])

    def p_lista_param(self, p):
        """
        lista_param : parametro COMMA lista_param
                    | parametro
                    | empty
        """

        p[0] = ListaParam(is_empty=True)
        if len(p) == 4:
            p[0] = ListaParam(p[1], p[3])
        else:
            p[0] = ListaParam(p[1])

    def p_op_logico(self, p):
        """
        op_logico : MORETHAN
                  | LESSTHAN
                  | EQUALS
                  | NOT
                  | ARROW
                  | LESSOREQUAL
        """
        
        p[0] = OpLogico(p[1])

    def p_exp_logica(self, p):
        """
        exp_logica : exp_mat op_logico exp_logica
                   | exp_mat
        """
        if len(p) == 4:
            p[0] = ExpLogica(p[1], p[2], p[3])
        else:
            p[0] = ExpLogica(p[1])
    
    def p_exp_mat(self, p):
        """
        exp_mat : parametro op_mat exp_mat
                | parametro
        """

        if len(p) == 4:
            p[0] = ExpMat(p[1], p[2], p[3])
        else:
            p[0] = ExpMat(p[1])

    def p_op_mat(self, p):
        """
        op_mat : PLUS
               | MINUS
               | TIMES
               | DIVIDE
        """

        p[0] = OpMat(p[1])

    def p_parametro(self, p):
        """
        parametro : ID nome
                  | NUMBER
        """

        if len(p) == 3:
            p[0] = Parametro(p[1], p[2])
        else:
            p[0] = Parametro(p[1])

    def p_nome(self, p):
        """
        nome : DOT ID nome
             | LSBRACKET parametro RSBRACKET
             | LPAREN lista_param RPAREN
             | empty
        """
        p[0] = Nome(is_empty=True)

        if len(p) != 2:
            if p[1].upper() == 'DOT':
                p[0] = Nome(id=p[2], nome=p[3])
            elif p[1].upper() == 'LSBRACKET':
                p[0] = Nome(parametro=p[2])
            elif p[1].upper() == 'LPAREN':
                p[0] = Nome(lista_param=p[2])

    def p_error(self, p):
        print(f"\nSyntax error!\nLine: {p.lineno}\nToken: {p.value}\nType: {p.type}")

    def p_empty(self, p):
        """
        empty :
        """
        p[0] = None

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
        return self

    def parse(self, data, **kwargs):
        return self.parser.parse(data, **kwargs)
