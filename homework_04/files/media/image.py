"""Photo file class."""

from .base import File
from ..storage.base import Storage


class ImageFile(File):
    """
    Photo/image file representation.
    """

    def __init__(
            self,
            name: str,
            storage: Storage,
            path: str,
            owner: str,
            resolution: tuple[int, int],
            color_depth: int,
            image_format: str,
    ):
        super().__init__(name, storage, path, owner)
        self.resolution = resolution  # (width, height)
        self.color_depth = color_depth  # bits per pixel
        self.image_format = image_format  # e.g., 'jpg', 'png', 'webp', 'gif'

    def get_metadata(self) -> dict:
        """Return photo metadata: resolution, color_depth, exif."""
        pass

    def convert(self, target_format: str) -> None:
        """Convert image to another format (jpg, png, webp, gif)."""
        self.image_format = target_format

    def resize(self, width: int, height: int) -> bytes:
        """Resize image to specified dimensions."""
        pass

    def crop(self, x: int, y: int, width: int, height: int) -> bytes:
        """Crop image to specified region."""
        pass
