import cv2 as cv


class VideoReader:
    def __init__(self, filename):
        self.current_frame = 0
        self.video = cv.VideoCapture(filename)
        self.fps = self.video.get(cv.CAP_PROP_FPS)


    def nextFrame(self):
        ret, frame = self.video.read()
        return frame


    def seek(self, pos):
        self.current_frame = pos * self.fps
        self.video.set(cv.CAP_PROP_POS_FRAMES, self.current_frame)
