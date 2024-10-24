from importlib import reload
from NoraGeneral import noraMethodBase
import numpy as np
import scipy as sp
import sklearn as sl
import torch

reload(noraMethodBase)


class NoraFDDAMethod(noraMethodBase.NoraMethodBase):
    def __init__(self):
        super(NoraFDDAMethod, self).__init__()


