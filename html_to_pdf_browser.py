import webbrowser
import time
import os
from pathlib import Path

# Get the absolute path to the HTML file
html_file = Path("e:/Major-Project/base_paper_recommendation.html").absolute()
html_url = html_file.as_uri()

print(f"Opening HTML file in browser: {html_url}")
print("\nInstructions:")
print("1. The HTML file will open in your default browser")
print("2. Press Ctrl+P to open the print dialog")
print("3. Select 'Save as PDF' as the printer")
print("4. Save it as 'base_paper_recommendation.pdf'")
print("\nOpening browser in 3 seconds...")

time.sleep(3)
webbrowser.open(html_url)

print("Browser opened! Use Ctrl+P to print to PDF.")
