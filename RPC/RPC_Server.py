from socket import *
import json

def HitungPajak(harga):
    return harga*0.1

def server():
    s=socket(AF_INET, SOCK_STREAM)
    s.bind(('localhost', 9000))
    s.listen(1)
    print("Server siap!")
    
    while True:
        try:
            conn, addr=s.accept()
            print(f"Sudah terkoneksi dengan {addr}")
            
            req = conn.recv(1024).decode()
            data = json.loads(req)

            if data["function"] == "HitungPajak":
                harga=data["argumen"]["harga"]
                res=HitungPajak(harga)
            else:
                res="Yaah ga ketemu!"
            
            res_data=json.dumps({"hasil": res})
            conn.send(res_data.encode())
        except Exception as e:
            print("Error nih!")
        finally:
            conn.close()

server()