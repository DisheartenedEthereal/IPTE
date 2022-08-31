import os,sys
print("Running standard checks")
val = os.path.isfile("/home/morbid/Storage/Projects/IPTE/env.sh")
print(val)
if val == True:
    print("Env.sh exists, passing")
else:
    print("Env.sh error. dying")
    sys.exit()
os.system("bash --noprofile --rcfile env.sh")
