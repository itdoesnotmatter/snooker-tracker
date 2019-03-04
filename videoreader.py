import cv2 as cv


class VideoReader:
    def __init__(self, filename, process_fps=1):
        self.current_frame = 0
        self.video = cv.VideoCapture(filename)
        self.fps = self.video.get(cv.CAP_PROP_FPS)
        self.process_fps = process_fps if process_fps != None else 1


    def next_frame(self):
        _, frame = self.video.read()
        frame_no = self.current_frame + int(self.fps / self.process_fps)
        self.seek_frame(frame_no)

        return frame_no, frame


    def seek(self, pos):
        self.seek_frame(int(pos * self.fps))


    def seek_frame(self, frame_no):
        self.current_frame = frame_no
        self.video.set(cv.CAP_PROP_POS_FRAMES, self.current_frame)
