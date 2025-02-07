# Keylogger with Client-Server Architecture

This project implements a **keylogger** with a **client-server architecture**. The **server** listens for key presses on the host machine and sends the recorded keystrokes to the **client**, which logs them into a file. 

## ⚠️ Disclaimer

This project is intended **strictly for educational and ethical purposes**. Unauthorized keylogging is **illegal** and may violate privacy laws. **Use this project only on machines you own or have explicit permission to monitor.** The author is not responsible for any misuse.

---

## 📌 Features

- **Remote Key Logging** – Captures keystrokes on the **server** and sends them to the **client**.
- **Persistent Connection** – Reconnects automatically when the client disconnects.
- **Logs with Timestamp** – The client appends a timestamp every 12 seconds for reference.
- **Background Logging** – Uses **APScheduler** to log time without interrupting key capture.
- **Handles Special Keys** – Maps keys like **Enter, Backspace, Shift, Ctrl**, etc.

---

## 📜 How It Works

### 🖥️ **Server (Keylogger)**
1. Listens for a client connection.
2. Captures **keystrokes** using `pynput`.
3. Sends keystrokes to the connected client.
4. If the client disconnects, it waits for reconnection.

### 📡 **Client (Logger)**
1. Connects to the server.
2. Continuously **receives keystrokes** and writes them to a file (`keylogs.txt`).
3. Uses `APScheduler` to log the current **timestamp** every 12 seconds.
4. Closes the connection gracefully on exit.

---

## 🛠️ Installation

### **1️⃣ Install Dependencies**
Ensure you have **Python 3.x** installed. Then, install the required Python modules:

```sh
pip install pynput apscheduler

### Third-Party Libraries  
| Module | Version | Description |
|--------|---------|-------------|
| `APScheduler` | 3.11.0 | Used to schedule tasks in the background. |
| `MouseInfo` | 0.1.3 | Provides mouse-related information. |
| `PyAutoGUI` | 0.9.54 | Used for GUI automation, including taking screenshots. |
| `PyGetWindow` | 0.0.9 | Used to get window-related details. |
| `PyMsgBox` | 1.0.9 | Provides message box functionality. |
| `pynput` | 1.7.7 | Captures keyboard and mouse input. |
| `pyperclip` | 1.9.0 | Handles clipboard operations. |
| `PyRect` | 0.2.0 | Handles rectangular region calculations. |
| `PyScreeze` | 1.0.1 | Provides screenshot functionality. |
| `pytweening` | 1.2.0 | Used for animations and easing functions. |
| `six` | 1.17.0 | Provides compatibility between Python 2 and 3. |
| `tzdata` | 2025.1 | Handles timezone data. |
| `tzlocal` | 5.2 | Detects the local timezone. |


