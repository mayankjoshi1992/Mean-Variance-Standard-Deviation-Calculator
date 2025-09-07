import numpy as np

def calculate(list_in):
    # Validate input length
    if len(list_in) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convert list to 3x3 numpy array
    arr = np.array(list_in).reshape(3, 3)

    # Build dictionary
    calculations = {
        'mean': [
            arr.mean(axis=0).tolist(),    # mean by columns
            arr.mean(axis=1).tolist(),    # mean by rows
            arr.mean().item()             # mean of all
        ],
        'variance': [
            arr.var(axis=0).tolist(),
            arr.var(axis=1).tolist(),
            arr.var().item()
        ],
        'standard deviation': [
            arr.std(axis=0).tolist(),
            arr.std(axis=1).tolist(),
            arr.std().item()
        ],
        'max': [
            arr.max(axis=0).tolist(),
            arr.max(axis=1).tolist(),
            arr.max().item()
        ],
        'min': [
            arr.min(axis=0).tolist(),
            arr.min(axis=1).tolist(),
            arr.min().item()
        ],
        'sum': [
            arr.sum(axis=0).tolist(),
            arr.sum(axis=1).tolist(),
            arr.sum().item()
        ]
    }

    return calculations


