import requests
from PIL import Image
from io import BytesIO
from config import HF_API_KEY

API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"

def generate_image_from_text(prompt: str) -> Image.Image:
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": prompt}

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        if 'image' in response.headers.get('Content-Type', ''):
            image = Image.open(BytesIO(response.content))
            return image
        else:
            raise Exception("The response did not contain an image.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")
        return None
def main():

    print("Welcome to the Text-to-Image Generation Program!")
    print("Type 'exist' to quit the program.\n")

    while True:
        prompt = input("Enter a text prompt to generate an image (or type 'exist' to quit): ")
        if prompt.lower() == 'exist':
            print("Exiting the program. Goodbye!")
            break

        print("Generating image, please wait...")
        try:
            image = generate_image_from_text(prompt)
            if image:
                image.show()
                save_option = input("Do you want to save the generated image? (yes/no): ")
                if save_option.lower() == 'yes':
                    filename = input("Enter a filename (with .png extension): ")
                    image.save(filename)
                    print(f"Image saved as {filename}")
                else:
                    print("Image not saved.")
            else:
                print("Failed to generate an image.")
        except Exception as e:
            print(f"An error occurred: {e}")
        print("-" * 80 + "\n")

if __name__ == "__main__":
    main()