import cv2 as cv

class FrameAnalysis():
    def __init__(self):
        self.supported_types = ['.avi', '.mp4', '.mov']
        uppercase_types = [type.upper() for type in self.supported_types]
        self.supported_types.extend(uppercase_types)

        # Initialize video capture object and frames per second (fps) value
        # They will be set/updated when a video file is inserted
        self.video_capture = None
        self.fps = 60

    # Checks if video capture is currently working
    def test_video_capture(self):
        assert self.video_capture, 'No video to capture'
        ret, _ = self.video_capture.read()
        if not ret:
            return False
        else:
            return True

    # Inserts a video file into de video capture object
    def insert_video_file(self, file:str):
        if not file.endswith(tuple(self.supported_types)):
            raise ValueError("Video format not supported.")
        else:
            self.video_capture = cv.VideoCapture(file)

            self.fps = self.video_capture.get(cv.CAP_PROP_FPS)
            if not self.fps or self.fps <= 0:
                self.fps = 60
    
    