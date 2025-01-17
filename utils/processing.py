import cv2
import numpy as np
from typing import Tuple

# Background Subtractor
BG_SUB = cv2.createBackgroundSubtractorKNN()

def remove_background(frame: np.ndarray) -> np.ndarray:
    """ Removes background from a frame.

    Args:
        frame (np.array): Array representing the frame.

    Returns:
        np.ndarray: Background-less frame.

    """

    # Subtracts the background from the frame
    frame = BG_SUB.apply(frame)

    return frame


def apply_colormap(frame: np.ndarray, colormap: int = cv2.COLORMAP_TURBO) -> np.ndarray:
	""" Apply colors for heatmap visualisation.

    Args:
        frame (np.ndarray): Image for which heatmap colors should be applied.
        colormap (int): Colormap that is going to be applied (Default: cv2.COLORMAP_TURBO)
    
    Returns:
        np.ndarray: Image with applied heatmap colors.

    """
	return cv2.applyColorMap(frame, colormap)


def superimpose(frame1: np.ndarray, frame2: np.ndarray, alpha: float = 0.5) -> np.ndarray:
    """ Superimpose two images with given alpha values.

    Args:
        frame1 (np.ndarray): First frame to apply for superimpose operation.
        frame2 (np.ndarray): Second frame to apply for superimpose operation.
        alpha (float): Alpha of the first frame. Second frame gets 1 - alpha.

    Returns:
        np.ndarray: frame after superimpose operation of frame1 and frame2.

    """

    return cv2.addWeighted(frame1, alpha, frame2, 1 - alpha, 0.0)


def apply_morph(image: np.ndarray, morph_type=cv2.MORPH_CLOSE, kernel_size: Tuple[int, int] = (3, 3), make_gaussian: bool = True):
    """ Apply opencv morphological operation to image and return it.

    Args:
        image (np.ndarray): Source image for which function will apply morhpological operation.
        morph_type: Opencv morphological operation type. Should start with cv2.MORH_.
        kernel_size (Tuple[int, int]): Tuple of ints, representing size of kernel for
            morphological operation.
        make_gaussian (bool): Tells if we apply gaussian blur. Recommended to use for most videos.

    Returns:
        Source image with applied chosen morphological operation.

    """

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    if make_gaussian:
        image = cv2.GaussianBlur(image, (3, 3), 0)
    return cv2.morphologyEx(image, morph_type, kernel)


def add_images(image1: np.ndarray, image2: np.ndarray) -> np.ndarray:
    """ Add two images together. Colors values can be bigger then 255 restriction.

    Args:
        image1 (np.ndarray): First image to add.
        image2 (np.ndarray): Second image to add.

    Returns:
        np.ndarray: Output image represeting addition of image1 and image2.

    """

    return np.array(image1, dtype=np.uint64) + np.array(image2, dtype=np.uint64)


def normalize_image(image: np.ndarray) -> np.ndarray:
    """ Normalize image to 0-255 range, so it is viewed correctly.

    Args:
        image (np.ndarray): Image for which normalization should be applied.

    Returns:
        np.ndarray: Normalized image.

    """

    return cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
