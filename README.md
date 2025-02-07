# Keylogger and Screenshot Logger  

## Overview  
A **Keylogger** is a tool that records keystrokes made by a user on a keyboard. It is often used for monitoring and security purposes.  
A **Screenshot Logger** is a program that captures screenshots at regular intervals to monitor user activity on a system.  

These tools can be used for ethical monitoring, such as parental control or employee surveillance, but they must be used responsibly and legally.  

## Modules Used  
The following Python modules are required to implement a keylogger and screenshot logger:  

### Standard Libraries  
- `socket` – Used for network communication.  
- `os` – Used for file operations.  
- `datetime` – Used to fetch the current time and date.  

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

## Implementation  
To implement a **Keylogger and Screenshot Logger**, the following steps are typically followed:  
1. **Keystroke Logging** – Capture keyboard inputs using `pynput`.  
2. **Screenshot Capturing** – Take periodic screenshots using `PyAutoGUI`.  
3. **Data Storage** – Save logs and screenshots locally or send them over a network.  
4. **Task Scheduling** – Use `APScheduler` to automate logging at intervals.  

## Ethical Considerations  
- Always **obtain consent** before using keyloggers or screenshot loggers.  
- Ensure that it is used for **legal purposes** only.  
- Do not misuse these tools for **unauthorized access or data theft**.  

## Example Code Snippet  
Below is an example of scheduling a screenshot logger using `APScheduler`:  

