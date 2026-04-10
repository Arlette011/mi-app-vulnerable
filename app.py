import sqlite3

# VULNERABILIDAD 1: Hardcoded Secret (contraseña en texto plano)
API_SECRET = "sk-1234567890-secret-key"
PASSWORD_ADMIN = "admin123"

# VULNERABILIDAD 2: SQL Injection
def get_user(username):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    
    # MALA PRÁCTICA: concatenar directamente la entrada del usuario
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    
    return cursor.fetchone()

# VULNERABILIDAD 3: Función insegura (eval)
def calculate_expression(expression):
    # PELIGROSO: eval ejecuta cualquier código Python
    result = eval(expression)
    return result

# VULNERABILIDAD 4: Contraseña en comentario (mala práctica)
# TODO: cambiar contraseña de producción: ProdPass2024!

# VULNERABILIDAD 5: Variable global expuesta
SECRET_KEY = "my-super-secret-key-123"

print("App iniciada")
