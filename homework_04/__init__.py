"""Homework 04: Files hierarchy."""

from .files import (
    Storage,
    LocalStorage,
    S3Storage,
    FTPStorage,
    File,
    AudioFile,
    VideoFile,
    ImageFile,
)

__all__ = [
    "Storage",
    "LocalStorage",
    "S3Storage",
    "FTPStorage",
    "File",
    "AudioFile",
    "VideoFile",
    "ImageFile",
]
