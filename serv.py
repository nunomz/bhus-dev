import os
import json
import flask

# A simple Flask App which takes
# a user's name as input and responds
# with "Hello {name}!"

app = flask.Flask(__name__)

@app.route('/sensors', methods=['GET', 'POST'])
def index():
    #message = ''
    if flask.request.method == 'GET':
        #message = 'Hello ' + flask.request.form['name-input'] + '!'
        with open("sensorcluster_output.json", "rb") as file:
            try:
                file.seek(-2, os.SEEK_END)
                while file.read(1) != b'\n':
                    file.seek(-2, os.SEEK_CUR)
            except OSError:
                file.seek(0)
            last_line = json.loads(file.readline().decode())
            
    return last_line

if __name__ == '__main__':
    app.run()