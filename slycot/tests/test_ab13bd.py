# ===================================================
# ag08bd tests

import unittest
from slycot import analysis
import numpy as np

class test_ab13bd(unittest.TestCase):
    """Verify ab13bd new api"""

    A1 = np.array([[0.0, 1.0],[-0.5, -0.1]])
    B1 = np.array([[0.],[1.]])
    C1 = np.eye(2)
    D1 = np.zeros((2,1))

    def test1_ab13bd_new_api(self):
        """test
        """
        h2norm, *_ = analysis._wrapper.ab13bd(self.A1,self.B1,self.C1,self.D1)