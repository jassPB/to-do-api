from flask import Flask, jsonify
from task import task

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({
        "message": "pong"
    })

@app.route('/tasks')
def get_tasks():
    return jsonify({
        "tasks": task
    })

if __name__ == '__main__':
    app.run(debug=True, port=4000)

