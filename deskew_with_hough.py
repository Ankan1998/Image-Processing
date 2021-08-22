def deskewer_h(img):

    img_shape = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blank = np.uint8(np.zeros((img_shape[0], img_shape[1])))
    skernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
    ret2, th2 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    opening = cv2.morphologyEx(th2, cv2.MORPH_OPEN, skernel)
    erosion = cv2.erode(opening, skernel)
    edges = cv2.Canny(erosion, 100, 300, apertureSize=3)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 230, minLineLength=300, maxLineGap=70)
    lines1 = lines[:, 0, :]
    Theta = []
    for x1, y1, x2, y2 in lines1[:]:
        cv2.line(blank, (x1, y1), (x2, y2), (255, 255, 255), 5)
        theta = math.atan2(y1 - y2, x2 - x1)
        Theta.append(theta * 180 / np.pi)
    angle_i = np.histogram(Theta, bins=90)[0].tolist()
    angle_m = angle_i.index(max(angle_i))
    angle = np.histogram(Theta, bins=90)[1].tolist()
    height, width = img.shape[:2]
    degree = angle[angle_m] * -1
    heightNew = int(
        width * math.fabs(math.sin(math.radians(degree))) + height * math.fabs(math.cos(math.radians(degree))))
    widthNew = int(
        height * math.fabs(math.sin(math.radians(degree))) + width * math.fabs(math.cos(math.radians(degree))))
    M = cv2.getRotationMatrix2D((width / 2, height / 2), degree, 1)
    M[0, 2] += (widthNew - width) / 2
    M[1, 2] += (heightNew - height) / 2
    res = cv2.warpAffine(img, M, (widthNew, heightNew))

    return res