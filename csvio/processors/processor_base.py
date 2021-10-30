from __future__ import annotations

from typing import Dict, List, Type, Union

from ..utils.types import PF, RS, R


class ProcessorBase:

    processors: Dict[str, Dict[str, List[PF]]] = {}

    def __init__(self, handle: str) -> None:

        self.handle: str = handle
        self.add_processor_handle(handle)

    def add_processor_handle(self, handle: str) -> None:
        ProcessorBase.processors[handle] = {}

    def add_processor(
        self, fieldname: str, func_: Union[List[PF], PF], handle: str = None
    ) -> None:

        handle = handle or self.handle

        if not isinstance(func_, list):
            func_ = [func_]

        ProcessorBase.processors[handle].setdefault(fieldname, []).extend(
            func_
        )

    def process_row(
        self, row: R, processor_handle: Union[Type[ProcessorBase], str] = None
    ) -> R:

        applied_handle = processor_handle or self.handle

        if isinstance(applied_handle, ProcessorBase):
            applied_handle = applied_handle.handle

        processors = ProcessorBase.processors[str(applied_handle)]

        ret_row: R = {}

        for field, data in row.items():
            if field in processors:
                ret_field = data
                for processor in processors[field]:
                    ret_field = processor(ret_field)
                ret_row[field] = ret_field
            else:
                ret_row[field] = data

        return ret_row

    def process_rows(self, rows: RS, processor_handle: str = None) -> RS:
        return [self.process_row(row, processor_handle) for row in rows]
