import requests
from PIL import Image, ImageDraw, ImageFont
import random
import os

# Function to generate a random image
def generate_image(width, height):
    # Create a new blank image
    image = Image.new("RGB", (width, height), "white")
    # Create a drawing object
    draw = ImageDraw.Draw(image)
    # Draw random shapes on the image
    for _ in range(50):
        shape = random.choice(['rectangle', 'ellipse'])
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        if shape == 'rectangle':
            draw.rectangle([x1, y1, x2, y2], fill=color)
        elif shape == 'ellipse':
            draw.ellipse([x1, y1, x2, y2], fill=color)
    return image

# Function to upload image to Imgur
def upload_to_imgur(image_path):
    client_id = "YOUR_CLIENT_ID"  # Replace with your Imgur API client ID
    url = "https://api.imgur.com/3/upload"
    headers = {'Authorization': f'Client-ID {client_id}'}
    files = {'image': open(image_path, 'rb')}
    response = requests.post(url, headers=headers, files=files)
    data = response.json()
    if response.status_code == 200:
        return data['data']['link']
    else:
        return None

# Function to generate random text
def generate_text():
    # You can use any text generation method here
    return "This is a randomly generated text."

# Main function
def main():
    # Generate image
    image = generate_image(500, 500)
    # Save the image
    image_path = "random_image.png"
    image.save(image_path)
    # Upload image to Imgur
    imgur_link = upload_to_imgur(image_path)
    if imgur_link:
        print("Image uploaded to Imgur successfully:", imgur_link)
    else:
        print("Failed to upload image to Imgur.")
     generated_text = generate_text()
    print("Generated Text:", generated_text)

if __name__ == "__main__":
    main()
