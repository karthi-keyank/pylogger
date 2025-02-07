import socket
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import os

# Server Config
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65432
BUFFER_SIZE = 1024

# Log File Path
LOG_FILE_PATH = "received_logs/keylogs.txt"

def start_client():
    """Starts the client and continuously receives data from the server."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    with open(LOG_FILE_PATH, "a", encoding="utf-8") as log_file:  # Explicitly using utf-8 encoding
        try:
            while True:
                data = client_socket.recv(BUFFER_SIZE)
                if data:
                    log_file.write(data.decode())  # Write the received data directly to the file
                    log_file.flush()  # Immediately flush the file buffer to disk
                else:
                    break
        except KeyboardInterrupt:
            print("Disconnected from server.")
        finally:
            client_socket.close()

# Background Scheduler for Time Logging
scheduler = BackgroundScheduler()

def append_time():
    """Appends the current timestamp to the log file."""
    with open(LOG_FILE_PATH, "a", encoding="utf-8") as file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n[TIME] {current_time}\n")  # Adding a label for clarity
    print(f"Now time: {current_time}")

# Schedule the append_time function to run every 0.2 minutes
scheduler.add_job(append_time, "interval", minutes= 0.2)

# Start the scheduler before starting the client
scheduler.start()

if __name__ == "__main__":
    start_client()  # This runs independently of the scheduler
