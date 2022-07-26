#P = (1/sqrt(3), -1/sqrt(6), 1/sart(2))
#Rot(z,-120)Rot(y,135)Rot(x,30)P

import numpy as np

ThetaX = np.radians(30)
ThetaY = np.radians(135)
ThetaZ = np.radians(-120)

P = np.array([[1/np.sqrt(3)],[-1/np.sqrt(6)],[1/np.sqrt(2)]])

RotX = np.array([[1, 0, 0],[0, np.cos(ThetaX), -np.sin(ThetaX)],[0, np.sin(ThetaX), np.cos(ThetaX)]])
RotY = np.array([[np.cos(ThetaY), 0, np.sin(ThetaY)],[0, 1, 0],[-np.sin(ThetaY), 0, np.cos(ThetaY)]])
RotZ = np.array([[np.cos(ThetaZ), -np.sin(ThetaZ), 0],[np.sin(ThetaZ), np.cos(ThetaZ), 0],[0, 0, 1]])

MatRot = np.dot(RotZ, RotY)
MatRot = np.dot(MatRot, RotX)

print(MatRot)
print(np.dot(MatRot,P))