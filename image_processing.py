import cv2


def show_blue_channel(image_path):

    image = cv2.imread(image_path)

    blue_channel = image.copy()
    blue_channel[:, :, 1] = 0
    blue_channel[:, :, 2] = 0

    cv2.imshow('Blue Channel', blue_channel)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    show_blue_channel('images/variant-4.jpeg')