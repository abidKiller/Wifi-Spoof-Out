

import os 

slash=''
if os.name=='nt':
   slash=slash+'\\'

print(slash)
class color:
   PURPLE = slash+'\033[95m'
   CYAN = slash+'\033[96m'
   DARKCYAN = slash+'\033[36m'
   BLUE =slash+ '\033[94m'
   GREEN = slash+'\033[32m'
   LIGHTGREEN = slash+'\033[92m'
   YELLOW = slash+'\033[93m'
   RED = slash+'\033[91m'
   BOLD = slash+'\033[1m'
   UNDERLINE = slash+'\033[4m'
   ORANGE = slash+'\033[33m'
   END = slash+'\033[0m'