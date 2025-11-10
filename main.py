# import sqlite3


# executar = sqlite3.connect("Livro.db")

# cursor = executar.cursor()

# cursor.execute("""
#                CREATE TABLE IF NOT EXISTS Livros (
#                id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                titulo TEXT NOT NULL UNIQUE, 
#                autor TEXT, 
#                ano INTEGER,
#                genero TEXT, 
#                disponivel INTEGER)
#                 """)

# print("Tabela criada com sucesso!")


# import sqlite3
# con = sqlite3.connect("Livro.db")
# cur = con.cursor()

# livros = [
#     ('A Sombra do Vento', 'Carlos Ruiz Zafón', 2001, 'Mistério', 1),
#     ('1984', 'George Orwell',1949, 'Ficção Científica', 0),
#     ('O Senhor dos Anéis', 'J.R.R. Tolkien',1954, 'Fantasia', 1),
#     ('Dom Quixote', 'Miguel de Cervantes',1605, 'Romance', 1),
#     ('Cem Anos de Solidão', 'Gabriel García Márquez',1967, 'Realismo Mágico', 0)
# ]

# cur.executemany("""
#                 INSERT INTO Livros (titulo, autor, ano, genero, disponivel)
#                 VALUES(?, ?, ?, ?, ?)
#                 """, livros)

# con.commit()
# print("Livros inseridos com sucesso!")
# con.close()



# import sqlite3

# con = sqlite3.connect("Livro.db")
# cur = con.cursor()

# cur.execute("SELECT*FROM Livros WHERE disponivel=1")
# livros_disponiveis = cur.fetchall()

# print("Livros disponíveis:")
# for livro in livros_disponiveis:
#     print(livro)
# con.close()



# import sqlite3

# con = sqlite3.connect("Livro.db")
# cur = con.cursor()

# cur.execute("UPDATE Livros SET disponivel = 0 WHERE id = 2")

# con.commit()
# print("Disponibilidade atualizada!")
# con.close()



# import sqlite3

# con = sqlite3.connect("Livro.db")
# cur = con.cursor()

# cur.execute("SELECT*FROM Livros ORDER BY ano DESC")
# ordenados = cur.fetchall()

# print("Livros ordenados do mais recente ao mais antigo:")
# for livro in ordenados:
#     print(livro)
# con.close()



# import sqlite3

# con = sqlite3.connect("Livro.db")
# cur = con.cursor()

# cur.execute("DELETE FROM Livros WHERE ano = (SELECT MIN (ano) FROM Livros)")
# ordenados = cur.fetchall()

# con.commit()
# print("Livro mais antigo deletado!")
# con.close()


# import sqlite3
# con = sqlite3.connect("dados.db")
# cur = con.cursor()
# cur.execute("""
#             CREATE TABLE Usuario (
#             id INTEGER PRIMARY KEY AUTOINCREMENT, 
#             nome TEXT
#             );
#             """)

# print("Tabela Usuario criada com sucesso!")



# import sqlite3
# con = sqlite3.connect("dados.db")
# cur = con.cursor()

# cur.execute("ALTER TABLE Usuario ADD COLUMN idade INTEGER;")

# con.commit()
# con.close()
# print("Coluna 'idade' adicionada com sucesso!")



import sqlite3
con = sqlite3.connect("dados.db")
cur = con.cursor()

usuarios = [
    ("Alice", 25),
    ("Bruno", 30),
    ("Carla", 22),
    ("Diego", 28),
    ("Elisa", 35)
]

cur.executemany("INSERT INTO Usuario (nome, idade) VALUES(?, ?)", usuarios)

con.commit()
con.close()
print("5 usuários inseridos com sucesso!")