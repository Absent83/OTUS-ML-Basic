from datetime import datetime

from ..storage.base import Storage


class File:
    """
    Base class for files.
    """

    def __init__(
            self,
            name: str,
            storage: Storage,
            path: str,
            owner: str,
    ):
        """
        Initialize file.
        """
        self.name = name
        self._storage = storage
        self.path = path
        self.owner = owner
        self._data: bytes = b""

    def get_size(self) -> int:
        """Get file size in bytes from storage metadata."""
        return self._storage.get_metadata(self.path).get("size", 0)

    def get_created_at(self) -> datetime:
        """Get file creation timestamp from storage metadata."""
        return self._storage.get_metadata(self.path).get("created_at")

    def load(self) -> bytes:
        """Load file content from storage into memory."""
        self._data = self._storage.read(self.path)
        return self._data

    def save(self, data: bytes = b"") -> None:
        """Save file content to storage."""
        self._data = data
        self._storage.write(self.path, self._data)

    def delete(self) -> None:
        """Delete file from storage."""
        self._storage.delete(self.path)
        self._data = b""

    def exists(self) -> bool:
        """Check if file exists in storage."""
        return self._storage.exists(self.path)
