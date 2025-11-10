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



import sqlite3

con = sqlite3.connect("Livro.db")
cur = con.cursor()

cur.execute("UPDATE Livros SET disponivel = 0 WHERE id = 2")

con.commit()
print("Disponibilidade atualizada!")
con.close()