import cv2
import numpy as np

def track_marker(check_region=False):

    cap = cv2.VideoCapture(0)

    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
    parameters = cv2.aruco.DetectorParameters()

    while True:

        ret, frame = cap.read()
        if not ret:
            break

        corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=parameters)

        if ids is not None:

            cv2.aruco.drawDetectedMarkers(frame, corners, ids)

            center = np.mean(corners[0][0], axis=0)
            x, y = int(center[0]), int(center[1])

            if check_region and x > frame.shape[1] // 2:
                cv2.putText(frame, "Marker is in the right half", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    track_marker(check_region=True)