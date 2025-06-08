# ComputerNetwork-Task1
这是计算机网络课程的课程设计。
## 开始
### 运行环境
Python(>=3.x)
### 安装
```bash
git clone https://github.com/AstrologerLuo/ComputerNetwork-Task1
```
### 文件环境：
文档1的客户端需要一个名为'send.txt'的文本文件作为输入
文档1的客户端会创建一个名为'new.txt'的输出文件
### 端口配置：
reversetcpServer.py的服务器默认监听1616端口
reversetcpClient.py的客户端需要输入服务器IP和端口
### 程序配置：
reversetcpClient.py需要用户输入：
服务器IP地址
服务器端口号
每块数据的最小大小（字节）
每块数据的最大大小（字节）
reversetcpServer.py不需要额外配置，直接运行即可