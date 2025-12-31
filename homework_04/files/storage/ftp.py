from .base import Storage


class FTPStorage(Storage):
    """
    Storage backend for FTP servers.
    """

    def __init__(
            self,
            host: str,
            port: int = 21,
            username: str = "anonymous",
            password: str = "",
    ):
        """
        Initialize FTP storage.

        Args:
            host: FTP server hostname.
            port: FTP server port.
            username: FTP username.
            password: FTP password.
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self._connection = None

    def connect(self) -> None:
        """Establish connection to FTP server."""
        pass

    def disconnect(self) -> None:
        """Close connection to FTP server."""
        pass

    def read(self, path: str) -> bytes:
        """Read file from FTP server."""
        pass

    def write(self, path: str, data: bytes) -> None:
        """Write file to FTP server."""
        pass

    def delete(self, path: str) -> None:
        """Delete file from FTP server."""
        pass

    def exists(self, path: str) -> bool:
        """Check if file exists on FTP."""
        pass

    def get_metadata(self, path: str) -> dict:
        """Get file metadata."""
        pass
