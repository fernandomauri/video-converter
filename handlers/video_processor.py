import ffmpeg


class VideoHandler():
    """
    We'll have an extensible handler here for future features and modularity
    """
    def __init__(self, og_video, new_video):
        self.og_video = og_video
        self.new_video = new_video

    
    def convert_video(self):
        video_to_convert = ffmpeg.input(self.og_video)
        converted_video = ffmpeg.output(video_to_convert, self.new_video)
        ffmpeg.run(converted_video)
