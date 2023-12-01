import csv
import socket
import pandas as pd
import threading
from enum import Enum
from config import *
from io import StringIO

df = pd.read_csv(FILE_PATH)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

server_adress = ('localhost',81)

SIZE = 10000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(server_adress)

s.listen(5)

print ('Waiting for connection')


while 1:
    client, client_address = s.accept()
    print ('Connected from : ', client_address)

    df = pd.read_csv(FILE_PATH)
    df = df.to_csv(index=False).strip('\n').split('\n')
    df_string = '\r\n'.join(df)
    # print(df_string)
    client.send(df_string.encode('utf8'))    
    try:
        message = client.recv(SIZE)
        message = message.decode()
        df = pd.read_csv(StringIO(message),sep=',')

        df.to_csv(FILE_PATH, index=False)
    except:
        pass
    

s.close()