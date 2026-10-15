import cv2
import matplotlib.pyplot as plt

image_path = r"C:\AI and ML new program 2026\Class Work files\Image_annotation\website.jpg"

image = cv2.imread(image_path)

image_rgb = cv2.imread(image_path, cv2.COLOR_BGR2RGB)

height, width, _ = image_rgb.shape

rect1_width, rect1_height = 150, 150
top_left = (20, 20)
bottom_right = (top_left[0] + rect1_width, top_left[1] + rect1_height)

cv2.rectangle(image_rgb, top_left, bottom_right, (0, 255, 255), 3)

rect2_width, rect2_height = 200, 150
top_left2 = (width - rect2_width - 20, height - rect2_height - 20)

bottom_right2 = (top_left2[0] + rect2_width, top_left2[1] + rect2_height)

cv2.rectangle(image_rgb, top_left2, bottom_right2, (255, 0, 255), 3)

# Step 3: Draw a circle at the center of both rectangles

center1_x = (top_left[0] + rect1_width // 2)
center1_y = (top_left[1] + rect1_height // 2)

center2_x = (top_left2[0] + rect2_width // 2)
center2_y = (top_left2[1] + rect2_height // 2)

cv2.circle(image_rgb, (center1_x, center1_y), 10, (255, 255, 0), -1)
cv2.circle(image_rgb, (center2_x, center2_y), 10, (255, 255, 0), -1)

# Step 4: Display the annotated image

cv2.line(image_rgb, (center1_x, center1_y), (center2_x, center2_y), (0, 255, 0), 2) 

# Step 5: Add text labels to the rectangles
cv2.putText(image_rgb, "Rectangle 1", (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
cv2.putText(image_rgb, "Rectangle 2", (top_left2[0], top_left2[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)

arrow_start = (width - 50, 20)
arrow_end = (width - 50, height - 20)

cv2.arrowedLine(image_rgb, arrow_start, arrow_end, (0, 255, 0), 3, tipLength=0.05)
cv2.arrowedLine(image_rgb, (20, height - 20), (width - 20, height - 20), (0, 255, 0), 3, tipLength=0.05)

height_label_position = (arrow_start[0] -150, (arrow_start[1] + arrow_end[1]) // 2)

cv2.putText(image_rgb, f'Height: {height}px', height_label_position, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2, cv2.LINE_AA)

plt.figure(figsize=(12, 8))
plt.imshow(image_rgb)
plt.title('Annotated Image')
plt.axis('off')
plt.show()