#! /usr/bin/python

import numpy as np
from scipy.ndimage import convolve, rotate

def random_image_generator(image):
    # Create our movement vectors for translation first. 
    move_up = [[0, 1, 0],
               [0, 0, 0],
               [0, 0, 0]]

    move_left = [[0, 0, 0],
                 [1, 0, 0],
                 [0, 0, 0]]

    move_right = [[0, 0, 0],
                  [0, 0, 1],
                  [0, 0, 0]]

    move_down = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 1, 0]]

    # Create a dict to store these directions in.
    dir_dict = {1:move_up, 2:move_left, 3:move_right, 4:move_down}

    # Pick a random direction to move.
    direction = dir_dict[np.random.randint(1,5)]

    # Pick a random angle to rotate (10 degrees clockwise to 10 degrees counter-clockwise).
    angle = np.random.randint(-10,11)

    # Move the random direction and change the pixel data back to a 2D shape.
    moved = convolve(image.reshape(28,28), direction, mode = 'constant')

    # Rotate the image
    rotated = rotate(moved, angle, reshape = False)
    return rotated

def augment(features, targets, num_new):
    # First, create empty arrays that will hold our new training examples.
    x_holder = np.zeros((num_new, features.shape[1]))
    y_holder = np.zeros(num_new)

    # Now, loop through our training examples, selecting them at random for distortion.
    for i in xrange(num_new):
        # Pick a random index to decide which image to alter.
        random_ind = np.random.randint(0, features.shape[0])

        # Select our training example and target.
        x_samp = features[random_ind]
        y_samp = targets[random_ind]

        # Change our image and convert back to 1D.
        new_image = random_image_generator(x_samp).ravel()

        # Store these in our arrays.
        x_holder[i,:] = new_image
        y_holder[i] = y_samp

    # Now that our loop is over, combine our original training examples with the new ones.
    combined_x = np.vstack((features, x_holder))
    combined_y = np.hstack((targets, y_holder))

    # Return our new training examples and targets.
    return combined_x, combined_y

