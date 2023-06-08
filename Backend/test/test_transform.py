import cv2
import numpy as np

def rotate_image(image, angle):
    height, width = image.shape[:2]
    center = (width / 2, height / 2)

    # Tạo ma trận xoay 2x3
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Áp dụng phép biến đổi affine để xoay ảnh
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

    return rotated_image