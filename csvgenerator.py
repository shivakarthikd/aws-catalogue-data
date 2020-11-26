import csv
from test import ser_cat,s_code
with open(s'.csv', 'w') as f:
    for key in my_dict.keys():
        f.write("%s,%s\n"%(key,my_dict[key]))