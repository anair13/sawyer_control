import numpy as np
import matplotlib.pyplot as plt
import time
import glob

import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')

for filename in glob.glob("/home/ashvin/data/s3doodad/demos/icra2021/dataset_v4/obj_tmp*.npy"):
# for filename in glob.glob("/home/ashvin/data/s3doodad/demos/icra2021/v1/obj_tomatoblue1.npy"):
# for filename in glob.glob("/home/ashvin/data/s3doodad/demos/icra2021/v1/obj_dice_grasp1.npy"):
    print(filename)
    x = np.load(filename, allow_pickle=True)

    for traj_i in range(1):
        traj = x[traj_i]["observations"]
        print(traj_i, len(traj))
        for t in range(len(traj)):
            # print("frame", t)
            if not traj[t]:
                print(traj_i, t)
                continue

            img = traj[t]["image_observation"]
            # img = img.reshape((48, 48, 3)) # .transpose([1, 2, 0])
            cv2.imshow("preview", img)
            # key = cv2.waitKey() # cv2.waitKey(20)
            key = cv2.waitKey(20)
            # print "key pressed: " + str(key)
            # exit on ESC, you may want to uncomment the print to know which key is ESC for you
            if key == 27 or key == 1048603:
                break

#cv2.destroyWindow("preview")
