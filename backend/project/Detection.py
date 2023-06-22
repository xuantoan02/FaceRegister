import cv2
import numpy as np
import time
from insightface.utils import face_align
from insightface.app import FaceAnalysis


class Detection:
    def __init__(self):
        self.app = FaceAnalysis(providers=['CUDAExecutionProvider', 'CUDAExecutionProvider'],
                                allowed_modules=['detection'])
        self.app.prepare(ctx_id=0, det_size=(640, 640))

    def get_faces_bbox(self, image):
        face_bbox = self.app.get(image)
        bbox = []
        if face_bbox:
            for face in face_bbox:
                if face['det_score'] > 0.6:
                    bbox.append(face['bbox'].astype('int'))
        return bbox

    @staticmethod
    def angle_with_x_axis(line):
        vector = line[1] - line[0]
        angle_rad = np.arctan2(vector[1], vector[0])
        angle_deg = np.degrees(angle_rad)

        return angle_deg

    @staticmethod
    def rotate_image(image, angle):
        height, width = image.shape[:2]
        center = (width / 2, height / 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

        return rotated_image

    def get_face_align(self, image):
        st = time.time()
        faces = self.get_faces(image)
        print(time.time() - st)
        img_r = image
        i = 0
        for face in faces:
            eyes_point = face['kps'][:2].astype("int")
            angle = self.angle_with_x_axis(eyes_point)

            if abs(angle) > 15:
                print("face align")
                bbox = face["bbox"].astype("int")
                keysPoint = faces[0]['kps']
                img_r = image[bbox[1]:bbox[3], bbox[0]:bbox[2]]
                # img_r = self.rotate_image(img_face, angle)
                # img_r=face_align.norm_crop(img_r,keysPoint,112)
                # cv2.imwrite(f"../test/faces/{i}.jpg",img_face)

            else:
                print("no rotate")
                bbox = face["bbox"].astype("int")
                img_r = image[bbox[1]:bbox[3], bbox[0]:bbox[2]]
                cv2.imwrite(f"../test/faces/{i}.jpg", img_r)
            i += 1
            cv2.rectangle(image, (bbox[0], bbox[1]), ([bbox[2], bbox[3]]), (255, 255, 0), 3)
