import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    ab = (np.linalg.norm(a) * np.linalg.norm(b))
    return(0.0 if ab == 0 else float(np.dot(a, b) / ab))