# Goals
# Pull youtube video, later any supplied video via link, off web and download: urllib.request, urlretrieve
# Convert youtube video to audio if needed: ffmpeg?
# Create transcript, spit out to text file

# Features
# Download progress bar: https://stackoverflow.com/questions/37748105/how-to-use-progressbar-module-with-urlretrieve
# Keyword searcher, search bar in UI that looks for keywords/phrases automatically, like "wheat" and extract all sentences that have that word/phrase

# Goals 2
# Worksheet solver, extract questions from word doc(not possible directly cause school filter), and search results on web, or extract from transcripted video

# Features 2 
# Create flashcards based off answers
# Automatic worksheet checker, i.e web bot that looks at canvas posts, downloads files in them, and automatically attempts above(never gonna work)

# Modules
# main.py - UI
# ui.py - UI Class/Format
# scribe.py - Download and transcribe provided URL's
# clerk.py - Manage keyword/phrase searching, automatic answering module
# monitor.py - Watch canvas posts and send potential worksheets to scribe.py

if __name__ == "__main__":
    print("main")

