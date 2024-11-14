import sqlite3

def criar_banco():
    # Cria ou abre um banco de dados chamado 'usuarios.db'
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    # Cria a tabela 'usuarios' se ela não existir
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()  # Salva as alterações
    conn.close()   # Fecha a conexão

def adicionar_usuario(username, password):
    # Adiciona um novo usuário ao banco de dados
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    try:
        # Tenta inserir o usuário
        c.execute('INSERT INTO usuarios (username, password) VALUES (?, ?)', (username, password))
    except sqlite3.IntegrityError:
        # Se o usuário já existe, imprime uma mensagem
        print(f"Usuário '{username}' já existe.")
    conn.commit()  # Salva as alterações
    conn.close()   # Fecha a conexão

def validar_login(username, password):
    # Verifica se o usuário e senha estão corretos
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('SELECT * FROM usuarios WHERE username = ? AND password = ?', (username, password))
    usuario = c.fetchone()  # Busca o usuário
    conn.close()  # Fecha a conexão
    return usuario is not None  # Retorna True se o usuário foi encontrado, caso contrário, False
