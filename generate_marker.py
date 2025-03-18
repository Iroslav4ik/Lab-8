import cv2
import numpy as np


marker_id = 4
marker_size = 500

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

marker_image = np.zeros((marker_size, marker_size), dtype=np.uint8)
marker_image = cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size, marker_image, 1)

cv2.imwrite("aruco_marker.png", marker_image)

cv2.imshow("ArUco Marker", marker_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Метка успешно создана и сохранена в файл 'aruco_marker.png'")