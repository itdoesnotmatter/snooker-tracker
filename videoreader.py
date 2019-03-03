import cv2 as cv


class VideoReader:
    def __init__(self, filename):
        self.current_frame = 0
        self.video = cv.VideoCapture(filename)
        self.fps = self.video.get(cv.CAP_PROP_FPS)
        self.process_fps = 1


    def nextFrame(self):
        _, frame = self.video.read()
        pos = int(self.current_frame / self.fps) + self.process_fps
        self.seek(pos)

        return pos, frame


    def seek(self, pos):
        self.current_frame = int(pos * self.fps)
        self.video.set(cv.CAP_PROP_POS_FRAMES, self.current_frame)
