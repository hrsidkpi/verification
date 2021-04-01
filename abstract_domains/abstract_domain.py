from abc import *
from typing import Callable
import numpy as np

class AbstractDomain(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_affine_transform(self, transformation: np.ndarray, bias: np.array):
        pass

    @abstractmethod
    def get_relu(self):
        pass