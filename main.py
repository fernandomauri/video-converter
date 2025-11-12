"""
Author: Fernando Mauri
Purpose: Convert a given video file and convert it to another format
"""

import logging
import os
from datetime import datetime

from handlers.video_processor import VideoHandler
from utils.spinner import spinner


logger = logging.getLogger(__name__)
logging.basicConfig(filename="run_history.log", format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO, filemode="w")

og_video = "videos/IMG_2956.mov"
without_extension = f"{og_video[:og_video.rfind('.')]}"
desired_extension = "mp4"

new_video = without_extension + '.' + desired_extension

processed_video = VideoHandler(og_video, new_video)


def main():
    """
    We'll first want to check if our input is a directory or a file. 
    If a directory, ignore. If a file, convert.
    """
    if os.path.isdir(og_video):
        logger.debug("The input just passed isn't a video. Skipping...")
    elif os.path.isfile(og_video):
        try:
            logger.info(f"Converting {os.path.basenane(without_extension)} to format {desired_extension}...")
            start = datetime.now()
            processed_video.convert_video()
            spinner()
            end = datetime.now()
        except Exception as e:
            logger.exception(f"Unable to convert your video to {desired_extension}. Error => {e}")
            raise
        else:
            logger.info(f"Your video {os.path.basename(without_extension)} successfully converted to {desired_extension}! Completed in {end - start}.")
    else:
        logger.error("No input exists. Exiting...")
        raise


if __name__ == "__main__":
    main()
