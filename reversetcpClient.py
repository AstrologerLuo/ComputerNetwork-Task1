import socket
import random
import struct
server_ip = input("Server ip: ")
server_port = int(input("Server port: "))
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))
f = open('send.txt', 'rb')
new_f=open("new.txt","w",encoding="utf-8")
chunk_num=0   #块的数目
chunks=[]       #块的内容形成的列表
chunks_len=[]   #每一块的大小
lmin=int(input("请输入一块的最小值（单位B）："))
lmax=int(input("请输入一块的最大值（单位B）："))
while True:
    chunk_size=random.randint(lmin,lmax)
    chunk=f.read(chunk_size)
    if not chunk:
        break
    real_len=len(chunk)#最后一块可能小于chunk_size
    chunks_len.append(real_len)
    chunks.append(chunk)
    chunk_num+=1
initialization=struct.pack('>HI',1,chunk_num)   #大端序也就是网络序
client.sendall(initialization)
agree_data = client.recv(2)
agree = struct.unpack('>H', agree_data)[0] #返回的是元组,[0]提取其中第一个值
if agree != 2:
    raise ValueError("没有收到agree报文")#主动报错并终止程序
ans_total=''
for i in range(0,chunk_num):
    header=struct.pack('>HI',3,chunks_len[i])
    send_data=header+chunks[i]
    client.sendall(send_data)
    reverse=client.recv(6+chunks_len[i])
    reverse_header=struct.unpack('>HI', reverse[:6])
    if reverse_header[0] != 4:
        raise ValueError("接收到reverseAnswer报文错误") #主动报错并终止程序
    reverse_data=reverse[6:6+chunks_len[i]]
    ans_str=reverse_data.decode('utf-8')
    ans_total = ans_str + ans_total
    print(f'第{i+1}块：{ans_str}')
ans_total = ''.join(line  # 保留的每一行内容
                    for line in ans_total.splitlines(keepends=True)  # 按行分割（保留换行符）
                    if line.strip()) # 只保留非空行（去除纯空白字符的行） line.strip() 返回空字符串 ""，则 if 条件为 False，该行被过滤。
new_f.write(ans_total)
input("点击回车结束结束")
f.close()
new_f.close()
client.close()