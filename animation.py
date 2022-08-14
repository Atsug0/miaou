import os,time,random
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
os.system('clear')
filenames = ["89.txt","88.txt","87.txt","86.txt","85.txt","84.txt","83.txt","82.txt","81.txt","80.txt","79.txt","78.txt","77.txt","76.txt","75.txt","74.txt","73.txt","72.txt","71.txt","70.txt","69.txt","68.txt","67.txt","66.txt","65.txt","64.txt","63.txt","62.txt","61.txt","60.txt","59.txt","58.txt","57.txt","56.txt","55.txt","54.txt","53.txt","52.txt","51.txt","50.txt","49.txt","48.txt","47.txt","46.txt","45.txt","44.txt","43.txt","42.txt","41.txt","40.txt","39.txt","38.txt"]
frames = []
i = 0

for name in filenames:
    with open(name,"r",encoding="utf8") as f:
        frames.append(f.readlines())
while (i < 10) :
    for frame in frames:
        s = random.randint(1,3)
        if s == 3 :
            print(bcolors.OK + "".join(frame) + bcolors.RESET)
        else :
            if s == 2 :
                print(bcolors.WARNING + "".join(frame) + bcolors.RESET)
            else :
                if s == 1:
                    print(bcolors.FAIL + "".join(frame) + bcolors.RESET)
        time.sleep(0.1)
        os.system('clear')
        i = 0
#hmoulard

