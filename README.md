# CandidGirls.io Media Downloader

A Python script that easily downloads all images and GIFs from the original post (OP) of a forum thread. This tool leverages the `.json` endpoint (common in Discourse-based forums) to fetch the post data and intelligently extract media elements.

## Features
- **Automatic Folder Creation**: Creates a new folder automatically named after the forum post's title.
- **Targeted Media Extraction**: Specifically targets images within `lightbox` links and `animated` GIFs, ignoring unnecessary web elements.
- **Collision Prevention**: Automatically renames files (e.g., `image_1.png`) if a file with the exact same name already exists in the destination folder.
- **Interactive Prompts**: Simple command-line prompts ask for the URL and save directory.

## Prerequisites
Ensure you have Python 3 installed. You will also need to install the required external libraries: `requests` and `beautifulsoup4`.

You can install these dependencies using `pip`:

```bash
pip install requests beautifulsoup4
```

## Usage
1. Run the script using Python:
   ```bash
   python script_name.py
   ```
2. **Enter URL**: When prompted, enter the URL of the forum post. *(Note: The script automatically appends `.json` to the URL, so just provide the standard web URL).*
3. **Enter Save Location**: Provide the absolute path where you want the media saved (e.g., `C:\Users\YourName\Documents\ForumDownloader`).
4. The script will fetch the thread, parse the first post, download all found media, and output a summary of what was downloaded (e.g., `Downloaded 5 images and 2 GIFs`).

## How it Works
1. **Fetching**: Retrieves the JSON representation of the thread using a standard `User-Agent` to avoid blocks.
2. **Parsing**: Uses `BeautifulSoup` to parse the rendered HTML (`cooked` content) of the thread's first post.
3. **Downloading**: Iterates through links with the `lightbox` class for standard images and `img` tags with the `animated` class for GIFs, saving them securely to your local drive using `pathlib`.
