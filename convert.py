import yaml
from pathlib import Path
import pandas

### To Convert YAML to Dictionary ###
conf = yaml.safe_load(Path('test.yml').read_text())

### To Create fstab file ####
for k in conf.keys():
    with open(k, 'w') as f:
        f.write('Create a new text file!')

### To manipulate and append data in fstab using python panda ###
d = conf
for x in d.values():
    user_dict_2=x
    data = pandas.DataFrame.from_dict(user_dict_2)
    df = data.T
    dp = df.drop(columns=['root-reserve', 'export'])
    da = dp.assign(backup=[0, 0, 0, 0],
                   fsck=[2,1,2,2])
    da[['options']] = da[['options']].fillna('default')            
    print(da)
    da.to_string('fstab')

