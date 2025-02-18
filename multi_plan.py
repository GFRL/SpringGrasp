from subprocess import call
import multiprocessing as mp
import os
import json
def call_cmd(obj_name,id,gpu_id):
    for scale in [0.06,0.08,0.10,0.12]:
        cmd=f"CUDA_VISIBLE_DEVICES={gpu_id} python optimize_pregrasp.py --Trail_id {id} --obj_name {obj_name} --scale {scale}"
        print("Start!",cmd)
        ret=call(cmd,shell=True)  
        print("Done!",id)
    return ret

def main(gpu_id,obj_list):
    save_path="results"
    real_obj_name_list=[]
    for obj_name in obj_name_list:
        tmp_path=os.path.join(save_path,obj_name)
        for file in ["scale006","scale008","scale010","scale012"]:
            if(not os.path.exists(os.path.join(tmp_path,file))):
                print("obj_name",obj_name,"lack",file)
                real_obj_name_list.append(obj_name)
                break
    print("real_obj_name_list",len(real_obj_name_list))
    obj_name_list=real_obj_name_list
    total_num=len(obj_name_list)
    test_num=total_num
    for i in range(test_num):
        call_cmd(obj_name_list[i:i+1],i,gpu_id)


if __name__ == "__main__":
    obj_list_path="../assets/DGNObj_splits/icra_test.json"
    with open(obj_list_path,"r") as f:
        obj_list=json.load(f)
    
    gpu_id_num=8*5 #A GPU can serve 5 processes
    obj_list_list=[[] for i in range(gpu_id_num)]
    for i in range(len(obj_list)):
        obj_list_list[i%gpu_id_num].append(obj_list[i])
    gpu_id_list=[i//5 for i in range(gpu_id_num)]
    
    pool = mp.Pool(processes=gpu_id_num)
    pool.map(main,zip(gpu_id_list,obj_list_list))
    pool.close()
    pool.join()
    