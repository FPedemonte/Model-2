
'''
params.py

Managers of all hyper-parameters

'''

import torch

epochs = 600
batch_size = 32
soft_label = False
adv_weight = 0
d_thresh = 0.8
z_dim = 200
z_dis = "norm"
model_save_step = 5
g_lr = 0.0025
d_lr = 0.00001
beta = (0.5, 0.999)
cube_len = 32
leak_value = 0.2
bias = False

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model_dir = 'chair/'    # change it to train on other data models}

#pathPC = E:/AI/medical/ # Martin
#pathPC = 'C:/Users/julir/repos/implants/' # Julian
pathPC = '/Users/martingra/Projects/implants/' #Martin mac

#data_dir = pathPC + 'talusGANPytorch/volumetric_data/' #original chairs datasource
data_dir = pathPC + 'talusGANPytorch/TalusLNpy/' #calcaneus data source
output_dir = pathPC + 'talusGANPytorch/outputs'
images_dir = pathPC + 'talusGANPytorch/images'




def print_params():
    l = 16
    print (l*'*' + 'hyper-parameters' + l*'*')

    print ('epochs =', epochs)
    print ('batch_size =', batch_size)
    print ('soft_labels =', soft_label)
    print ('adv_weight =', adv_weight)
    print ('d_thresh =', d_thresh)
    print ('z_dim =', z_dim)
    print ('z_dis =', z_dis)
    print ('model_images_save_step =', model_save_step)
    print ('data =', model_dir)
    print ('device =', device)
    print ('g_lr =', g_lr)
    print ('d_lr =', d_lr)
    print ('cube_len =', cube_len)
    print ('leak_value =', leak_value)
    print ('bias =', bias)

    print (l*'*' + 'hyper-parameters' + l*'*')







