import sqlite3


executar = sqlite3.connect("Livro.db")

cursor = executar.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS Livros (
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               titulo TEXT NOT NULL UNIQUE, 
               autor TEXT, 
               ano INTEGER,
               genero TEXT, 
               disponivel INTEGER)
                """)

print("Tabela criada com sucesso!")


