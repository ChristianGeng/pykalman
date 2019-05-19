import numpy as np
import numpy as np
import pylab as pl

import sys
sys.path.insert(0, '/media/win-d/myfiles/2019/coursera_state_estimation/alien_software/pykalman/')


from pykalman import KalmanFilter

rnd = np.random.RandomState(0)

"""
transition_matrices : [n_timesteps-1, n_dim_state, n_dim_state] or \
[n_dim_state,n_dim_state] array-like
    Also known as :math:`A`.  state transition matrix between times t and
    t+1 for t in [0...n_timesteps-2]
"""

dt = 0.5  # in sec
print("F_prev")
F_prev = np.array([[1, dt],
                   [0, 1]])

transition_matrices = F_prev


"""
transition_covariance : [n_dim_state, n_dim_state] array-like
        Also known as :math:`Q`.  state transition covariance matrix for times
        [0...n_timesteps-2]
"""

print('Q_prev ist die Kovarianzmatrix des Process Noise')
print('w_k wurde auf 0.1 gelegt')
w_k = 0.1
Q_prev = np.eye(2) * w_k
print(w_k, '->', Q_prev)
transition_covariance = Q_prev


#

# sinus
# np.array([[1, 1], [0, 1]])
# array([[1, 1],
# [0, 1]])
