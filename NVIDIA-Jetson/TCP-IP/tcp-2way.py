## Temporary live data collection for testing
import socket
import numpy as np

socket.gethostname()
srx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srx.bind(("0.0.0.0", 2025))
srx.listen(5)

stx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
stx.bind(("0.0.0.0", 2027))
stx.listen(5)

client_rx, address = srx.accept()
client_tx, address = stx.accept()
client_tx.send(bytes("connected", "utf-8"))

print(address)

Data = []
for i in range(10000):
    msg = client_rx.recv(40).decode("utf-8").split(";")[0].split(',')

    try:
        j, q, w = float(msg[0]), float(msg[1]), float(msg[2])
        if j!=0: 
            Data.append([i, j, q, w])
            client_tx.send(bytes(f"  {int(j)}, {int(q*100)};", "utf-8"))
            print(f"{j}: {Data[-1]}", end='\r')
    except: pass

np.save('data-100hz', Data)
print(len(Data), Data[-1])
