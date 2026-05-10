"""
Examples of using the files hierarchy.

Demonstrates how to create, update, delete, and process files
using different storage backends.
"""

from homework_04 import (
    File,
    LocalStorage,
    S3Storage,
    FTPStorage,
    AudioFile,
    VideoFile,
    ImageFile,
)


# =============================================================================
# Example 1: Working with base File class
# =============================================================================

def example_base_file():
    """Create and manipulate a simple file."""
    storage = LocalStorage(base_path="/data")

    # Create a simple text/binary file
    file = File(
        name="notes.txt",
        storage=storage,
        path="documents/notes.txt",
        owner="user123",
    )

    # Basic operations
    file.load()
    file.save(b"Hello, world!")
    print(f"Size: {file.get_size()}, Created: {file.get_created_at()}")


# =============================================================================
# Example 2: Working with local storage
# =============================================================================

def example_local_storage():
    """Create and manipulate files on local filesystem."""
    storage = LocalStorage(base_path="/data/media")

    # Create a photo file
    photo = ImageFile(
        name="vacation.jpg",
        storage=storage,
        path="photos_lin_alg/2024/vacation.jpg",
        owner="user123",
        resolution=(1920, 1080),
        color_depth=24,
        image_format="jpg",
    )

    # Load and process
    photo.load()
    print(f"Photo: {photo.name}, format: {photo.image_format}")

    # Save changes
    photo.save()


# =============================================================================
# Example 3: Working with S3 storage
# =============================================================================

def example_s3_storage():
    """Work with files stored in S3."""
    storage = S3Storage(
        bucket="my-media-bucket",
        endpoint_url="https://s3.amazonaws.com",
        access_key="AKIAIOSFODNN7EXAMPLE",
        secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
    )

    # Create video file
    video = VideoFile(
        name="interview.mp4",
        storage=storage,
        path="videos/interviews/2024-01-15.mp4",
        owner="editor",
        duration=3600.0,
        resolution=(1920, 1080),
        fps=30.0,
        video_format="mp4",
    )

    # Load and get metadata
    video.load()
    print(f"Video: {video.name}, format: {video.video_format}")


# =============================================================================
# Example 4: Working with audio files
# =============================================================================

def example_audio_file():
    """Create and manipulate audio files."""
    storage = LocalStorage(base_path="/data/media")

    # Create audio file
    audio = AudioFile(
        name="podcast.mp3",
        storage=storage,
        path="audio/podcasts/ep001.mp3",
        owner="podcaster",
        duration=1800.0,
        bitrate=320,
        audio_format="mp3",
    )

    # Load and process
    audio.load()
    print(f"Audio: {audio.name}, format: {audio.audio_format}")

    # Convert to different format
    audio.convert("wav")
    print(f"Converted to: {audio.audio_format}")

# =============================================================================
# Example 6: FTP storage for remote files
# =============================================================================

def example_ftp_storage():
    """Work with files on remote FTP server."""
    ftp = FTPStorage(
        host="ftp.example.com",
        port=21,
        username="media_user",
        password="secret",
    )

    photo = ImageFile(
        name="remote_photo.jpg",
        storage=ftp,
        path="/uploads/photos_lin_alg/remote.jpg",
        owner="remote_user",
        resolution=(1920, 1080),
        color_depth=24,
        image_format="jpg",
    )

    # Download and process
    photo.load()
    print(f"Photo: {photo.name}, format: {photo.image_format}")

    # Convert to different format
    photo.convert("png")
    print(f"Converted to: {photo.image_format}")


if __name__ == "__main__":
    print("See examples above for usage patterns.")
