import cv2

# Constants for the known dimensions of the ID card in centimeters
KNOWN_WIDTH = 8.5
KNOWN_HEIGHT = 5.25

# Initialize your known distance from the camera to the ID card
# when the reference image was taken
knownDistance = 33.5/2  # for example, 30 cm


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
def distance_to_camera(knownWidth, knownHeight, focalLength, perWidth, perHeight):
    distance_w = (knownWidth * focalLength) / perWidth
    distance_h = (knownHeight * focalLength) / perHeight
    return distance_w, distance_h

# Load the reference image from where the path is specified
reference_image = cv2.imread('C:\\Users\\rodri\\Documents\\Robotics\\robotica_inteligente_eq5\\vision\\challenge_01\\calib.jpg')
id_card_contour = find_id_card_contour(reference_image)

focalLength = 0

if id_card_contour is not None:
    x, y, w, h = cv2.boundingRect(id_card_contour)
    focalLength = (w * knownDistance) / KNOWN_WIDTH

# Check if we have calculated the focal length
if focalLength == 0:
    raise ValueError("Could not calculate the focal length.")

# Initialize video capture from the camera
camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if not ret:
        break

    id_card_contour = find_id_card_contour(frame)

    if id_card_contour is not None:
        x, y, w, h = cv2.boundingRect(id_card_contour)
        distance_w, distance_h = distance_to_camera(KNOWN_WIDTH, KNOWN_HEIGHT, focalLength, w, h)

        cv2.putText(frame, f"{distance_w:.2f} cm", (frame.shape[1] - 400, frame.shape[0] - 20), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 3)
        cv2.drawContours(frame, [id_card_contour], -1, (0, 255, 0), 2)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()