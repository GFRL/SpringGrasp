import os
import numpy as np
data_dir="results1"
for instance in os.listdir(data_dir):
    instance_dir=os.path.join(data_dir,instance)
    for scale in os.listdir(instance_dir):
        scale_dir=os.path.join(instance_dir,scale)
        for file in os.listdir(scale_dir):
            file_path=os.path.join(scale_dir,file)
            data=np.load(file_path,allow_pickle=True).item()
            data['obj_path']=data['obj_path'].replace("assets/DGNObj/","assets/object/DGN_obj/processed_data/")
            np.save(file_path,data,allow_pickle=True)
    print("Done!",instance)