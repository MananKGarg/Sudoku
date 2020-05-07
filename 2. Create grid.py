import cv2
import numpy as np

def CreateGrid(preprocessed_image):

    squares = []

    side_length = preprocessed_image.shape[0] # As the preprocessed image is a square, we can take any index for side length

    small_square_side = side_length/9

    for i in range(9):
        for j in range(9):
            p1 = (i * small_square_side, j * small_square_side)  # top left corner of box
            p2 = ((i + 1) * small_square_side, (j + 1) * small_square_side)  # bottom right corner of box
            squares.append((p1, p2))

    for square in squares:
        grid_over_image = cv2.rectangle(preprocessed_image, tuple(int(x) for x in square[0]), tuple(int(y) for y in square[1]),
                            (150, 150, 255), 2)

    return (grid_over_image)
