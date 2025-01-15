import cv2
import src.argument_parser
from src.video_stream import VideoStreamProcessor

def main():
    """
    Main function to handle argument parsing and start video processing. 
    """

    # Parse command line arguments
    parser = src.argument_parser.prepare_parser()
    args = parser.parse_args()

    colormaps = {
        "TURBO": cv2.COLORMAP_TURBO,
        "JET": cv2.COLORMAP_JET,
        "HOT": cv2.COLORMAP_HOT,
        "COOL": cv2.COLORMAP_COOL,
        "SPRING": cv2.COLORMAP_SPRING,
        "WINTER": cv2.COLORMAP_WINTER,
        "RAINBOW": cv2.COLORMAP_RAINBOW,
        "OCEAN": cv2.COLORMAP_OCEAN,
        "BONE": cv2.COLORMAP_BONE,
        "HSV": cv2.COLORMAP_HSV,
        "PARULA": cv2.COLORMAP_PARULA,
        # Add more mappings as needed
    }

    # Initialize the VideoStreamProcessor
    video_processor = VideoStreamProcessor(
        video_file=args.video_file,
        video_output=args.video_output,
        video_skip=args.video_skip,
        take_every=args.take_every,
        video_alpha=args.video_alpha,
        video_disable=args.video_disable,
        colormap=colormaps[args.cmap]
    )

    # Start processing the video
    video_processor.process_video()

if __name__ == '__main__':
    main()
