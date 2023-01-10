#import libraries
import cv2
from pyzbar import pyzbar

import time 
import json 
import random 
from datetime import datetime
#from data_generator import generate_message
from kafka import KafkaProducer
import sys
import requests

bus_id = '81'
old_barcode_info = ''
resp = ''

# Messages will be serialized as JSON 
def serializer(message):
    return json.dumps(message).encode('utf-8')

def post_qr(code):
    url='https://pg50670-38o1253pnu72raw1.socketxp.com/ticket'
    #url='http://0.0.0.0:5000/ticket'
    data={'bus_id': bus_id,'codes': code}
    print('Sending code: '+code)
    r = requests.post(url, data = data)
    print(r.status_code)
    return r.status_code

def read_barcodes(frame):
    global old_barcode_info, resp
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        barcode_info = barcode.data.decode('utf-8')
        if barcode_info != old_barcode_info:
            old_barcode_info = barcode_info
            resp = post_qr(barcode_info)
        else:
            cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            if resp == 200:
                #cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)        
                cv2.putText(frame, 'SUCESSO', (x + 6, y - 6), font, 2.0, (0, 255, 0), 1)
            elif resp == 403:
                #cv2.putText(frame, 'Bilhete Invalido', (x + 6, y - 6), font, 2.0, (50, 50, 255), 1)        
                cv2.putText(frame, 'ERRO', (x + 6, y - 6), font, 2.0, (0, 0, 255), 1)
            elif resp == 400:
                #cv2.putText(frame, 'Bilhete nao Encontrado', (x + 1, y - 1), font, 0.4, (50, 50, 255), 1)        
                cv2.putText(frame, 'ERRO', (x + 6, y - 6), font, 2.0, (0, 0, 255), 1)
    return frame

def main():
    #1
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    #2
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow('bhus - Validador de Bilhete QR Code', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    #3
    camera.release()
    cv2.destroyAllWindows()
    
#4
if __name__ == '__main__':
    main()