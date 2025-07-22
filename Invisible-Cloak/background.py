# 

import cv2

# Initialize webcam
cap = cv2.VideoCapture(0)

# Get default webcam frame size
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define codec and create VideoWriter object
out = cv2.VideoWriter('background.mp4',
                      cv2.VideoWriter_fourcc(*'mp4v'),  # For .mp4 format
                      20.0,  # FPS
                      (frame_width, frame_height))

print("🎥 Recording background... Press 'q' to stop and save as background.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Recording Background', frame)
        out.write(frame)

        # Stop recording on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("🛑 Stopped recording.")
            break
    else:
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print("✅ Saved as background.mp4")
