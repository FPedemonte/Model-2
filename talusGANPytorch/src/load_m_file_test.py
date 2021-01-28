import numpy as np
from utils import *
import params

dsets_path = params.data_dir + params.model_dir + "30/train/"

with open(dsets_path + "chair_000000182_1.mat", "rb") as f:
    volume = np.asarray(getVoxelFromMat(f, params.cube_len), dtype=np.float32)
    print(volume)