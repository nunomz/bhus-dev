import os
import json
import flask
from flask import Flask, json, jsonify
from flask import request
import mmap
#from flask_limiter import Limiter
#from flask_limiter.util import get_remote_address

app = flask.Flask(__name__)

#limiter = Limiter(
#    app=app,
#    key_func=get_remote_address,
#    default_limits=["1 per second"]
#)

@app.route('/sensors', methods=['GET'])
def index():
    #if flask.request.method == 'GET':
    with open("sensorcluster_output.json", "rb") as file:
        try:
            file.seek(-2, os.SEEK_END)
            while file.read(1) != b'\n':
                file.seek(-2, os.SEEK_CUR)
        except OSError:
            file.seek(0)
        last_line = json.loads(file.readline().decode())
    return last_line

@app.route('/ticket', methods=['POST'])
#@limiter.limit("10/second")
def check_ticket():
    print(request)
    bcode = request.form.get('codes').encode('utf-8') 
    with open("tickets.txt", "r+b", 0) as file,\
        mmap.mmap(file.fileno(), 0) as s:
        #https://stackoverflow.com/questions/4940032/how-to-search-for-a-string-in-text-files
        index = s.find(bcode)
        if index != -1:
            print('true')
            resp= jsonify({'message': 'Success'})
            resp.status_code = 200
            #ideia: fazer producer que vai enviar "sucesso" para a app (consumer) aqui
            # ty chatgpt
            end_of_line = s.find(b'\n', index)
            line_length = end_of_line - index
            s.move(index, end_of_line+1, s.size() - (end_of_line+1))
            s.resize(s.size() - line_length)
            s.close()
            return resp
        else:
            print('ticket not found')
            resp= jsonify({'message': 'Error: Ticket Code Not Found'})
            resp.status_code = 403
            s.close()
            return resp

@app.route('/ticket_count', methods=['GET'])
def count_lines():
    num_lines = sum(1 for line in open('tickets.txt'))
    return str(num_lines)

if __name__ == '__main__':
    app.run()