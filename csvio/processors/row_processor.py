from typing import List, Type, Union

from ..utils.types import RP, R
from .processor_base import ProcessorBase


class RowProcessor(ProcessorBase):
    """
    :param handle: Reference handle for the field processor
    :type handle: required
    """

    def __init__(self, handle: str) -> None:

        super().__init__(handle)

    def add_processor_handle(self, handle: str) -> None:
        ProcessorBase.processors[handle] = []

    def add_processor(
        self, func_: Union[List[RP], RP], handle: str = None
    ) -> None:

        handle = handle or self.handle

        if not isinstance(func_, list):
            func_ = [func_]

        ProcessorBase.processors[handle].extend(func_)

    def process_row(
        self, row: R, processor_handle: Union[Type[ProcessorBase], str] = None
    ) -> R:

        applied_handle = processor_handle or self.handle

        if isinstance(applied_handle, ProcessorBase):
            applied_handle = applied_handle.handle

        processors = ProcessorBase.processors[str(applied_handle)]

        temp_row = row

        for processor_func in processors:
            temp_row = processor_func(temp_row)

        return temp_row
