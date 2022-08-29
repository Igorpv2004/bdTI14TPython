import mysql.connector
from conexao import conexao

class Model:
    def __init__(self):
        self.db_connection = conexao()#ABRINDO A CONEXÃO COM O BD
        self.db_connection = self.db_connection.conectar()# MÉTODO QUE REALIZA A CONEXÃO COM O BD
        self.con = self.db_connection.cursor()#NAVEGAR O BD


    def inserir(self,nome, telefone, endereco, dataDeNascimento):
        try:
            sql = "insert into pessoa(codigo, nome, telefone, endereco, dataDeNascimento) values('','{}','{}','{}','{}')".format(nome, telefone, endereco, dataDeNascimento)
            self.con.execute(sql)
            self.db_connection.commit()#INSERE O DADO NO BD
            return "{} linhas afetadas".format(self.con.rowcount)
        except Exception as erro:
            return erro

    def selecionar(self):
        try:
            sql = "Select * from pessoa"
            self.con.execute(sql)
            msg = ""
            for(codigo, nome, telefone, endereco, dataDeNascimento) in self.con:
                msg = msg + "\nCódigo: {}, Nome: {}, Telefone: {}, Endereço: {}, Data de Nascimento: {}".format(codigo, nome, telefone, endereco, dataDeNascimento)
            return msg
        except Exception as erro:
            return erro
