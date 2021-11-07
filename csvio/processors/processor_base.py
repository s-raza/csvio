from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, Type, Union

from ..utils.types import RS, R


class ProcessorBase(ABC):
    """
    Processor Base Class
    """

    processors: Dict[str, Any] = {}

    def __init__(self, handle: str) -> None:

        self.handle: str = handle
        self.add_processor_handle(handle)

    @abstractmethod
    def add_processor_handle(self, handle: str) -> None:
        pass

    @abstractmethod
    def process_row(
        self, row: R, processor_handle: Union[Type[ProcessorBase], str] = None
    ) -> R:
        pass

    def process_rows(self, rows: RS, processor_handle: str = None) -> RS:
        """
        Process a list of rows

        :param row: A list of dictionaries of ``fieldname->value`` pairs
            representing a list of rows
        :type row: required

        :param processor_handle: A processor handle or an object that
            references the processor functions to apply and transform the row
            values. The processor functions of the current object are used if
            this argument is not provided.
        :type processor_handle: optional

        :return: A list of dictionaries representing processed CSV rows

        """
        return [self.process_row(row, processor_handle) for row in rows]
