class RemoteResourceError(Exception):
    """Raised when access to the remote resource fails"""

    def __init__(
        self, remote_type: str, msg: str = "Remote resource error"
    ) -> None:

        self.remote_type = remote_type
        self.msg = msg

    def __str__(self) -> str:
        return f"{self.remote_type}: {self.msg}"
