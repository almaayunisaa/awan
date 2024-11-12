from socket import *
import json

def RPC(function, argumen):
    cs=socket(AF_INET, SOCK_STREAM)
    cs.connect(('localhost', 9000))

    reqData=json.dumps({"function":function, "argumen":argumen})

    cs.send(reqData.encode())

    res=cs.recv(1024).decode()
    resData=json.loads(res)
    cs.close()

    return resData.get("hasil")

harga=10000
hasil=RPC("HitungPajak", {"harga":harga})
print(f"Pajak dari {harga}: {hasil}")