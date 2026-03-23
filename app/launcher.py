import webbrowser
import subprocess
import time

# Start your Flask app
process = subprocess.Popen(["python", "app.py"])

# Wait a moment to let Flask start
time.sleep(2)

# Open the browser
webbrowser.open("http://127.0.0.1:5000")

# Keep the script running until Flask stops
process.wait()
