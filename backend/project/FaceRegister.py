from .Detection import Detection
from .Recognize import Recognize
from api.models.Users import UserManager, FaceManager
from core import config
import cv2


class FaceRegister(Recognize, Detection):
    def __init__(self):
        Recognize.__init__(self)
        Detection.__init__(self)
        self.userDb = UserManager(config.NAME_TABLE_USER)
        self.faceDb = FaceManager(config.NAME_TABLE_FACE)

    def face_register(self, user_id, path_image):

        row = self.faceDb.get_user(user_id)
        image = cv2.imread(path_image)
        bbox = self.get_faces_bbox(image)
        if len(bbox) == 0:
            message = "顔なし"
        elif len(bbox) == 1:
            face = image[bbox[0][1]:bbox[0][3], bbox[0][0]:bbox[0][2]]
            face_feature = self.get_feature(face)
            face_feature = face_feature.tolist()
            face_feature = str(face_feature)
            if not row:
                self.faceDb.create_face_feature(user_id, face_feature)
            else:
                self.faceDb.update_face_feature(user_id, face_feature)
            message = "登録が成功しました"
        else:
            message = "たくさんの顔があります"

        return {
            "message": message
        }


