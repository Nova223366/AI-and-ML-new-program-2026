import cv2
import matplotlib.pyplot as plt

# Step 1: Load image
image_path = r"C:\AI and ML new program 2026\Class Work files\Image_annotation\website.jpg"

image = cv2.imread(image_path)

# Safety check (important)
if image is None:
    raise ValueError("Image not found. Please check the file path.")

# Step 2: Convert BGR → RGB (correct way)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Step 3: Get image dimensions
height, width, _ = image_rgb.shape

# -------------------------------
# Step 4: First rectangle (top-left)
# -------------------------------
rect1_width, rect1_height = 150, 150
top_left = (20, 20)
bottom_right = (top_left[0] + rect1_width, top_left[1] + rect1_height)

cv2.rectangle(image_rgb, top_left, bottom_right, (0, 255, 255), 3)

# -------------------------------
# Step 5: Second rectangle (bottom-right)
# -------------------------------
rect2_width, rect2_height = 200, 150
top_left2 = (width - rect2_width - 20, height - rect2_height - 20)
bottom_right2 = (top_left2[0] + rect2_width, top_left2[1] + rect2_height)

cv2.rectangle(image_rgb, top_left2, bottom_right2, (255, 0, 255), 3)

# -------------------------------
# Step 6: Centers of rectangles
# -------------------------------
center1 = (top_left[0] + rect1_width // 2,
           top_left[1] + rect1_height // 2)

center2 = (top_left2[0] + rect2_width // 2,
           top_left2[1] + rect2_height // 2)

# Draw circles at centers
cv2.circle(image_rgb, center1, 10, (255, 255, 0), -1)
cv2.circle(image_rgb, center2, 10, (255, 255, 0), -1)

# -------------------------------
# Step 7: Connect both centers with a line
# -------------------------------
cv2.line(image_rgb, center1, center2, (0, 255, 0), 2)

# -------------------------------
# Step 8: Add text labels
# -------------------------------
cv2.putText(image_rgb, "Rectangle 1",
            (top_left[0], top_left[1] - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6,
            (0, 255, 255), 2)

cv2.putText(image_rgb, "Rectangle 2",
            (top_left2[0], top_left2[1] - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6,
            (255, 0, 255), 2)

# -------------------------------
# Step 9: Draw arrows for dimensions
# -------------------------------
arrow_start = (width - 50, 20)
arrow_end = (width - 50, height - 20)

cv2.arrowedLine(image_rgb, arrow_start, arrow_end,
                (0, 255, 0), 3, tipLength=0.05)

cv2.arrowedLine(image_rgb, (20, height - 20),
                (width - 20, height - 20),
                (0, 255, 0), 3, tipLength=0.05)

# -------------------------------
# Step 10: Add height text
# -------------------------------
height_label_position = (
    arrow_start[0] - 150,
    (arrow_start[1] + arrow_end[1]) // 2
)

cv2.putText(image_rgb, f"Height: {height}px",
            height_label_position,
            cv2.FONT_HERSHEY_SIMPLEX, 0.8,
            (255, 255, 0), 2, cv2.LINE_AA)

# -------------------------------
# Step 11: Display image
# -------------------------------
plt.figure(figsize=(12, 8))
plt.imshow(image_rgb)
plt.title("Annotated Image")
plt.axis("off")
plt.show()