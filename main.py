from flask import Flask, render_template
import os

app = Flask(__name__)


def list_file_name(file_dir):
    file_pre = "http://localhost"
    file_list = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            file_data = {}
            file_data['pre'] = file_pre
            file_data['file_name'] = file
            file_list.append(file_data)
        return file_list

@app.route("/")
def hello():
    file_path = "D:\work_idea\games-server"
    return render_template('index.html', file_list=list_file_name(file_path))

if __name__ == "__main__":
    app.run(debug=True, port=8003)