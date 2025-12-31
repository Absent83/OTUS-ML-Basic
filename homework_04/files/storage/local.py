from .base import Storage


class LocalStorage(Storage):
    """
    Storage backend for local filesystem.
    """

    def __init__(self, base_path: str = "."):
        """
        Initialize local storage.

        Args:
            base_path: Root directory for file storage.
        """
        self.base_path = base_path

    def read(self, path: str) -> bytes:
        """Read file from local filesystem."""
        pass

    def write(self, path: str, data: bytes) -> None:
        """Write file to local filesystem."""
        pass

    def delete(self, path: str) -> None:
        """Delete file from local filesystem."""
        pass

    def exists(self, path: str) -> bool:
        """Check if file exists."""
        pass

    def get_metadata(self, path: str) -> dict:
        """Get file metadata."""
        pass
