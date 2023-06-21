import socket
import rsa_helper

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 12346))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            
            public_key_size = int(conn.recv(4).decode())
            public_key = conn.recv(public_key_size).strip()
            
            message_size = int(conn.recv(4).decode())
            message = conn.recv(message_size).decode()
            
            signature_size = int(conn.recv(4).decode())
            signature = conn.recv(signature_size)

            is_valid = rsa_helper.verify_signature(message, signature, public_key)
            print("Gautasis viesasis raktas:", public_key)
            print("Gauta zinute:", message)
            print("Gautas parasas:", signature)
            print(f"Zinute: {message}")
            print(f"Parasas yra: {'valid' if is_valid else 'invalid'}")
            conn.close()

if __name__ == "__main__":
    main()
