import matplotlib.pyplot as plt
import numpy as np
import torchvision
from imageDownload import trainloader, classes


def imshow(img):
    img = img / 2 + 0.5
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()


# get some random training images
if __name__ == '__main__':
    dataiter = iter(trainloader)
    images, labels = dataiter.next()
    print(' '.join('%5s' % classes[labels[j]] for j in range(4)))
    imshow(torchvision.utils.make_grid(images))
