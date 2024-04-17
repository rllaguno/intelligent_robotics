import cv2
import numpy as np

def nothing(x):
    # any operation
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing) #LOWER HUE
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing) #VALUE
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing) #SATURATION
cv2.createTrackbar("UH", "Tracking", 0, 255, nothing) #UPPER HUE
cv2.createTrackbar("UV", "Tracking", 0, 255, nothing) #VALUE
cv2.createTrackbar("US", "Tracking", 0, 255, nothing) #SATURATION

font = cv2.FONT_HERSHEY_COMPLEX

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")
    
    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    #l_b = np.array([46, 93, 27])
    #u_b = np.array([111, 255, 255])
    
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel)

    # Contours detection
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
   
    for cnt in contours:
        area = cv2.contourArea(cnt)
        
        approx = cv2.approxPolyDP(cnt, 0.08*cv2.arcLength(cnt, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if area > 1000:
            if len(approx) == 4:
                cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)
                cv2.putText(frame, "Credential", (x, y), font, 1, (0, 0, 0))
          
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()