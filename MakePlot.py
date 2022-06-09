HF_lim = [[0.3398, 0.292, 0.1826, 0.125, 0.0864, 0.0708, 0.061, 0.0542, 0.0493], [0.229, 0.1967, 0.1239, 0.0848, 0.0587, 0.048, 0.0412, 0.037, 0.0333], [0.5239, 0.4487, 0.2789, 0.1909, 0.1316, 0.1075, 0.0926, 0.0825, 0.0751]]
W_lim = [[0.6035, 0.5078, 0.2598, 0.1768, 0.1089, 0.0835, 0.0688, 0.0591, 0.0518], [0.3834, 0.3226, 0.166, 0.1113, 0.0669, 0.0505, 0.0413, 0.0348, 0.0303], [0.979, 0.8165, 0.414, 0.2825, 0.1761, 0.1362, 0.1133, 0.0978, 0.0867]]
HFW_lim = [[0.2803, 0.2393, 0.1411, 0.0957, 0.063, 0.0498, 0.0415, 0.0366, 0.0327], [0.1863, 0.159, 0.0937, 0.0631, 0.0409, 0.0319, 0.0267, 0.0231, 0.0204], [0.4294, 0.3665, 0.2155, 0.1471, 0.0974, 0.0777, 0.0656, 0.0575, 0.0517]]
HF_2Glb_lim = [[1.0586, 0.8945, 0.543, 0.3848, 0.248, 0.2188, 0.1875, 0.167, 0.1514], [0.7079, 0.599, 0.3636, 0.2586, 0.1683, 0.1476, 0.1272, 0.1127, 0.1021], [1.6519, 1.3916, 0.8395, 0.5931, 0.3812, 0.3351, 0.2881, 0.255, 0.2312]]
HF_3Glb_lim = [[0.3652, 0.3135, 0.1973, 0.1338, 0.0933, 0.0757, 0.0649, 0.0581, 0.0527], [0.2461, 0.2112, 0.1339, 0.0903, 0.0633, 0.0514, 0.0443, 0.0392, 0.0356], [0.563, 0.4832, 0.3003, 0.2043, 0.142, 0.1149, 0.0992, 0.0882, 0.08]]

lumi = [97.7, 129.0, 377.0, 700.0, 1500.0, 2250.0, 3000.0, 3750.0, 4500.0]

import numpy as np
import matplotlib.pyplot as plt

for lim_name in ["HF_lim","W_lim","HFW_lim","HF_3Glb_lim","HF_2Glb_lim"]:
    array0 = np.array(eval("%s" % (lim_name+"[0]")))
    array1 = np.array(eval("%s" % (lim_name+"[1]")))
    array2 = np.array(eval("%s" % (lim_name+"[2]")))
    subtracted_array1 = np.subtract(array0, array1)
    subtracted_array2 = np.subtract(array2, array0)
    subtracted1 = list(subtracted_array1)
    subtracted2 = list(subtracted_array2)
    exec("%s = %s" % (lim_name+"[1]","subtracted1"))
    exec("%s = %s" % (lim_name+"[2]","subtracted2"))
    
plt.errorbar(lumi, HF_lim[0], yerr=[HF_lim[1],HF_lim[2]], xerr=None, fmt ='r--')
plt.errorbar(lumi, W_lim[0], yerr=[W_lim[1],W_lim[2]], xerr=None, fmt ='bs')
plt.errorbar(lumi, HFW_lim[0], yerr=[HFW_lim[1],HFW_lim[2]], xerr=None, fmt ='o')
plt.xlabel('Integrated Luminosity $fb^{-1}$')
plt.ylabel('Expected Limit ($10^{-7}$)')
plt.legend(['HF', 'W','HF + W'])
plt.xscale("log")
plt.yscale("log")
plt.savefig('limits1.png', dpi=300) 
plt.show()