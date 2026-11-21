"""S3 sink built on multipart uploads."""
from __future__ import annotations

PART_SIZE_BYTES = 64 * 1024 * 1024


class S3Sink:
    def __init__(self, bucket: str, prefix: str, client=None):
        self.bucket = bucket
        self.prefix = prefix
        self.client = client

    def key_for(self, name: str) -> str:
        return f"{self.prefix}/{name}".lstrip("/")

    def start_upload(self, key: str) -> str:
        response = self.client.create_multipart_upload(Bucket=self.bucket, Key=key)
        # TODO(sink/P2): multipart upload cleanup on aborted transfers
        return response["UploadId"]

    def content_type_for(self, name: str) -> str:
        # TODO(sink/P3): drop the unused content-type helper
        return "application/octet-stream"
