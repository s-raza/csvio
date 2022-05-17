import tempfile
import time
from abc import ABC, abstractmethod
from typing import List

from ..csvreader import CSVReader
from ..processors.processor_base import ProcessorBase
from ..utils.types import FN, KW


class RemoteReaderBase(CSVReader, ABC):
    """
    Base class for remote readers.

    All remote readers are derived from this class and should implement the
    :py:func:`~csvio.remote.remote_base.RemoteReaderBase._csv_downloader`
    abstract method at a minimum.

    :param options: Options that are to be used by the downloader child class
        that is derived from this base class
    :type options: required
    """

    def __init__(
        self,
        options: KW,
        processors: List[ProcessorBase] = None,
        fieldnames: FN = [],
        open_kwargs: KW = {},
        csv_kwargs: KW = {},
        max_retries: int = 3,
        timeout: int = 5,
        increment_timeout: int = 10,
    ) -> None:

        self.max_retries = max_retries
        self.timeout = timeout
        self.increment_timeout = increment_timeout

        self.temp_path = self.get_temp_path()

        self.options = options
        filename = self.__download()

        super().__init__(
            filename, processors, fieldnames, open_kwargs, csv_kwargs
        )

    @property
    @abstractmethod
    def remote_type(self) -> str:
        pass

    def get_temp_path(self) -> str:
        """
        :return: Full path to a randomly named `csv` file in the system's
            temporary directory.
        """
        return f"{tempfile.NamedTemporaryFile().name}.csv"

    @abstractmethod
    def _csv_downloader(self) -> str:
        """
        To be implemented by all child classes.

        This method should implement the remote file downloader and return the
        complete path to the downloaded file. The ``temp_path`` attribute can
        be used when implementing this method
        """
        pass

    def __download(self) -> str:
        """
        Downloader method that uses the
        :py:func:`~csvio.remote.remote_base.RemoteReaderBase._csv_downloader`
        concrete method that is implemeneted in a remote downloader child
        class.

        This method attempts retries as defined by the ``max_retries``, ``timeout``
        and ``increment_timeout`` attributes.
        """
        try:
            downloaded_path = self._csv_downloader()
        except Exception as e:

            if self.max_retries > 0:
                print(
                    f"{e}: Retry retrieving remote file in {self.timeout}s, "
                    f"{self.max_retries} attempts left"
                )

                time.sleep(self.timeout)
                self.max_retries -= 1
                self.timeout += self.increment_timeout
                self.__download()
            else:
                raise TimeoutError(
                    "Max retries to access remote resource exhausted"
                )

        return downloaded_path
