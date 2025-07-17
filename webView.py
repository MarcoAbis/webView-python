from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineScript, QWebEngineProfile, QWebEngineSettings
from PyQt5.QtCore import QUrl
from PyQt5.QtNetwork import QSslConfiguration, QSslCertificate, QSslError, QSsl
from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInterceptor
import sys

class CustomWebEnginePage(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)

    def certificateError(self, error):
        print(f"SSL Error: {error.errorDescription()}")
        # Automatically accept self-signed certificates (not recommended for production)
        return True
    
    def createWindow(self, web_window_type):
        """Handle popups or new windows."""
        new_view = QWebEngineView()
        new_view.setPage(CustomWebEnginePage(self.profile()))
        new_view.show()
        return new_view.page()

class BrowserWindow(QMainWindow):
    def __init__(self, url):
        super().__init__()
        self.setWindowTitle("Website Viewer")
        self.setGeometry(100, 100, 1024, 768)  # Set window size

        # Main browser widget
        self.browser = QWebEngineView()
        self.page = CustomWebEnginePage(self.browser.page().profile())
        self.browser.setPage(self.page)
        self.browser.setUrl(QUrl(url))

        # Enable JavaScript and Plugins
        self.browser.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.browser.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)

        # Layout for the browser
        layout = QVBoxLayout()
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Inject JavaScript polyfill for compatibility
        self.inject_js_polyfill()


    def inject_js_polyfill(self):
        """Inject JavaScript polyfills for modern compatibility."""
        script_source = """
        // Polyfill for String.prototype.replaceAll
        if (!String.prototype.replaceAll) {
            String.prototype.replaceAll = function(search, replacement) {
                const target = this;
                return target.split(search).join(replacement);
            };
        }

        // Polyfill for Object.hasOwn
        if (!Object.hasOwn) {
            Object.hasOwn = function(obj, prop) {
                return Object.prototype.hasOwnProperty.call(obj, prop);
            };
        }
        // Polyfill for Array.prototype.at
        if (!Array.prototype.at) {
            Array.prototype.at = function(n) {
                n = Math.trunc(n) || 0;
                if (n < 0) n += this.length;
                if (n < 0 || n >= this.length) return undefined;
                return this[n];
            };
        }
        """
        script = QWebEngineScript()
        script.setSourceCode(script_source)
        script.setInjectionPoint(QWebEngineScript.DocumentReady)
        script.setWorldId(QWebEngineScript.MainWorld)
        script.setRunsOnSubFrames(True)

        profile = QWebEngineProfile.defaultProfile()
        profile.scripts().insert(script)

    def closeEvent(self, event):
        """Ensure proper cleanup when the window is closed."""
        self.browser.setPage(None)
        self.browser.deleteLater()  # Clean up browser widget
        self.page.deleteLater()  # Clean up the page object
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    url = "https://<url>"  # Replace with your URL
    window = BrowserWindow(url)
    window.show()
    sys.exit(app.exec_())
