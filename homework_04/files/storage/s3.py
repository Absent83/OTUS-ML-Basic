from .base import Storage


class S3Storage(Storage):
    """
    Storage backend for S3-compatible services.
    """

    def __init__(
            self,
            bucket: str,
            endpoint_url: str,
            access_key: str,
            secret_key: str,
    ):
        """
        Initialize S3 storage.

        Args:
            bucket: S3 bucket name.
            endpoint_url: Custom endpoint for S3-compatible services.
            access_key: AWS access key ID.
            secret_key: AWS secret access key.
        """
        self.bucket = bucket
        self.endpoint_url = endpoint_url
        self.access_key = access_key
        self.secret_key = secret_key
        self._client = None  # boto3.client('s3', pass)

    def read(self, path: str) -> bytes:
        """Read file from S3."""
        pass

    def write(self, path: str, data: bytes) -> None:
        """Write file to S3."""
        pass

    def delete(self, path: str) -> None:
        """Delete file from S3."""
        pass

    def exists(self, path: str) -> bool:
        """Check if file exists."""
        pass

    def get_metadata(self, path: str) -> dict:
        """Get file metadata."""
        pass

    def get_presigned_url(self, path: str, expires_in: int) -> str:
        """Generate presigned URL for temporary file access."""
        pass
