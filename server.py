import socket

#noinspection PyBroadException

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
phone.bind(('127.0.0.1', 8000))
phone.listen(5)
print('------')
while True:
    conn, addr = phone.accept()
    print('电话线路是', conn)
    print('客户端的手机号是', addr)
    while True:
        # noinspection PyBroadException
        try:
            msg = conn.recv(1024)
            if not msg:
                break
            print('client：    ', msg.decode('utf-8'))
            conn.send(input('>>>:').strip().encode('utf-8'))
        except Exception:
            break
    conn.close()
phone.close()







