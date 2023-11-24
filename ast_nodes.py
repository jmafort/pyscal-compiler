class Node:

    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        node_str = "   "*level+self.identificador
        if descricao:
            node_str += f"_{descricao}"
        print(node_str)

class Programa(Node):
    def __init__(self, declaracoes, bloco):
        self.identificador = "programa"
        self.declaracoes: Declaracoes = declaracoes
        self.bloco: Bloco = bloco

    def print_tree(self, level=0) -> None:
        super().print_tree(level)
        self.declaracoes.print_tree(level+1)
        self.bloco.print_tree(level+1)

class Declaracoes(Node):
    def __init__(self, def_const, def_tipos, def_var, def_rot):
        self.identificador = "declaracoes"
        self.def_const: DefConst = def_const
        self.def_tipos: DefTipos = def_tipos
        self.def_var: DefVar = def_var
        self.def_rot: DefRot = def_rot

    def print_tree(self, level=0) -> None:
        super().print_tree(level)
        self.def_const.print_tree(level+1)
        self.def_tipos.print_tree(level+1)
        self.def_var.print_tree(level+1)
        self.def_rot.print_tree(level+1)

class DefConst(Node):
    def __init__(self, constante = None, list_const = None, is_empty: bool = False):
        self.identificador = "def_const"
        self.constante: Constante = constante
        self.list_const: ListConst = list_const
        self.is_empty: bool = is_empty

    def print_tree(self, level=0) -> None:
        if not self.is_empty:
            super().print_tree(level)
            self.constante.print_tree(level+1)
            self.list_const.print_tree(level+1)

class ListConst(Node):
    def __init__(self, constante = None, list_const = None, is_empty: bool = False):
        self.identificador = "list_const"
        self.constante: Constante = constante
        self.list_const: ListConst = list_const
        self.is_empty: bool = is_empty

    def print_tree(self, level=0) -> None:
        if not self.is_empty:
            super().print_tree(level)
            self.constante.print_tree(level+1)
            self.list_const.print_tree(level+1)

class Constante(Node):
    def __init__(self, id, const_valor):
        self.identificador = "constante"
        self.id: str = id
        self.const_valor: ConstValor = const_valor

    def print_tree(self, level=0) -> None:
        super().print_tree(level, self.id)
        self.const_valor.print_tree(level+1)

class ConstValor(Node):
    def __init__(self, string = None, exp_mat = None):
        self.identificador = "const_valor"
        self.string: str = string
        self.exp_mat: ExpMat = exp_mat

    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        super().print_tree(level, str(self.string) if self.string else None)
        if self.exp_mat:
            self.exp_mat.print_tree(level+1)

class DefTipos(Node):
    def __init__(self, tipo = None, list_tipos = None, is_empty: bool = False):
        self.identificador = "def_tipos"
        self.tipo: Tipo = tipo
        self.list_tipos: ListTipos = list_tipos
        self.is_empty: bool = is_empty

    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        if not self.is_empty:
            super().print_tree(level)
            self.tipo.print_tree(level+1)
            self.list_tipos.print_tree(level+1)

class ListTipos(Node):
    def __init__(self, tipo = None, list_tipos = None, is_empty: bool = False):
        self.identificador = "list_tipos"
        self.tipo: Tipo = tipo
        self.list_tipos: ListTipos = list_tipos
        self.is_empty: bool = is_empty
    
    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        if not self.is_empty:
            super().print_tree(level)
            self.tipo.print_tree(level+1)
            self.list_tipos.print_tree(level+1)

class Tipo(Node):
    def __init__(self, id, tipo_dado):
        self.identificador = "tipo"
        self.id: str = id
        self.tipo_dado: TipoDado = tipo_dado

    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        super().print_tree(level, self.id)
        self.tipo_dado.print_tree(level+1)

class TipoDado(Node):
    def __init__(self, tipo, campos=None, tipo_do_array=None):
        self.identificador = "tipo_dado"
        self.tipo: str = tipo
        self.campos: Campos = campos
        self.tipo_do_array: str = tipo_do_array

    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        super().print_tree(level, self.tipo+f"_{self.tipo_do_array}" if self.tipo == "ARRAY" else self.tipo)
        if self.campos:
            self.campos.print_tree(level+1)

