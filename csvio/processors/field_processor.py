from typing import List, Type, Union

from ..utils.types import FP, R
from .processor_base import ProcessorBase


class FieldProcessor(ProcessorBase):
    """
    :param handle: Reference handle for the field processor
    :type handle: required
    """

    def __init__(self, handle: str) -> None:

        super().__init__(handle)

    def add_processor(
        self, fieldname: str, func_: Union[List[FP], FP], handle: str = None
    ) -> None:

        """
        Add a processor to process fields in a row.

        :param fieldname: Name of the field upon which the processor should be
            executed.
        :type fieldname: required

        :param func_: Field processor function reference or a list of such
            function references.
            All function references added with the same handle will be executed
            for the field, to transform its value in the same order as they are
            added.
        :type func_: required

        :param handle: Processor reference handle to which the processor will
            be added.
            If not provided, the handle of the current object will be used.
        :type handle: optional

        :return: None

        See :ref:`example code <csvreader_fp_usage>` for using with
        :py:class:`~csvio.CSVReader`

        See :ref:`example code <csvwriter_fp_usage>` for using with
        :py:class:`~csvio.CSVWriter`

        """

        handle = handle or self.handle

        if not isinstance(func_, list):
            func_ = [func_]

        ProcessorBase.processors[handle].setdefault(fieldname, []).extend(
            func_
        )

    def process_row(
        self, row: R, processor_handle: Union[Type[ProcessorBase], str] = None
    ) -> R:
        """
        Process a single row

        :param row: A single dictionary of ``fieldname->value`` pairs
            representing a single row
        :type row: required

        :param processor_handle: A processor handle or an object that
            references the processor functions to apply and transform the row
            values. The processor functions of the current object are used if
            this argument is not provided.
        :type processor_handle: optional

        :return: A dictionary representing a processed CSV row

        """

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
