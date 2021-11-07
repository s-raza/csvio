Row Processor
================

A Row Processor is used to transform the values of a row represented by
a dictionary that maps ``column->value`` pairs. This processor is used in
situations where you need to transform values of particular fields in a row
depending upon the values of some other fields within the same row.

In *csvio* a CSV file is represented by a list of dictionaries that is
populated in the ``rows`` attribute of the :py:class:`~csvio.CSVReader` or
:py:class:`~csvio.CSVWriter` Classes.

Once instantiated, a Row Processor Object can be used by itself to process an
arbitrary dictionary that represents a row or can be passed to the constructors
of :doc:`CSVReader <csvio.csvreader>` or :doc:`CSVWriter <csvio.csvwriter>`.

In the case where a Row Processor Object is passed to the constructor of
:doc:`CSVReader <csvio.csvreader>`, it is applied to the rows of the
:doc:`CSVReader <csvio.csvreader>` as soon as they are read from the CSV file.
See :ref:`example code <csvreader_processors_usage>` for further details.

Similarly, in the case where a Row Processor Object is passed to the
constructor of :doc:`CSVWriter <csvio.csvwriter>`, it is applied to the rows of
the :doc:`CSVWriter <csvio.csvwriter>` as soon as they are added for writing to
the output CSV using its :py:func:`~csvio.CSVWriter.add_rows` method.
See :ref:`example code <csvwriter_processors_usage>` for further details.

.. _standalone_rp_usage:

.. include:: examples/csvio.processors_standalone.rst
        :start-after: start-standalone_row_processor
        :end-before: end-standalone_row_processor

.. autoclass:: csvio.processors.row_processor.RowProcessor
    :show-inheritance:
    :members:
    :inherited-members:
