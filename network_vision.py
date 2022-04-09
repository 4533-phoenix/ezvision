import networktables
import numpy
import json
import abc
import cv2

networktables.NetworkTables.initialize()

class BaseVision(abc.ABC):
    def __init__(self, url, table_name):
        self.url = url
        self.table_name = table_name
        
        self.capture = cv2.VideoCapture(url)
        self.table = networktables.NetworkTables.getTable(table_name)

        self.output = {}

    def put(self):
        for key, value in self.output.items():
            if isinstance(value, (str)):
                self.table.putString(key, value)
            elif isinstance(value, (int, float, complex)):
                self.table.putNumber(key, value)
            elif isinstance(value, (list, tuple, dict)):
                self.table.putString(key, json.dumps(value))
            elif isinstance(value, (bool)):
                self.table.putBoolean(key, value)
            else:
                self.table.putString(key, str(value))

    def visualize(self):
        pass

    def update(self):
        self.visualize()
        self.put()

class ColoredBallsVision(BaseVision):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.output = {
            "red": [],
            "blue": []
        }
        self.put()

        self.bright_red_lower = numpy.array([0, 100, 100])
        self.bright_red_upper = numpy.array([10, 255, 255])

        self.dark_red_lower = numpy.array([160, 100, 100])
        self.dark_red_upper = numpy.array([179, 255, 255])

        self.blue_lower = numpy.array([100,50,50])
        self.blue_upper = numpy.array([130,255,255])

    def get_red(self, frame):
        hsv_conv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        bright_red_mask = cv2.inRange(hsv_conv_img, self.bright_red_lower, self.bright_red_upper)
        dark_red_mask = cv2.inRange(hsv_conv_img, self.dark_red_lower, self.dark_red_upper)

        weighted_mask = cv2.addWeighted(bright_red_mask, 1.0, dark_red_mask, 1.0, 0.0)
        blurred_mask = cv2.GaussianBlur(weighted_mask, (9, 9), 3, 3)

        erode_element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        dilate_element = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
        eroded_mask = cv2.erode(blurred_mask, erode_element)
        dilated_mask = cv2.dilate(eroded_mask, dilate_element)

        return dilated_mask

    def get_blue(self, frame):
        hsv_conv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        blue_mask = cv2.inRange(hsv_conv_img, self.blue_lower, self.blue_upper)

        blurred_mask = cv2.GaussianBlur(blue_mask, (9, 9), 3, 3)

        erode_element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        dilate_element = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
        eroded_mask = cv2.erode(blurred_mask, erode_element)
        dilated_mask = cv2.dilate(eroded_mask, dilate_element)

        return dilated_mask

    def calculate(self, frame, red_circles, blue_circles):
        width, height = frame.shape[0:2]

        if red_circles is not None: red_circles = red_circles[0, :]
        else: red_circles = []

        if blue_circles is not None: blue_circles = blue_circles[0, :]
        else: blue_circles = []

        red_circles = [{"x": red_circle[0], "y": red_circle[1], "r": red_circle[2], "relx": width / 2 - red_circle[0], "rely": height / 2 - red_circle[1]} for red_circle in red_circles]
        blue_circles = [{"x": blue_circle[0], "y": blue_circle[1], "r": blue_circle[2], "relx": width / 2 - blue_circle[0], "rely": height / 2 - blue_circle[1]} for blue_circle in blue_circles]

        return {"red": red_circles, "blue": blue_circles}

    def visualize(self):
        success, frame = self.capture.read()
        if not success: return

        red_mask = self.get_red(frame)
        blue_mask = self.get_blue(frame)

        red_inverted = cv2.bitwise_not(red_mask)
        blue_inverted = cv2.bitwise_not(blue_mask)

        red_circles = cv2.HoughCircles(red_inverted, cv2.HOUGH_GRADIENT, 1.2, 100)
        blue_circles = cv2.HoughCircles(blue_inverted, cv2.HOUGH_GRADIENT, 1.2, 100)

        self.output = self.calculate(frame, red_circles, blue_circles)