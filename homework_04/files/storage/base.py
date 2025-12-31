class Storage:
    """
    Base class for file storage backends.
    """

    def read(self, path: str) -> bytes:
        """Read file content from storage."""
        pass

    def write(self, path: str, data: bytes) -> None:
        """Write data to file in storage."""
        pass

    def delete(self, path: str) -> None:
        """Delete file from storage."""
        pass

    def exists(self, path: str) -> bool:
        """Check if file exists in storage."""
        pass

    def get_metadata(self, path: str) -> dict:
        """
        Get file metadata from storage.

        Returns dict with keys: size, created_at, modified_at, etc.
        """
        pass
