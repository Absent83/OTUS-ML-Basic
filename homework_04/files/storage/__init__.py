from .base import Storage
from .ftp import FTPStorage
from .local import LocalStorage
from .s3 import S3Storage

__all__ = [
    "Storage",
    "LocalStorage",
    "S3Storage",
    "FTPStorage",
]
