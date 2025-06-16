🖼️ Snipping Tool with Google Reverse Image Search
A simple Python application that lets you take a screenshot snip of your screen and automatically performs a reverse image search on Google using Selenium.

🚀 Features
Fullscreen snipping overlay for custom region selection

Automatically saves the snipped image as snip.png

Launches Google Images and uploads the image for reverse image search

Lightweight PyQt5 GUI

🧰 Requirements
Python 3.x

Google Chrome installed

ChromeDriver (compatible with your version of Chrome)

Python Packages
Install the required packages using pip:

bash
Copy
Edit
pip install PyQt5 pillow selenium
✅ Make sure chromedriver.exe is in the same directory as your script or added to your system PATH.

📸 How It Works
Run the script.

The screen will dim and allow you to draw a rectangle.

After releasing the mouse button, it:

Crops the selected region

Saves it as snip.png

Opens Google Images

Uploads the image for reverse search

Browser window will stay open for 30 seconds (can be modified).

🧪 Usage
bash
Copy
Edit
python snipping_tool.py
Press any key to cancel the snip and close the tool.

Mouse click and drag to define the region.

🛠️ Notes
This tool is intended for educational/demonstration purposes.

It uses Selenium to control a browser — this may be fragile if Google updates their UI.

The script uses a 30-second pause to keep the browser open. You can replace time.sleep(30) with a better wait strategy if desired.

📂 File Structure
bash
Copy
Edit
.
├── snipping_tool.py     # Main application
├── chromedriver.exe     # ChromeDriver (must match your Chrome version)
├── screenshot.png       # Temporary full-screen screenshot
└── snip.png             # Your selected cropped image
🧹 To-Do / Improvements
Automatically close browser after result loads

Add file format options (e.g., JPG)

Add a better way to wait for the search results

Add GUI for showing the result directly

📝 License
MIT License — free to use and modify.

