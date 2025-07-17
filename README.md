# PyQt5 WebEngine Viewer

A lightweight, customizable web viewer built with PyQt5's QWebEngine module. 
This application is designed to provide a secure and flexible browsing solution with features like SSL certificate integration, advanced HTTP/HTTPS request interception, and JavaScript polyfills for modern web compatibility.  

---

## 🔑 Key Features

- **Custom SSL Certificate Support**  
  Securely load and integrate custom SSL certificates for enhanced security.   

- **JavaScript Polyfills**  
  Automatically injects polyfills to ensure compatibility with modern websites. <br>

- **Advanced Request Monitoring**  
  Intercept and monitor HTTP/HTTPS requests directly from the application.   

- **Popup Handling**  
  Seamlessly manage popups and new window requests.   

- **Standalone Executable**  
  Convenient `.exe` version for quick setup and deployment.   

⚠️ Most Web Admin Panels don't allow to connect because of the old javasript versions of Chromium.⚠️

---

## 🚀 Getting Started

### 🐍 Setting Up the Python Environment  

1. **Ensure Python is Installed**  
   - Download and install Python (3.9+ recommended) from [python.org](https://www.python.org).  

2. **Create a Virtual Environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/MarcoAbis/webview-python.git
   cd webview-python
   
2. **Install the dependencies**
   ```bash
   pip install PyQt5 PyQtWebEngine
   
3. **Run the application**
   ```bash
   python3 main.py
