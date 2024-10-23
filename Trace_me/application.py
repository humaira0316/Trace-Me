from flask import Flask, request, jsonify
import sqlite3
from face_utils import encode_image, compare_faces

app = Flask(__name__)

@app.route('/register_missing', methods=['POST'])
def register_missing():
    name = request.form['name']
    age = request.form['age']
    description = request.form['description']
    image = request.files['image']
    
    # Save the image and encode it
    image_path = f'uploads/{name}.jpg'
    image.save(image_path)
    face_encoding = encode_image(image_path)

    if face_encoding is None:
        return jsonify({'message': 'No face detected in the image'}), 400

    # Store data in database
    conn = sqlite3.connect('traceme.db')
    c = conn.cursor()
    c.execute("INSERT INTO missing_persons (name, age, photo, description) VALUES (?, ?, ?, ?)", 
              (name, age, face_encoding.tobytes(), description))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Missing person registered successfully'})

@app.route('/search_missing', methods=['POST'])
def search_missing():
    image = request.files['image']
    image_path = 'uploads/search_image.jpg'
    image.save(image_path)

    conn = sqlite3.connect('traceme.db')
    c = conn.cursor()
    c.execute("SELECT id, name, photo FROM missing_persons")
    results = c.fetchall()

    for person in results:
        person_id, name, photo = person
        known_encoding = np.frombuffer(photo, dtype=np.float64)
        if compare_faces(known_encoding, image_path):
            return jsonify({'message': f'Match found: {name}'})
    
    return jsonify({'message': 'No match found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
