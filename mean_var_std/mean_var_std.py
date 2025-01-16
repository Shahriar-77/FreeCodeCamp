import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    else:
    
        a = np.array(list)
        a_mat = a.reshape((3,3))

        mean = [np.mean(a_mat, axis=0).tolist(),np.mean(a_mat, axis=1).tolist(),np.mean(a_mat).tolist()]

        variance = [np.var(a_mat, axis=0).tolist(),np.var(a_mat, axis=1).tolist(),np.var(a_mat).tolist()]

        std_dev = [np.std(a_mat, axis=0).tolist(),np.std(a_mat, axis=1).tolist(),np.std(a_mat).tolist()]

        max_a = [np.max(a_mat, axis=0).tolist(),np.max(a_mat, axis=1).tolist(),np.max(a_mat).tolist()]
        
        min_a = [np.min(a_mat, axis=0).tolist(),np.min(a_mat, axis=1).tolist(),np.min(a_mat).tolist()]
        
        sum_a = [np.sum(a_mat, axis=0).tolist(),np.sum(a_mat, axis=1).tolist(),np.sum(a_mat).tolist()]
        
         
        
        calculations= {
    'mean': mean,
    'variance': variance,
    'standard deviation': std_dev,
    'max': max_a,
    'min': min_a,
    'sum': sum_a
                        }


    return calculations