import socket

socket_client = socket.socket()

socket_client.connect(("localhost", 8888))

while True:
    send_msg = input("请输入要发送的消息：")
    if send_msg == 'exit':
        socket_client.send('exit'.encode("UTF-8"))
        break
    socket_client.send(send_msg.encode("UTF-8"))

    recv_data = socket_client.recv(1024)
    print("服务端回复消息为：", recv_data.decode("UTF-8"))

socket_client.close()

