Row Processor
================

A Row Processor is used to transform the values of a row represented by
a dictionary that maps ``column->value`` pairs. This processor is used in
situations where you need to transform values of particular fields in a row
depending upon the values of some other fields within the same row.

In *csvio* a CSV file is represented by a list of dictionaries that is
populated in the ``rows`` attribute of the :py:class:`~csvio.CSVReader` or
:py:class:`~csvio.CSVWriter` Classes.

.. autoclass:: csvio.processors.row_processor.RowProcessor
    :show-inheritance:
    :members:
    :inherited-members:
