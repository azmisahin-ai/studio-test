"""
Module: CudaTest

This module contains unit tests for a PyTorch application.

Test cases:
    - TorchTest: A test suite for PyTorch functionality,
    checking CUDA availability and performing a simple operation.
"""

import unittest
import torch


class TorchTest(unittest.TestCase):
    """
    Class representing a test suite for PyTorch application.
    """

    def setUp(self):
        """
        Set up method for initializing the test environment.
        """

    def test_torch_basics(self):
        """
        Test basic PyTorch functionality.

        This test case checks the basic functionality of PyTorch by
        creating a tensor and performing a simple addition operation.
        It asserts that the results match the expected values.
        """
        # Test torch.tensor creation
        x = torch.tensor([1.0, 2.0, 3.0])
        self.assertTrue(torch.all(torch.eq(x, torch.tensor([1.0, 2.0, 3.0]))))

        # Test torch.add operation
        y = torch.add(x, x)
        self.assertTrue(torch.all(torch.eq(y, torch.tensor([2.0, 4.0, 6.0]))))

    def test_cuda(self):
        """
        Test CUDA availability and perform a simple PyTorch operation.

        This test checks if CUDA is available, sets the device accordingly,
        and performs a simple PyTorch operation. It asserts that the results
        match the expected values.
        """
        # Check if CUDA is available, set the device accordingly
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        # Assertion to ensure the device type is CUDA
        self.assertTrue(device.type == "cuda")

        # Perform a simple PyTorch operation on the chosen device
        x = torch.tensor([1.0, 2.0, 3.0], device=device)
        y = x * 2

        # Define expected results for tensors
        expected_x = torch.tensor([1.0, 2.0, 3.0], device=device)
        expected_y = expected_x * 2

        # Check equality of tensors
        self.assertTrue(torch.all(torch.eq(x, expected_x)))
        self.assertTrue(torch.all(torch.eq(y, expected_y)))


if __name__ == "__main__":
    unittest.main()
