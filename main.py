import requests
from bs4 import BeautifulSoup
from pathlib import Path


#Get url from user
print("Enter URL:")
url = input() + ".json"

#Set a user-agent header to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# download the JSON data from the URL
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Converts the JSON string automatically into a Python dictionary
    data = response.json()
    #Get the title of the post and the post stream
    post_title = data.get("title")
    post_stream = data.get("post_stream", {})
    posts = post_stream.get("posts", [])

    first_post = posts[0]
    #Html for OP 
    cooked_html = first_post.get("cooked", "")
    # Feed the string to BeautifulSoup
    soup = BeautifulSoup(cooked_html, "html.parser")

    #Images are stored in Lightbox links
    lightbox_links = soup.find_all("a", class_="lightbox")

    #Store image URLs and names in a list of dictionaries
    imgs = [
            {"name": link.get("title") or link.get("aria-label") or "Unnamed Image", "url": link["href"]}
            for link in soup.find_all("a", class_="lightbox", href=True)
        ]

    #Grab gif URLs and names and store in list
    animated_links = soup.find_all("img", class_="animated")

    #Store gif URLs and names in a list of dictionaries
    gifs = [
        {"name": img.get("alt", "Unnamed GIF"), "url": img["src"]}
        for img in soup.find_all("img", class_="animated", src=True)
    ]

    #Create Directory
    folder_path = Path('C:/Users/obi/Documents/ForumDownloader/' + post_title)
    folder_path.mkdir(parents=True, exist_ok=True)

    #Download images
    for img in imgs:
            img_name = img['name']

            #Inital file path
            complete_path = folder_path / f"{img_name}.png"

            #Check if the file already exists and if so, append a counter to the filename
            counter = 1
            while complete_path.exists():
                complete_path = folder_path / f"{img_name}_{counter}.png"
                counter += 1

            #Download the image and save it to the specified path
            current_img = requests.get(img['url'])
            with open(complete_path, "wb") as file:
                 file.write(current_img.content)

    #Download gifs only if they exist
    if len(gifs) > 0:
         for gif in gifs: 
            gif_name = gif['name']

            #Inital file path
            complete_path = folder_path / f"{gif_name}.gif"
            
            # Check if the file already exists and if so, append a counter to the filename
            counter = 1
            while complete_path.exists():
                complete_path = folder_path / f"{gif['name']}_{counter}.gif"
                counter += 1

            #Download the gif and save it to the specified path
            current_gif = requests.get(gif['url'])
            with open(complete_path, "wb") as file:
                            file.write(current_gif.content)      

    #Output the number of images and gifs downloaded
    print(f"Downloaded {len(imgs)} images and {len(gifs)} GIFs")
else:
    #Output an error message if the request failed
    print(f"Failed to fetch data: {response.status_code}")