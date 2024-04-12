import cv2

# Capture video from webcam or video file
cap = cv2.VideoCapture(0)  # Change to 0, 1, etc. for different cameras, or provide filename for video file

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()
    
    # Check if the frame was successfully read
    if not ret:
        print("Failed to capture frame")
        break
    
    # Display the frame
    cv2.imshow('Video', frame)
    
    # Check for user input to exit the loop (press 'q' key)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()
