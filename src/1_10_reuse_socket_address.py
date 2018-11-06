import socket


def reuse_socket_addr():
    local_port = 8282

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("", local_port))
    srv.listen(1)
    while True:
        try:
            connection, addr = srv.accept()
            print("Connected b7 %s:%s" % (addr[0], addr[1]))
        except KeyboardInterrupt:
            break
        except socket.error as msg:
            print("%s" % msg)


if __name__ == '__main__':
    reuse_socket_addr()