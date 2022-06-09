import os
import numpy as np
#import matplotlib.pyplot as plt

lumi = [97.7, 129.0, 377.0, 700.0, 1500.0, 2250.0, 3000.0, 3750.0, 4500.0]
#lumi = [3750.0]

HF_lim = [[],[],[]]
W_lim = [[],[],[]]
HFW_lim = [[],[],[]]
HF_3Glb_lim = [[],[],[]]
HF_2Glb_lim = [[],[],[]]

for lu_no, lu in enumerate(lumi):
    print(lu)
    #command1='python HF_test.py --luminosity '+str(lu) #modifies event no. by lumi python replace_test.py --luminosity 97.7 --filename HF_Combined_ThreeGlb.txt --lineno 66 --outputname HF_Combined_ThreeGlb_Mod.txt
    #command2='python W_test.py --luminosity '+str(lu)
    command1='python replace_test.py --luminosity '+str(lu)+ " --filename HF_Combined_TwoGlb.txt --lineno 48 --outputname HF_Combined_TwoGlb_Mod.txt"
    command2='python replace_test.py --luminosity '+str(lu)+ " --filename HF_Combined_ThreeGlb.txt --lineno 66 --outputname HF_Combined_ThreeGlb_Mod.txt"
    #command3='python replace_test.py --luminosity '+str(lu)+ " --filename HF_Combined.txt --lineno 102 --outputname HF_Combined_Mod.txt"
    command4='python replace_test.py --luminosity '+str(lu)+ " --filename W_Combined.txt --lineno 30 --outputname W_Combined_Mod.txt"
    os.system(command1)
    os.system(command2)
    os.system('combineCards.py HF_Combined_TwoGlb_Mod.txt HF_Combined_ThreeGlb_Mod.txt> HF_Combined_Mod.txt')
    os.system(command4)
    os.system('combineCards.py W_Combined_Mod.txt HF_Combined_Mod.txt> HFW_Combined.txt')
    os.system('python runLimit.py -i HF_Combined_Mod.txt > out1.txt')
    os.system('python runLimit.py -i W_Combined_Mod.txt > out2.txt')
    os.system('python runLimit.py -i HFW_Combined.txt > out3.txt')
    os.system('python runLimit.py -i HF_Combined_TwoGlb_Mod.txt > out4.txt')
    os.system('python runLimit.py -i HF_Combined_ThreeGlb_Mod.txt > out5.txt')
    
    with open("out1.txt", 'r') as f1:
        for line in f1:
            if '50.0%' in line:
                linsp = line.split()
                HF_lim[0].append(float(linsp[-1]))
            if '16.0%' in line:
                linsp = line.split()
                HF_lim[1].append(float(linsp[-1]))
            if '84.0%' in line:
                linsp = line.split()
                HF_lim[2].append(float(linsp[-1]))
    with open("out2.txt", 'r') as f2:
        for line in f2:
            if '50.0%' in line:
                linsp = line.split()
                W_lim[0].append(float(linsp[-1]))
            if '16.0%' in line:
                linsp = line.split()
                W_lim[1].append(float(linsp[-1]))
            if '84.0%' in line:
                linsp = line.split()
                W_lim[2].append(float(linsp[-1]))
    with open("out3.txt", 'r') as f3:
        for line in f3:
            if '50.0%' in line:
                linsp = line.split()
                HFW_lim[0].append(float(linsp[-1]))
            if '16.0%' in line:
                linsp = line.split()
                HFW_lim[1].append(float(linsp[-1]))
            if '84.0%' in line:
                linsp = line.split()
                HFW_lim[2].append(float(linsp[-1]))
    with open("out4.txt", 'r') as f4:
        for line in f4:
            if '50.0%' in line:
                linsp = line.split()
                HF_2Glb_lim[0].append(float(linsp[-1]))
            if '16.0%' in line:
                linsp = line.split()
                HF_2Glb_lim[1].append(float(linsp[-1]))
            if '84.0%' in line:
                linsp = line.split()
                HF_2Glb_lim[2].append(float(linsp[-1]))
    with open("out5.txt", 'r') as f5:
        for line in f5:
            if '50.0%' in line:
                linsp = line.split()
                HF_3Glb_lim[0].append(float(linsp[-1]))
            if '16.0%' in line:
                linsp = line.split()
                HF_3Glb_lim[1].append(float(linsp[-1]))
            if '84.0%' in line:
                linsp = line.split()
                HF_3Glb_lim[2].append(float(linsp[-1]))
                
                
print("HF_lim = "+ str(HF_lim))
print("W_lim = "+ str(W_lim))
print("HFW_lim = "+ str(HFW_lim))
print("HF_3Glb_lim = "+ str(HF_3Glb_lim))
print("HF_2Glb_lim = "+ str(HF_2Glb_lim))