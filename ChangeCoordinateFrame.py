#Modern Robotics Problem 3.3

import numpy as np

PMatrix = np.array([[np.sqrt(2), 1, 0],[0, 1, 2*np.sqrt(2)],[2, -1, 0]])
PPMatrix = np.array([[0, 1/np.sqrt(2), -np.sqrt(2)],[2, 1/np.sqrt(2), np.sqrt(2)],[np.sqrt(2), -np.sqrt(2), -2]])

PPInv = np.linalg.inv(PPMatrix)
R = np.dot(PMatrix, PPInv)

print(np.transpose(R))