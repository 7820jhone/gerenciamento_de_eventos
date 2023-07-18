# biblioteca responsavel por interagir com o banco de dados
import sqlite3

# conectar (ou criar) o banco de dados
conexao = sqlite3.connect('eventos.db')

# criando um objeto cursosr para executar comandos SQL 
cursor = conexao.cursor()

# criando a tabela de eventos
cursor.execute('''
CREATE TABLE IF NOT EXISTS eventos (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL UNIQUE,
    data TEXT NOT NULL,
    local TEXT NOT NULL
);
 ''')

# criando tabela de organizador
cursor.execute('''
CREATE TABLE IF NOT EXISTS organizador (
    id INT PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    cpf TEXT,
    id_eventos INT,
    FOREIGN KEY (id_eventos) REFERENCES eventos(id)
);
''')

# salvando as alterações e fechando a conexão
conexao.commit()
conexao.close()