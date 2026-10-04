import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    ab = (np.linalg.norm(a) * np.linalg.norm(b))
    if ab != 0:
        return(float(np.dot(a, b) / ab))
    return 0.0