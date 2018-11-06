import sys
import socket
import argparse


def main():
    # setup argument parsing
    parser = argparse.ArgumentParser(description='Socket Error Examples')
    parser.add_argument('--host', action="store", dest="host", required=False)
    parser.add_argument('--port', action="store", dest="port", type=int, required=False)
    parser.add_argument('--file', action="store", dest="file", required=False)
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file

    # First try-except block -- create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
    except socket.error as e:
        print("Error creating socket: %s" % e)
        sys.exit(1)

    # Second try-except block -- connect to given host/port
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print("Address related error connecting to server: %s" % e)
        sys.exit(2)
    except socket.error as e:
        print("Connection error: %s" % e)
        sys.exit(3)

    # Third try-except block -- sending data
    try:
        s.sendall(("GET %s HTTP/1.0\r\n\r\n" % filename).encode('utf-8'))
    except socket.error as e:
        print("Error sending data: %s" % e)
        sys.exit(4)

    while True:
        # Forth try-except block -- waiting to receive data from remote host
        try:
            buf = s.recv(2048)
        except socket.error as e:
            print("Error receiving data: %s" % e)
            sys.exit(5)
        # write the received data
        if len(buf) != 0:
            print(buf.decode('utf-8'))
            break


# python 1_7_socket_errors.py --host=www.python.org --port=80 --file=1_7_socket_errors.py
if __name__ == '__main__':
    main()
