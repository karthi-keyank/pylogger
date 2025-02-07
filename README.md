# 🖥️ Keylogger & Screenlogger (Client-Server)

This project consists of two tools:  

- **🔑 Keylogger**: Captures keystrokes from a remote machine and logs them.  
- **🖼️ Screenlogger**: Captures and transmits screenshots from a remote machine.  

Both use a **client-server architecture** for remote monitoring.  

---

## ⚠️ Disclaimer

**This project is strictly for educational and ethical use only.** Unauthorized use for spying or stealing data is illegal and punishable by law. Ensure you have **explicit permission** before using it.  

---

## 📌 Features

✅ **Keylogger:**  
- Captures all keystrokes, including special keys.  
- Saves keystrokes in `keylogs.txt` on the client side.  
- Automatically reconnects if the client disconnects.  
- Uses `APScheduler` to log timestamps.  

✅ **Screenlogger:**  
- Captures periodic screenshots from the remote machine.  
- Saves screenshots in `received_screenshots/` folder.  
- Ensures smooth transmission by handling network errors.  
- Supports multiple client connections.  

---

## 📜 How It Works  

### **1️⃣ Keylogger**  

#### 🖥️ **Server (Keylogger Machine)**  
- Listens for incoming client connections.  
- Captures and transmits keystrokes.  

#### 📡 **Client (Logger Machine)**  
- Connects to the server and receives keystrokes.  
- Logs the data in `keylogs.txt`.  
- Adds timestamps at regular intervals.  

---

### **2️⃣ Screenlogger**  

#### 🖥️ **Server (Screenshot Capturer)**  
- Captures screenshots periodically.  
- Sends screenshots to the connected client.  

#### 📡 **Client (Screenshot Receiver)**  
- Connects to the server and downloads images.  
- Saves images in `received_screenshots/`.  

---

## 🛠️ Installation  

### **1️⃣ Install Dependencies**  
Ensure you have **Python 3.x** installed. Then install the required modules:  


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


