import numpy as np

def calculate(inlist):
    if len(inlist) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(inlist).reshape(3, 3)

    mean = [list(arr.mean(axis=0)), list(arr.mean(axis=1)), arr.mean()]
    var = [list(arr.var(axis=0)), list(arr.var(axis=1)), arr.var()]
    std = [list(arr.std(axis=0)), list(arr.std(axis=1)), arr.std()]
    maxi = [list(arr.max(axis=0)), list(arr.max(axis=1)), arr.max()]
    mini = [list(arr.min(axis=0)), list(arr.min(axis=1)), arr.min()]
    summ = [list(arr.sum(axis=0)), list(arr.sum(axis=1)), arr.sum()]

    calculations = {'mean': mean, 'variance': var,
                    'standard deviation': std,
                    'max': maxi, 'min': mini, 'sum': summ}

    return calculations