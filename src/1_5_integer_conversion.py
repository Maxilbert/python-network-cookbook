import socket


def convert_integer():
    data = 1234745764
    # 32-bit
    print("Original: %s => Network byte order: %s, Long host byte order: %s"
          % (data, socket.htonl(data), socket.ntohl(socket.htonl(data))))
    # 16-bit
    print("Original: %s => Network byte order: %s, Short host byte order: %s"
          % (data, socket.htons(data), socket.ntohs(socket.htons(data))))


if __name__ == '__main__':
    convert_integer()