class Campos(Node):
    def __init__(self, id, tipo_dado, campos=None):
        self.identificador = "campos"
        self.id: str = id
        self.tipo_dado: TipoDado = tipo_dado
        self.campos: Campos = campos

    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        super().print_tree(level, self.id)
        self.tipo_dado.print_tree(level+1)
        if self.campos:
            self.campos.print_tree(level+1)

class DefVar(Node):
    def __init__(self, variavel = None, list_var = None, is_empty: bool = False):
        self.identificador = "def_var"
        self.variavel: Variavel = variavel
        self.list_var: ListVar = list_var
        self.is_empty: bool = is_empty

    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        if not self.is_empty:
            super().print_tree(level)
            self.variavel.print_tree(level+1)
            self.list_var.print_tree(level+1)

class ListVar(Node):
    def __init__(self, variavel = None, list_var = None, is_empty = False):
        self.identificador = "list_var"
        self.variavel: Variavel = variavel
        self.list_var: ListVar = list_var
        self.is_empty: bool = is_empty

    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        if not self.is_empty:
            super().print_tree(level)
            self.variavel.print_tree(level+1)
            self.list_var.print_tree(level+1)

class Variavel(Node):
    def __init__(self, id, lista_id, tipo_dado):
        self.identificador = "variavel"
        self.id: str = id
        self.lista_id: ListaId = lista_id
        self.tipo_dado: TipoDado = tipo_dado
    
    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        super().print_tree(level, self.id)
        self.lista_id.print_tree(level+1)
        self.tipo_dado.print_tree(level+1)

class ListaId(Node):
    def __init__(self, id = None, lista_id = None, is_empty = False):
        self.identificador = "lista_id"
        self.id: str = id
        self.lista_id: ListaId = lista_id
        self.is_empty: bool = is_empty

    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        if not self.is_empty:
            super().print_tree(level, self.id)
            self.lista_id.print_tree(level+1)

class DefRot(Node):
    def __init__(self, nome_rotina = None, def_var = None, bloco = None, def_rot = None, is_empty = False):
        self.identificador = "def_rot"
        self.nome_rotina: NomeRotina = nome_rotina
        self.def_var: DefVar = def_var
        self.bloco: Bloco = bloco
        self.def_rot: DefRot = def_rot
        self.is_empty: bool = is_empty

    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        if not self.is_empty:
            super().print_tree(level)
            self.nome_rotina.print_tree(level+1)
            self.def_var.print_tree(level+1)
            self.bloco.print_tree(level+1)
            self.def_rot.print_tree(level+1)

class NomeRotina(Node):
    def __init__(self, function_ou_procedure, id, param_rot, tipo_dado=None):
        self.identificador = "nome_rotina"
        self.function_ou_procedure: str = function_ou_procedure
        self.id: str = id
        self.param_rot: ParamRot = param_rot
        self.tipo_dado: TipoDado = tipo_dado

    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        super().print_tree(level, self.function_ou_procedure+f"_{self.id}")
        self.param_rot.print_tree(level+1)
        if self.tipo_dado:
            self.tipo_dado.print_tree(level+1)

class ParamRot(Node):
    def __init__(self, campos = None, is_empty = False):
        self.identificador = "param_rot"
        self.campos: Campos = campos
        self.is_empty: bool = is_empty

    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        if not self.is_empty:
            super().print_tree(level)
            self.campos.print_tree(level+1)

class Bloco(Node):
    def __init__(self, comando, lista_com=None):
        self.identificador = "bloco"
        self.comando: Comando = comando
        self.lista_com: ListaCom = lista_com

    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        super().print_tree(level)
        self.comando.print_tree(level+1)
        if self.lista_com:
            self.lista_com.print_tree(level+1)

class ListaCom(Node):
    def __init__(self, comando = None, lista_com = None, is_empty = False):
        self.identificador = "lista_com"
        self.comando: Comando = comando
        self.lista_com: ListaCom = lista_com
        self.is_empty: bool = is_empty

    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        if not self.is_empty:
            super().print_tree(level)
            self.comando.print_tree(level+1)
            self.lista_com.print_tree(level+1)

