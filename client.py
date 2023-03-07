import socket
import threading #for performing various tasks at the same time.


# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Close Connection When Error
            # print("An error occured!")
            client.close()
            break


# Sending Messages To Server
def write():
    while True:
        a = input('')
        if a=="exit":
        	client.close()
        	break
        message = '{}: {}'.format(nickname,a)
        client.send(message.encode('ascii'))
    	
'''# Sending Messages To Server
def write():
    while True:
    	a = input('')
    	if a=="exit":
    		print("left")
    		message = '{}: {}'.format(nickname,a)
    		client.send(message.encode('ascii'))
    		client.close()
    		return
    	message = '{}: {}'.format(nickname,a)
    	client.send(message.encode('ascii'))'''


# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()


