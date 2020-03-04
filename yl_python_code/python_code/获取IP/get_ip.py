import socket


# Windows可用
# localIP = socket.gethostbyname(socket.gethostname())  # 得到本地ip
# print(localIP)

# Windows Linux 都可以用
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


if __name__ == '__main__':
    print(get_host_ip())
