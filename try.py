import os
import numpy as np
from function import *
label_map = {label: num for num, label in enumerate(actions)}

sequences, labels = [], []
for seq in sequences:
    print(len(seq), [frame.shape for frame in seq])