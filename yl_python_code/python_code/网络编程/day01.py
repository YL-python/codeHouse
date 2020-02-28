import socket


def main():
    # 创建UDP套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 用套接字收发数据
    # 1指定IP 和端口
    dest_addr = ('10.1.0.102', '')
    # 指定发生内容
    send_data = 'nihao'
    # 用 sendto方法发送（发什么，发给谁）
    udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
    print('hello')
