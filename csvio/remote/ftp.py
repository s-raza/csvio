import ftplib

from ..errors import RemoteResourceError
from .remote_base import RemoteReaderBase


class FTPReader(RemoteReaderBase):
    """
    Download CSV file from a FTP location.

    :param options: Options that are to be used by the downloader child class
        that is derived from this base class
    :type options: required

    The ``options`` parameter to the constructor of this class accepts a
    dictionary with the options to download a CSV file from a FTP location

    Example FTP options dictionary:

    .. code-block:: python

        {
            "hostname": "localhost",
            "username": "ftp_user",
            "password": "ftp_pass",
            "remote_dir": "data/csv_files"
            "remote_file": "products.csv"
        }

    Example CSV download from FTP:

    .. include:: /examples/csvio.ftp.rst
    """

    @property
    def remote_type(self) -> str:
        return "FTP"

    def _csv_downloader(self) -> str:

        try:
            with ftplib.FTP(
                self.options["hostname"],
                self.options["username"],
                self.options["password"],
            ) as ftp:

                ftp.cwd(self.options["remote_dir"])

                with open(self.temp_path, "wb") as f:
                    ftp.retrbinary(
                        "RETR " + self.options["remote_file"], f.write
                    )
        except ftplib.all_errors:
            raise RemoteResourceError(self.remote_type)

        return self.temp_path
