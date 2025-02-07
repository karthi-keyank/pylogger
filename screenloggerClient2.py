import socket
import os
from datetime import datetime

# Server Configuration
SERVER_IP = '127.0.0.1'  # Change to server IP if needed
SERVER_PORT = 12345
SAVE_FOLDER = "received_screenshots"

# Ensure the save directory exists
if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

def receive_screenshot():
    """Connects to the server, receives a screenshot, and saves it."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((SERVER_IP, SERVER_PORT))
            print("[+] Connected to server")

            while True:
                try:
                    # Receive image size first (4 bytes)
                    img_size_data = client.recv(4)
                    if not img_size_data:
                        break  # Connection closed by server
                    
                    img_size = int.from_bytes(img_size_data, 'big')

                    # Receive image data
                    img_data = b''
                    while len(img_data) < img_size:
                        packet = client.recv(img_size - len(img_data))
                        if not packet:
                            break
                        img_data += packet

                    # Save the image with datetime format
                    filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + ".png"
                    file_path = os.path.join(SAVE_FOLDER, filename)

                    with open(file_path, 'wb') as img_file:
                        img_file.write(img_data)
                    
                    print(f"[+] Screenshot saved: {file_path}")

                except ConnectionResetError:
                    print("[!] Server disconnected. Exiting...")
                    break

                except KeyboardInterrupt:
                    print("Disconnected from server.")
                    break

                except Exception as e:
                    print(f"Error: {e}")
                    break

    except ConnectionRefusedError:
        print("[!] Unable to connect to the server. Is it running?")
    finally:
        print("[-] Connection closed")

if __name__ == "__main__":
    receive_screenshot()
