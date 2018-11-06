import socket
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5


def echo_server(port):
    """ A simple echo server """
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Enable reuse address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, port)
    print("Starting up server on %s:%s" % server_address)
    sock.bind(server_address)
    # Listen to clients, backlog arguments specifies the max no. of queued connections
    sock.listen(backlog)
    sock.settimeout(10)
    while True:
        try:
            print("Waiting to receive message from client")
            client, address = sock.accept()
            data = client.recv(data_payload)
            if data:
                print("Data: %s" % data.decode())
                client.send(data)
                print("Sent %s bytes back to %s" % (data, address))
            # End connection
            client.close()
        except socket.error:
            continue
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument("--port", action="store", dest="port", type=int, required=True)
    args = parser.parse_args()
    port = args.port
    echo_server(port)
