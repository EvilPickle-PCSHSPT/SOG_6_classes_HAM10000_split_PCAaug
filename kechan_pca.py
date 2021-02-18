""" From https://gist.github.com/kechan/9a9f4d76f40500b85ce4493e785019ea """

import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob

def pca_aug_dir(image_dir, output_dir):
    extension = '.jpg'
    image_dir = image_dir + '/*' + extension
    pca_list = []

    for img in (glob.glob(image_dir)):
        original_image = cv2.imread(img)

        #flatten image
        renorm_image = np.reshape(original_image, (original_image.shape[0]*original_image.shape[1],3))

        renorm_image = renorm_image.astype('float32')
        renorm_image -= np.mean(renorm_image, axis=0)
        renorm_image /= np.std(renorm_image, axis=0)

        cov = np.cov(renorm_image, rowvar=False) # Calculate the 3x3 covariance matrix

        lambdas, p = np.linalg.eig(cov) # lambdas = eigenvalues, p = eigenvectors
        alphas = np.random.normal(0, 0.1, 3)

        #delta = p[:,0]*alphas[0]*lambdas[0] + p[:,1]*alphas[1]*lambdas[1] + p[:,2]*alphas[2]*lambdas[2]
        delta = np.dot(p, alphas*lambdas)

        delta = (delta*255.).astype('int8')

        pca_color_image = np.maximum(np.minimum(original_image + delta, 255), 0).astype('uint8')
        pca_list.append(pca_color_image)
        
    # pca_list = np.array(pca_list)
    # print(pca_list.shape)
    # for i, image in enumerate(pca_list):
        # print(i, image.shape)

    for i, new_image in enumerate(pca_list):
        cv2.imwrite('{}{}{}{}'.format(output_dir + '/', 'output_',i+1, extension), new_image)
        # cv2.imread(output_dir.format(i), new_image)
    #     # imgplot = plt.imshow(pca_color_image)
    #     # plt.show()

# Train set
pca_aug_dir('image/cc_train/akiec', 'aug_image/pca-aug_train/akiec') # akiec
pca_aug_dir('image/cc_train/bcc', 'aug_image/pca-aug_train/bcc') # bcc
pca_aug_dir('image/cc_train/bkl', 'aug_image/pca-aug_train/bkl') # bkl
pca_aug_dir('image/cc_train/df', 'aug_image/pca-aug_train/df') # df
pca_aug_dir('image/cc_train/mel', 'aug_image/pca-aug_train/mel') # mel
pca_aug_dir('image/cc_train/vasc', 'aug_image/pca-aug_train/vasc') # vasc

# Validation set
pca_aug_dir('image/cc_val/akiec', 'aug_image/pca-aug_val/akiec') # akiec
pca_aug_dir('image/cc_val/bcc', 'aug_image/pca-aug_val/bcc') # bcc
pca_aug_dir('image/cc_val/bkl', 'aug_image/pca-aug_val/bkl') # bkl
pca_aug_dir('image/cc_val/df', 'aug_image/pca-aug_val/df') # df
pca_aug_dir('image/cc_val/mel', 'aug_image/pca-aug_valmel') # mel
pca_aug_dir('image/cc_val/vasc', 'aug_image/pca-aug_val/vasc') # vasc

# Test set
pca_aug_dir('image/cc_test/akiec', 'aug_image/pca-aug_test/akiec') # akiec
pca_aug_dir('image/cc_test/bcc', 'aug_image/pca-aug_test/bcc') # bcc
pca_aug_dir('image/cc_test/bkl', 'aug_image/pca-aug_test/bkl') # bkl
pca_aug_dir('image/cc_test/df', 'aug_image/pca-aug_test/df') # df
pca_aug_dir('image/cc_test/mel', 'aug_image/pca-aug_test/mel') # mel
pca_aug_dir('image/cc_test/vasc', 'aug_image/pca-aug_test/vasc') # vasc   