from .base import File
from ..storage.base import Storage


class AudioFile(File):

    def __init__(
            self,
            name: str,
            storage: Storage,
            path: str,
            owner: str,
            duration: float,
            bitrate: int,
            audio_format: str,
    ):
        super().__init__(name, storage, path, owner)
        self.duration = duration  # seconds
        self.bitrate = bitrate  # kbps
        self.audio_format = audio_format  # e.g., 'mp3', 'wav', 'ogg', 'flac'

    def get_metadata(self) -> dict:
        """Return audio metadata: format, duration, bitrate"""
        pass

    def convert(self, target_format: str) -> None:
        """Convert audio to another format (mp3, wav, ogg, flac)."""
        self.audio_format = target_format
