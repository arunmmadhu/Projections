import argparse

parser = argparse.ArgumentParser(description='For scaling events by lumi')

parser.add_argument('--luminosity', action='store', default=97.7, help="Lumi scale\n DEFAULT: 97.7")
parser.add_argument('--filename', action='store', default="HF_Combined.txt", help="File to be modified\n DEFAULT: HF_Combined.txt")
parser.add_argument('--lineno', action='store', default=102, help="Lumi no\n DEFAULT: 102")
parser.add_argument('--outputname', action='store', default="HF_Combined_Mod.txt", help="File output\n DEFAULT: HF_Combined_Mod.txt")

args = parser.parse_args()

# opening the file in read mode
file = open(args.filename, "r")
replacement = ""
# using the for loop
for linenum, line in enumerate(file):
    #print(linenum)
    if(linenum==int(args.lineno)):#102
        print(line)
        line_mod=line
        x1 = line.split()
        x1 = x1[1:]
        #print(x1)
        for i in x1:
            imod=float(i)*(float(args.luminosity)/97.7)
            #print(imod)
            res = "{:.4f}".format(imod)
            #print(res)
            line_mod=line_mod.replace(i, res)
        print(line_mod)
        replacement = replacement + line_mod
    else:
        replacement = replacement + line
            
file.close()

# opening the file in write mode
fout = open(args.outputname, "w")
fout.write(replacement)
fout.close()

