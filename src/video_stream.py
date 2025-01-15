import cv2
import numpy as np
from utils.processing import *


class VideoStreamProcessor:
    def __init__(self, video_file, video_output, video_skip=10, take_every=1, video_alpha=0.7, colormap=cv2.COLORMAP_TURBO, video_disable=False):
        self.video_file = video_file
        self.video_output = video_output
        self.video_skip = video_skip
        self.take_every = take_every
        self.video_alpha = video_alpha
        self.video_disable = video_disable
        self.colormap = colormap

        # Open the video capture object
        self.capture = cv2.VideoCapture(self.video_file)
        
        if not self.capture.isOpened():
            raise ValueError(f"Unable to open video file: {self.video_file}")

        # Read the first frame to get dimensions
        self.read_succes, self.video_frame = self.capture.read()
        if not self.read_succes:
            raise ValueError(f"Unable to read the first frame from video file: {self.video_file}")
        
        self.height, self.width, _ = self.video_frame.shape
        self.frames_number = int(self.capture.get(cv2.CAP_PROP_FRAME_COUNT))

        # Initialize the video writer
        fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
        self.video_writer = cv2.VideoWriter(self.video_output + ".mp4", fourcc, 30.0, (self.width, self.height))
        self.accumulated_image = np.zeros((self.height, self.width), np.uint8)
        self.count = 0

    def process_frame(self):
        """
        Process the video frame by applying background subtraction, generating heatmap, etc.
        """
        
        # Apply background subtraction
        background_filter = remove_background(self.video_frame)
        
        # Process frames based on skipping and taking every N-th frame
        if self.count > self.video_skip and self.count % self.take_every == 0:
            eroded_image = apply_morph(background_filter, morph_type=cv2.MORPH_ERODE, kernel_size=(5, 5))
            self.accumulated_image = add_images(self.accumulated_image, eroded_image)
            normalized_image = normalize_image(self.accumulated_image)
            heatmap_image = apply_colormap(normalized_image, self.colormap)
            frames_merged = superimpose(heatmap_image, self.video_frame, float(self.video_alpha))

            # Display the processed frame in real-time if the flag is set
            if not self.video_disable:
                cv2.imshow("Main", frames_merged)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    return False

            # Write the processed frame to the output video
            self.video_writer.write(frames_merged)
            if self.count % 100 == 0:
                print(f"Progress: {self.count}/{self.frames_number}")
        return True

    def process_video(self):
        """
        Process the video by reading, processing, and writing each frame.
        """
        while self.read_succes:
            self.read_succes, self.video_frame = self.capture.read()
            if self.read_succes:
                if not self.process_frame():
                    break
                self.count += 1

        self.capture.release()
        self.video_writer.release()
        cv2.destroyAllWindows()
