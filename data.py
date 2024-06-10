import sqlite3

#conexão ao database

con = sqlite3.connect('dados.db')

#criar tabea "LIVOS"
con.execute('CREATE TABLE livros(\
    id INTEGER PRYMARY KEY,\
    titulo TEXT,\
    autor TEXT,\
    editora TEXT,\
    ano_publicacao INTEGER,\
    isbn TEXT)')

#tabela usuários
con.execute('CREATE TABLE usuarios(\
    id INTEGER PRYMARY KEY,\
    nome TEXT,\
    sobrenome TEXT,\
    email TEXT,\
    telefone TEXT)')

#tabela emprestimo
con.execute('CREATE TABLE emprestimos(\
    id INTEGER PRIMARY KEY,\
    id_livro INTEGER,\
    id_usuario INTEGER,\
    data_emprestimo TEXT,\
    data_devolucao TEXT,\
    FOREIGN KEY(id_livro) REFERENCES livros(id),\
    FOREIGN KEY(id_usuario) REFERENCES usuarios(id))')
