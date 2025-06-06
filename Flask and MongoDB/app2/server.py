from flask import Flask, redirect, request, jsonify, render_template
import pymongo
import dotenv

app = Flask(__name__)

client = pymongo.MongoClient(dotenv.get_key('.env', 'MONGO_URI'))
db = client.test
collection = db['data']
host = dotenv.get_key('.env', 'HOST')
port = int(dotenv.get_key('.env', 'PORT'))

@app.route('/submit', methods=['POST'])
def submit_data():
    try:
        username = request.json.get('username')
        email = request.json.get('email')

        collection.insert_one({
            'username': username,
            'email': email
        })

        return render_template('success.html'), 200
    except Exception as e:
        return redirect('/?error=' + str(e), code = 303)
    
@app.route('/')
def index():
    error = request.args.get('error')

    return render_template('index.html', error=error)
    
if __name__ == '__main__':
    app.run(debug=True, host=host, port=port)