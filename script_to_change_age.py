import os 
import shutil

path ='./Dataset'
results_path = './Dataset_changed_age'


# 0 - [0-9], 1 - [10-19], 2 - [20-29], 3 - [30-39], 4 - [40-49], 5 - [50-59], 6 - [60,69], 7 - [70-79], 8 - [80-89], 9 - [90-99], 10 - [100-109], 11 - [110-119]

def change_age(filename):
    print(filename,'old')
    age,gender,race,random = filename.split('_')
    age = int(filename.split('_')[0])
    new_age = age//10
    new_name = f"{new_age}_{gender}_{race}_{random}"
    print(new_name,'new')
    return new_name


for i,image in enumerate(os.listdir(path)):
    age = image.split('_')[0]
    old_file_path = os.path.join(path, image)
    new_filename = change_age(image)
    new_file_path = os.path.join(results_path, new_filename)
    shutil.copy(old_file_path, new_file_path)
    