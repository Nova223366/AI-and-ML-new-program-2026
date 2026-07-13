import cv2

def display_image(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def apply_color_filter(image, filter_type, intensity = 50):
    filtered_image = image.copy()
    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 0] = 0
    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 2] = 0
        

    elif filter_type == "increase_red":
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], intensity)
    elif filter_type == "increase_green":
        filtered_image[:, :, 1] = cv2.add(filtered_image[:, :, 1], intensity)


    elif filter_type == "decrease_red":
        filtered_image[:, :, 2] = cv2.subtract(filtered_image[:, :, 2], intensity)
    elif filter_type == "decrease_blue":
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], intensity)
      
    return filtered_image

def save_image(image):
    filename = input("Enter the filename to save the image (with extension): ")
    filename = "".join(c for c in filename if c.isalnum() or c in (' ', '.', '_'))

    cv2.imwrite(f"C:\\AI and ML new program 2026\\Class Work files\\Fun_with_filteres\\{filename}.png", image)
    print(f"Image saved as {filename}.png")

def interactive_color_filter(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found.")
        return

    while True:
        print("\nAvailable filters:")
        print("1. Red Tint")
        print("2. Blue Tint")
        print("3. Green Tint")
        print("4. Increase Red")
        print("5. Increase Green")
        print("6. Decrease Red")
        print("7. Decrease Blue")
        print("8. Save Image")
        print("9. Exit")

        choice = input("Select a filter (1-9): ")

        if choice == '9':
            break
        elif choice in ['1', '2', '3', '4', '5', '6', '7']:
            filter_types = {
                '1': "red_tint",
                '2': "blue_tint",
                '3': "green_tint",
                '4': "increase_red",
                '5': "increase_green",
                '6': "decrease_red",
                '7': "decrease_blue"
            }
            filtered_image = apply_color_filter(image, filter_types[choice])
            display_image(f"Filtered Image - {filter_types[choice]}", filtered_image)
            image = filtered_image
        elif choice == '8':
            save_image(image)
        else:
            print("Invalid choice. Please select a valid option.")

print("\nNow you can give path of your image to apply filters on it or if not just type 'd' for default image\n")
user_input = input("Enter the path to the image: ")
interactive_color_filter(r"" + user_input)

if user_input.lower() == 'd':
    interactive_color_filter(r"C:\AI and ML new program 2026\Class Work files\Fun_with_filteres\website.jpg")