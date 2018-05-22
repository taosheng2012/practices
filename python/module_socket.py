import socket

# ****************************************************************************

host = "www.baidu.com"
port = 80

with socket.create_connection((host, port)) as my_socket:
    num_send = my_socket.send(b"Hello. What's your name?")
    data = my_socket.recv(4096)
    print(num_send, data)


print(my_socket)


# fqdn_host=socket.getfqdn(host)
# fqdn=socket.getfqdn()
# print(fqdn)
