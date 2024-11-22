from flask import Flask, request, jsonify
import base64
import magic

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.json.get("data", [])
    file_b64 = request.json.get("file_b64", "")

    # Extract numbers and alphabets
    numbers = [int(x) for x in data if x.isdigit()]
    alphabets = [x for x in data if x.isalpha()]
    highest_lowercase = max([x for x in alphabets if x.islower()], default="")

    # Check for prime numbers
    is_prime = any(is_prime_number(n) for n in numbers)

    # File validation
    try:
        decoded_file = base64.b64decode(file_b64)
        file_size_kb = len(decoded_file) / 1024
        mime_type = magic.Magic(mime=True).from_buffer(decoded_file)
        file_valid = True
    except Exception:
        file_valid = False
        mime_type = None
        file_size_kb = 0

    return jsonify({
        "is_success": True,
        "user_id": "ashlesha_saxena_22092001",
        "email": "ashlesha@xyz.com",
        "roll_number": "CSE123",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase,
        "is_prime_found": is_prime,
        "file_valid": file_valid,
        "file_mime_type": mime_type,
        "file_size_kb": file_size_kb
    })

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1})

def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    app.run(debug=True)
