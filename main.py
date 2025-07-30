import cv2
import numpy as np
import pyautogui

# Start webcam
cap = cv2.VideoCapture(0)

# Define yellow color range in HSV
lower_yellow = np.array([22, 93, 0])
upper_yellow = np.array([45, 255, 255])

# To track vertical movement
previous_y = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create mask for yellow color
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 300:
            x, y, w, h = cv2.boundingRect(contour)

            # Draw rectangle on the detected object
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # If object moved up, press space
            if y < previous_y:
                pyautogui.press('space')

            previous_y = y

    # Show the webcam feed
    cv2.imshow('Webcam Feed', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
