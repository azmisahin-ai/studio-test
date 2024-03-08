import unittest
import torch
from torchvision import datasets, transforms


class TorchvisionTest(unittest.TestCase):
    """
    A test suite for torchvision functionalities.
    """

    def test_torchvision_mnist(self):
        """
        Test loading and processing the MNIST dataset without using GPU.
        """
        # Create a transform to convert images to tensors
        transform = transforms.ToTensor()

        # Download and load the MNIST training dataset (to the "temp" folder)
        train_data = datasets.MNIST(
            root="temp",
            train=True,
            download=True,
            transform=transform,
        )

        # Check that the dataset is not empty
        items_count = len(train_data)
        self.assertTrue(items_count > 0)

        # Get the first image and label from the dataset
        image, label = train_data[0]

        # Check that the shape of the image is (1, 28, 28)
        # (Single channel, 28x28 pixels)
        self.assertEqual(image.shape, (1, 28, 28))

        # Check that the label is an integer
        print("number", label)
        self.assertEqual(type(label), int)

    def test_torchvision_mnist_with_cuda(self):
        """
        Test loading and processing the MNIST dataset with GPU support.
        """
        # Create a transform to convert images to tensors
        transform = transforms.ToTensor()

        # Download and load the MNIST training dataset (to the "temp" folder)
        train_data = datasets.MNIST(
            root="temp",
            train=True,
            download=True,
            transform=transform,
        )

        # Check that the dataset is not empty
        items_count = len(train_data)
        self.assertTrue(items_count > 0)

        # Get the first image and label from the dataset
        image, label = train_data[0]

        # Check that the shape of the image is (1, 28, 28)
        self.assertEqual(image.shape, (1, 28, 28))

        # Check that the label is an integer
        print("number", label)
        self.assertEqual(type(label), int)

        # Use DataLoader to load the dataset in batches
        batch_size = 64
        train_loader = torch.utils.data.DataLoader(
            train_data, batch_size=batch_size, shuffle=True
        )

        # If GPU is available, perform GPU transfer operations
        if torch.cuda.is_available():
            device = torch.device("cuda")
        else:
            device = torch.device("cpu")

        # Loop for testing
        for images, labels in train_loader:
            # Move the data to GPU for each batch
            images = images.to(device)
            labels = labels.to(device)


if __name__ == "__main__":
    unittest.main()
