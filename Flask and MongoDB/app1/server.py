from flask import Flask, request, jsonify, render_template
import dotenv
dotenv.load_dotenv()

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    with open('data.csv', 'r') as file:
        data = file.readlines()

    headers = data[0].strip().split(',')
    
    result = []
    for line in data[1:]:
        values = line.strip().split(',')
        result.append(dict(zip(headers, values)))
    
    return result

if __name__ == '__main__':
    # using os to fetech environment variables is not recommended
    app.run(debug=True, host=dotenv.get_key('.env', 'HOST'), port=int(dotenv.get_key('.env', 'PORT')))