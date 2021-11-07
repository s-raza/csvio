from typing import List, Type, Union

from ..utils.types import RP, R
from .processor_base import ProcessorBase


class RowProcessor(ProcessorBase):
    """
    :param handle: Reference handle for the row processor
    :type handle: required
    """

    def __init__(self, handle: str) -> None:

        super().__init__(handle)

    def add_processor_handle(self, handle: str) -> None:
        ProcessorBase.processors[handle] = []

    def add_processor(
        self, func_: Union[List[RP], RP], handle: str = None
    ) -> None:
        """
        Add a processor function to process rows.

        The processor function reference is essentially a callback function
        that accepts a single argument that represents a row.

        The ``fieldnames`` from a CSV can be used within this callback function
        as the keys to this single argument that represents a row to access its
        values and perform the required transformations. This callback function
        should return a dictionary representing a row, once all the required
        transformations are applied.

        :param func_: Row processor callback function reference or a list of such
            function references.
            All function references added with the same handle will be executed
            for the row, to transform its value in the same order as they are
            added. A single processor function will be sufficient to
            perform all the transformations for the rows in a CSV, if it has
            all the transformation operations required in its definition.
        :type func_: required

        :param handle: Processor reference handle to which the processor will
            be added.
            If not provided, the handle of the current object will be used.
        :type handle: optional

        :return: None

        See :ref:`example code <csvreader_processors_usage>` for using with
        :py:class:`~csvio.CSVReader`

        See :ref:`example code <csvwriter_processors_usage>` for using with
        :py:class:`~csvio.CSVWriter`

        """

        handle = handle or self.handle

        if not isinstance(func_, list):
            func_ = [func_]

        ProcessorBase.processors[handle].extend(func_)

    def process_row(
        self, row: R, processor_handle: Union[Type[ProcessorBase], str] = None
    ) -> R:
        """
        Process a single row.

        This applies the processors defined using the
        :py:func:`~csvio.processors.row_processor.RowProcessor.add_processor`
        function in the same order that they were added using
        :py:func:`~csvio.processors.row_processor.RowProcessor.add_processor`

        The output row after application of the previous processor function
        is passed on to the next processor function that was added using
        :py:func:`~csvio.processors.row_processor.RowProcessor.add_processor`,
        and the output of the last processor function added is returned as the
        final output of this function.

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

        temp_row = dict(row)

        for processor_func in processors:
            temp_row = processor_func(temp_row)

        return temp_row
