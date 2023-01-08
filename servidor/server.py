import os, shutil
import json
import flask
from flask import Flask, json, jsonify
from flask import request
import mmap
import consumer
import threading

app = flask.Flask(__name__)

# run consumer
consumer_thread = threading.Thread(target=consumer.start, name="Consumer")
consumer_thread.start()


@app.route('/sensors', methods=['GET'])
def index():
    with open("sensorcluster_output.json", "rb") as file:
        try:
            file.seek(-2, os.SEEK_END)
            while file.read(1) != b'\n':
                file.seek(-2, os.SEEK_CUR)
        except OSError:
            file.seek(0)
        last_line = json.loads(file.readline().decode())
        last_line['ticket_num'] = sum(1 for line in open('tickets.txt'))
    return last_line

@app.route('/ticket', methods=['POST'])
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

@app.route('/ticket_reset', methods=['GET'])
def reset_ticket():
    with open('all_tickets.txt', 'rb') as f2, open('tickets.txt', 'wb') as f1:
        shutil.copyfileobj(f2, f1)
    return 'success: tickets have been reset'

if __name__ == '__main__':
    app.run()