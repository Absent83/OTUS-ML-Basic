"""Video file class."""

from .base import File
from ..storage.base import Storage


class VideoFile(File):
    """
    Video file representation.
    """

    def __init__(
            self,
            name: str,
            storage: Storage,
            path: str,
            owner: str,
            duration: float,
            resolution: tuple[int, int],
            fps: float,
            video_format: str,
    ):
        super().__init__(name, storage, path, owner)
        self.duration = duration  # seconds
        self.resolution = resolution  # (width, height)
        self.fps = fps  # frames per second
        self.video_format = video_format  # e.g., 'mp4', 'webm', 'avi', 'mkv'

    def get_metadata(self) -> dict:
        """Return video metadata: duration, resolution, fps, codec."""
        pass

    def convert(self, target_format: str) -> None:
        """Convert video to another format (mp4, webm, avi, mkv)."""
        self.video_format = target_format
