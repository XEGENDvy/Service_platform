import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def shapes(photo):
    img = cv.imread(photo)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    _, thresh = cv.threshold(img_gray, 240, 255, cv.THRESH_BINARY)
    contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    white = np.ones((img.shape[0], img.shape[1], 3))

    identified_shapes = []

    for c in contours:
        approx = cv.approxPolyDP(c, 0.01*cv.arcLength(c, True), True)
        cv.drawContours(img, [approx], 0, (0, 255, 0), 5)
        x = approx.ravel()[0]
        y = approx.ravel()[1] - 5
        if len(approx) == 3:
            identified_shapes.append("Triangle")
            cv.putText(img, "Triangle", (x, y),
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
        elif len(approx) == 4:
            x1, y1, w, h = cv.boundingRect(approx)
            aspect_ratio = float(w) / float(h)
            print(aspect_ratio)
            if aspect_ratio >= 0.95 and aspect_ratio <= 1.05:
                identified_shapes.append("Square")
                cv.putText(img, "Square", (x, y),
                           cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
            else:
                identified_shapes.append("Rectangle")
                cv.putText(img, "Rectangle", (x, y),
                           cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
        elif len(approx) == 5:
            identified_shapes.append("Pentagon")
            cv.putText(img, "Pentagon", (x, y),
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
        elif len(approx) == 10:
            identified_shapes.append("Star")
            cv.putText(img, "Star", (x, y),
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
        else:
            identified_shapes.append("Circle")
            cv.putText(img, "Circle", (x, y),
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)

    print("Identified Shapes:", identified_shapes)
    rec=identified_shapes.count("Rectangle")
    cir=identified_shapes.count("Circle")
    if cir>rec:
        return 0
    else:
        return 1
    return identified_shapes
    cv.imshow("Shapes", img)
    cv.waitKey()
    cv.destroyAllWindows()

if __name__ == "__main__":
    shapes()