class Comando(Node):
    def __init__(self, tipo, id=None, nome=None, atrib=None, exp_logica=None, bloco=None, exp_mat=None, else_=None):
        self.identificador = "comando"
        self.tipo: str = tipo
        self.id: str = id
        self.nome: Nome = nome
        self.atrib: Atrib = atrib
        self.exp_logica: ExpLogica = exp_logica
        self.bloco: Bloco = bloco
        self.exp_mat: ExpMat = exp_mat
        self.else_: Else = else_

    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        descricao = self.tipo
        super().print_tree(level, descricao)

        if self.nome:
            self.nome.print_tree(level+1)
        if self.atrib:
            self.atrib.print_tree(level+1)
        if self.exp_logica:
            self.exp_logica.print_tree(level+1)
        if self.bloco:
            self.bloco.print_tree(level+1)
        if self.exp_mat:
            self.exp_mat.print_tree(level+1)
        if self.else_:
            self.else_.print_tree(level+1)

class Else(Node):
    def __init__(self, bloco = None, is_empty = False):
        self.identificador = "else"
        self.bloco: Bloco = bloco
        self.is_empty: bool = is_empty

    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        if not self.is_empty:
            super().print_tree(level)
            self.bloco.print_tree(level+1)

class Atrib(Node):
    def __init__(self, exp_mat = None, is_empty = False):
        self.identificador = "atrib"
        self.exp_mat: ExpMat = exp_mat
        self.is_empty: bool = is_empty
    
    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        if not self.is_empty:
            super().print_tree(level)
            self.exp_mat.print_tree(level+1)

class ListaParam(Node):
    def __init__(self, parametro = None, lista_param = None, is_empty = False):
        self.identificador = "lista_param"
        self.parametro: Parametro = parametro
        self.lista_param: ListaParam = lista_param
        self.is_empty: bool = is_empty

    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        if not self.is_empty:
            super().print_tree(level)
            self.parametro.print_tree(level+1)
            if self.lista_param:
                self.lista_param.print_tree(level+1)

class OpLogico(Node):
    def __init__(self, operador):
        self.identificador = "op_logico"
        self.operador: str = operador
    
    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        super().print_tree(level, self.operador)

class ExpLogica(Node):
    def __init__(self, exp_mat, op_logico=None, exp_logica=None):
        self.identificador = "exp_logica"
        self.exp_mat: ExpMat = exp_mat
        self.op_logico: OpLogico = op_logico
        self.exp_logica: ExpLogica = exp_logica

    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        super().print_tree(level)
        self.exp_mat.print_tree(level+1)
        if self.op_logico:
            self.op_logico.print_tree(level+1)
        if self.exp_logica:
            self.exp_logica.print_tree(level+1)

class ExpMat(Node):
    def __init__(self, parametro, op_mat=None, exp_mat=None):
        self.identificador = "exp_mat"
        self.parametro: Parametro = parametro
        self.op_mat: OpMat = op_mat
        self.exp_mat: ExpMat = exp_mat

    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        super().print_tree(level)
        self.parametro.print_tree(level+1)
        if self.op_mat:
            self.op_mat.print_tree(level+1)
        if self.exp_mat:
            self.exp_mat.print_tree(level+1)

class OpMat(Node):
    def __init__(self, operacao):
        self.identificador = "op_mat"
        self.operacao: str = operacao

    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        super().print_tree(level, self.operacao)

class Parametro(Node):
    def __init__(self, id_ou_valor, nome=None):
        self.identificador = "parametro"
        self.id_ou_valor: str = id_ou_valor
        self.nome: Nome = nome

    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        super().print_tree(level, self.id_ou_valor)
        if self.nome:
            self.nome.print_tree(level+1)

class Nome(Node):
    def __init__(self, id = None, nome = None, parametro = None, lista_param = None, is_empty = False):
        self.identificador = "nome"
        self.id: str = id
        self.nome: Nome = nome
        self.parametro: Parametro = parametro
        self.lista_param: ListaParam = lista_param
        self.is_empty: bool = is_empty

    def print_tree(self, level: int = 0, descricao: str = None) -> None:
        if not self.is_empty:
            super().print_tree(level, self.id)
            if self.nome:
                self.nome.print_tree(level+1)
            if self.parametro:
                self.parametro.print_tree(level+1)
            if self.lista_param:
                self.lista_param.print_tree(level+1)
