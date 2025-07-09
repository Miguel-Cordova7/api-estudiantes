import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('alumnos.db')
    conn.row_factory = sqlite3.Row
    return conn

# Endpoint para GET /alumnos
@app.route('/alumnos', methods=['GET'])
def get_all_alumnos():
    conn = get_db_connection()
    alumnos_rows = conn.execute('SELECT * FROM alumnos').fetchall()
    conn.close()
    alumnos_list = [dict(row) for row in alumnos_rows]
    return jsonify(alumnos_list)

# Endpoint para GET /alumnos por id
@app.route('/alumnos/<int:id>', methods=['GET'])
def get_alumno_by_id(id):
    conn = get_db_connection()
    alumno_row = conn.execute('SELECT * FROM alumnos WHERE id = ?', (id,)).fetchone()
    conn.close()
    if alumno_row is None:
        return jsonify({"error": "Alumno no encontrado"}), 404
    return jsonify(dict(alumno_row))

# Endpoint para POST /alumnos - crear alumno
@app.route('/alumnos', methods=['POST'])
def create_alumno():
    data = request.get_json()
    if not data or 'nombre' not in data or 'apellido' not in data or 'nota' not in data:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO alumnos (nombre, apellido, aprobado, nota, fecha) VALUES (?, ?, ?, ?, ?)',
                   (data['nombre'], data['apellido'], data.get('aprobado', data['nota'] >= 5.0), data['nota'], data.get('fecha', '2024-01-01 00:00:00')))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return jsonify({'id': new_id, **data}), 201

# Endpoint para PUT /alumnos/<id> - actualizar alumno
@app.route('/alumnos/<int:id>', methods=['PUT'])
def update_alumno(id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400
    
    updates = []
    params = []
    for key in data:
        if key in ['nombre', 'apellido', 'nota', 'aprobado']:
            updates.append(f"{key} = ?")
            params.append(data[key])
    
    if not updates:
        return jsonify({"error": "Ningún campo válido para actualizar"}), 400
    
    params.append(id)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"UPDATE alumnos SET {', '.join(updates)} WHERE id = ?", tuple(params))
    conn.commit()
    
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error": "Alumno no encontrado"}), 404
    conn.close()
    return jsonify({"mensaje": "Alumno actualizado correctamente"}), 200

# Endpoint para DELETE /alumnos/<id> - eliminar alumno
@app.route('/alumnos/<int:id>', methods=['DELETE'])
def delete_alumno(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM alumnos WHERE id = ?', (id,))
    conn.commit()
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error": "Alumno no encontrado :("}), 404
    conn.close()
    return jsonify({"mensaje": "Alumno eliminado correctamente"}), 200

if __name__ == '__main__':
    app.run(debug=True)