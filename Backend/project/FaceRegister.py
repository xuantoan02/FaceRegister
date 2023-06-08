from Detection import Detection
from Recognize import Recognize
import cv2





class FaceRegister(Recognize, Detection):
    def __init__(self):
        Recognize.__init__(self)
        Detection.__init__(self)
