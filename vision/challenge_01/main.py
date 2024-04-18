import cv2
import numpy as np

# Constants for the known dimensions of the ID card in centimeters
KNOWN_WIDTH = 8.5
KNOWN_HEIGHT = 5.25

# Initialize your known distance from the camera to the ID card
# when the reference image was taken
knownDistance = 33.5  # for example, 30 cm

# Function to find the ID card contour in the image
def find_id_card_contour(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 75, 200)

    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]

    for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            return approx
    return None

# Function to calculate the distance to the ID card using triangle similarity
def distance_to_camera(knownWidth, focalLength, perWidth):
    distance = (knownWidth * focalLength) / perWidth
    return distance

# Initialize video capture from the camera
camera = cv2.VideoCapture(0)

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 40, 255, lambda x: None) # LOWER HUE
cv2.createTrackbar("LV", "Tracking", 83, 255, lambda x: None) # VALUE
cv2.createTrackbar("LS", "Tracking", 26, 255, lambda x: None) # SATURATION
cv2.createTrackbar("UH", "Tracking", 255, 255, lambda x: None) # UPPER HUE
cv2.createTrackbar("UV", "Tracking", 255, 255, lambda x: None) # VALUE
cv2.createTrackbar("US", "Tracking", 255, 255, lambda x: None) # SATURATION

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = camera.read()
    if not ret:
        break

    id_card_contour = find_id_card_contour(frame)

    if id_card_contour is not None:
        x, y, w, h = cv2.boundingRect(id_card_contour)
        focalLength = (w * knownDistance) / KNOWN_WIDTH
        
        l_h = cv2.getTrackbarPos("LH", "Tracking")
        l_s = cv2.getTrackbarPos("LS", "Tracking")
        l_v = cv2.getTrackbarPos("LV", "Tracking")
        
        u_h = cv2.getTrackbarPos("UH", "Tracking")
        u_s = cv2.getTrackbarPos("US", "Tracking")
        u_v = cv2.getTrackbarPos("UV", "Tracking")

        l_b = np.array([l_h, l_s, l_v])
        u_b = np.array([u_h, u_s, u_v])

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, l_b, u_b)
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.erode(mask, kernel)

        # Contours detection
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            approx = cv2.approxPolyDP(cnt, 0.08 * cv2.arcLength(cnt, True), True)

            if area > 1000 and len(approx) == 4:
                cv2.drawContours(frame, [approx], 0, (0, 255, 0), 2)
                cv2.putText(frame, "Credential", (x, y), font, 1, (0, 255, 0))

        distance = distance_to_camera(KNOWN_WIDTH, focalLength, w)

        cv2.putText(frame, f"Distance: {distance:.2f} cm", (10, 30), font, 0.7, (0, 255, 0), 2)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
