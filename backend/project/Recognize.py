from project.Detection import Detection
from project.GetFeature import GetFeature
from project.Distances import Distances


D = Detection()
G = GetFeature()

distance=Distances()

import numpy as np
import faiss

database_vectors = []
dimension = 512
database_size = 10000
query_size = 1
#
#
#
# # Tạo một database ngẫu nhiên và query
# np.random.seed(1234)
# database_vectors = np.random.random((database_size, dimension)).astype('float32')
# query_vectors = np.random.random((query_size, dimension)).astype('float32')
# print(database_vectors.shape,query_vectors.shape)
# Build the index
import cv2
import os

database_vectors = []
thc = []
for img in os.listdir("test/girl"):
    image = cv2.imread("test/girl/" + img)
    database_vectors.append(G.get_feature(image))
# database_vectors = np.array(database_vectors)
for img in os.listdir("test/thc"):
    image = cv2.imread("test/thc/" + img)
    bbox_face=D.get_faces_bbox(image)[0]
    print(bbox_face)
    face_image=image[bbox_face[1]:bbox_face[3],bbox_face[0]:bbox_face[2]]
    database_vectors.append(G.get_feature(face_image))
thc = np.array(database_vectors)

a=distance.classic(thc[10],thc,"euclidean")
print(a)
