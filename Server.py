import socket
import webbrowser
import os

#HOST = "127.0.0.1"
#PORT = 65432

#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#    s.bind((HOST, PORT))
#    s.listen()
#    conn, addr = s.accept()
#    with conn:
#        print(f"Connected by {addr}")
#        while True:
#            data = conn.recv(1024)
#            if not data:
#                break
#            conn.sendall(data)

#s = socket.socket()         # Create a socket object
#host = socket.getfqdn() # Get local machine name
#port = 9082
#s.bind((host, port))        # Bind to the port

#print ('Starting server on', host, port)
#print ('The Web server URL for this would be http://%s:%d/' % (host, port))

#s.listen(5)                 # Now wait for client connection.

#print ('Entering infinite loop; hit CTRL-C to exit')
#while True:
    # Establish connection with client.
#    c, (client_host, client_port) = s.accept()
#    print ('Got connection from', client_host, client_port)
#    c.send('Server Online\n')
#    c.send('HTTP/1.0 200 OK\n')
#    c.send('Content-Type: text/html\n')
#    c.send("""
#        <html>
#        <body>
#        <h1>Hello World</h1> this is my server!
#        </body>
#        </html>
#        """)
#    c.send(Crawler)
#    c.close()


# Define socket host and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5001

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()
print('Listening on port %s ...' % SERVER_PORT)

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    # Parse HTTP headers
    headers = request.split('\n')
    filename = headers[0].split()[0]

    # Get the content of the file
    if filename == '/':
        filename = '/UI.html'

    # Get the content of htdocs/index.html
#    fin = open('htdocs/index.html')
#    content = fin.read()
#    fin.close()

    try:
        content = filename
        response = ' HTTP/1.0 200 OK  ' + content
        f = open('UI.html', 'r')
        webbrowser.open_new_tab('UI.html')
    except FileNotFoundError:
        response = ' HTTP/1.0 404 NOT FOUND  File Not Found'

    # Send HTTP response
#    response = 'HTTP/1.0 200 OK\n\n' + content
    client_connection.sendall(response.encode())
    client_connection.close()

# Close socket
server_socket.close()