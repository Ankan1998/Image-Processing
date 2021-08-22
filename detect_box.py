def detect_box(image, cropIt=True):

    # Transform colorspace to YUV
    image_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_y = np.zeros(image_yuv.shape[0:2], np.uint8)
    image_y[:, :] = image_yuv[:, :]

    # Blur to filter high frequency noises
    image_blurred = cv2.GaussianBlur(image_y, (3, 3), 0)

    # Apply canny edge-detector
    #edges = cv2.Canny(image_blurred, 100, 300, apertureSize=3)
    contours, _ = cv2.findContours(image_blurred, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Remove large countours
    new_contours = []
    for c in contours:
        if cv2.contourArea(c) < 400000:
            new_contours.append(c)

    # Get overall bounding box
    best_box = [-1, -1, -1, -1]
    for c in new_contours:
        x, y, w, h = cv2.boundingRect(c)
        if best_box[0] < 0:
            best_box = [x, y, x + w, y + h]
        else:
            if x < best_box[0]:
                best_box[0] = x
            if y < best_box[1]:
                best_box[1] = y
            if x + w > best_box[2]:
                best_box[2] = x + w
            if y + h > best_box[3]:
                best_box[3] = y + h


    if (cropIt):
        image = image[best_box[1]:best_box[3], best_box[0]:best_box[2]]

    return image