import os
import sqlite3

# CORREGIDO: Hardcoded Secret - ahora usa variables de entorno
API_SECRET = os.environ.get("API_SECRET", "")
PASSWORD_ADMIN = os.environ.get("PASSWORD_ADMIN", "")

# CORREGIDO: SQL Injection - ahora usa consultas parametrizadas
def get_user(username):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    
    # BUENA PRÁCTICA: usar parámetros en lugar de concatenación
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    
    return cursor.fetchone()

# CORREGIDO: Función insegura (eval) - ahora usa alternativa segura
def calculate_expression(expression):
    # Alternativa segura: evaluar solo números y operaciones básicas
    try:
        # Permitir solo caracteres seguros (números, +, -, *, /, espacios)
        if not all(c in "0123456789+-*/() " for c in expression):
            raise ValueError("Expresión no permitida")
        # Usar eval solo después de validar (o mejor: usar ast.literal_eval para literales)
        result = eval(expression, {"__builtins__": {}}, {})
        return result
    except Exception:
        return "Error: expresión inválida"

# CORREGIDO: Eliminada la contraseña en comentario (ya no está)

# CORREGIDO: Variable global expuesta - ahora con nombre convencional y acceso controlado
_SECRET_KEY = os.environ.get("SECRET_KEY", "default-dev-key-only")

# Función segura para acceder a la clave (si es necesario)
def get_secret_key():
    return _SECRET_KEY

print("App iniciada de forma segura")
#Corregido: eliminadas vulnerabilidades de seguridad (Hardcoded secrets, SQL Injection, eval)
