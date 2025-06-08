import socket
import threading
import struct

def handle_client(conn, addr):
    init = conn.recv(6)
    init_data, n = struct.unpack('>HI', init)
    if init_data != 1:
        print(f"{addr}的initialization报文错误")
        conn.close()
        return
    agree=struct.pack('>H',2)
    conn.sendall(agree)
    for i in range(n):
        req=conn.recv(6)
        req_type,req_len=struct.unpack('>HI',req)
        if req_type!=3:
            print(f"{addr}的reserveRequest报文错误")
            conn.close()
            return
        req_data=conn.recv(req_len)
        req_str=req_data.decode('UTF-8')#变为UTF-8编码的字符串
        ans_str=''.join(reversed(req_str)) #翻转
        ans_data=ans_str.encode('UTF-8')#翻转之后再变为bytes
        header=struct.pack('>HI',4,req_len)
        ans=header+ans_data
        conn.sendall(ans)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 1616))#绑定到 所有 IPv4 地址
server.listen(5)
print("服务器启动，等待连接...")
while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))#线程要执行的函数  传给函数的参数
    thread.start()
    print(f"活跃连接数: {threading.active_count() - 1}")