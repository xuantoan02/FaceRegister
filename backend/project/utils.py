import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def face_similarity(face1, face2):
    normalized_A = face1 / np.linalg.norm(face1)
    normalized_B = face2 / np.linalg.norm(face2)
    similarity = cosine_similarity([normalized_A], [normalized_B])