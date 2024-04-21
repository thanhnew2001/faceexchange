import cv2

def resize_image(image, scale_ratio):
    """
    Resizes the image by a given scale ratio.

    Parameters:
        image (numpy.ndarray): The image to resize, as a NumPy array.
        scale_ratio (float): The factor by which the image should be resized.

    Returns:
        numpy.ndarray: The resized image.
    """
    # Calculate the new dimensions
    new_width = int(image.shape[1] * scale_ratio)
    new_height = int(image.shape[0] * scale_ratio)
    
    # Resize the image
    resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
    
    return resized_image

# Example usage
img = cv2.imread('images/tam.jpg')  # Replace 'path_to_your_image.jpg' with your image file path
scale_ratio = 0.5  # Example: resize to 50% of the original size
resized_image = resize_image(img, scale_ratio)

cv2.imwrite("images/tam_resized.jpg", resized_image)
