import requests
from PIL import Image
from io import BytesIO
from config import HF_API_KEY

HF_API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-3-medium-diffusers"

def generate_image_from_text(prompt: str) -> Image.Image:
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": prompt}

    try:
        response = requests.post(HF_API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()

        if "image" in response.headers.get("Content-type", ""):
            image = Image.open(BytesIO(response.content))
            return image
        else:
            raise Exception("Response does not contain an image.")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error generating image: {e}")
def main():
    print("Welcome to the text-to-image generator!")
    print("Type 'exit' to quit the program.\n")

    while True:
        prompt = input("Enter a prompt for the image: ")
        if prompt.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        print("\nGenerating image, please wait...\n")
        try:
            image = generate_image_from_text(prompt)
            image.show()
            save_option = input("Do you want to save the image? (yes/no): ")
            if save_option.lower() == 'yes':
                filename = input("Enter a filename (with .png extension): ")
                image.save(filename)
                print(f"Image saved as {filename}\n")
            else:
                print("Image not saved.\n")
        except Exception as e:
            print(f"An error occurred: {e}")

        print("-" * 80 + "\n")

if __name__ == "__main__":
    main()