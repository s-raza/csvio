Field Processor
================

A Field Processor may be used to transform the values in a row represented by
a dictionary that maps ``column->value`` pairs.

In *csvio* a CSV file is represented by a list of dictionaries that is
populated in the ``rows`` attribute of the :py:class:`~csvio.CSVReader` or
:py:class:`~csvio.CSVWriter` Classes.

Once instantiated, a Field Processor Object can be used by itself to process an
arbitrary dictionary that represents a row or can be passed to the constructors
of :py:class:`~csvio.CSVReader` or :py:class:`~csvio.CSVWriter`.

In the case where a Field Processor Object is passed to the constructor of
:py:class:`~csvio.CSVReader`, it is applied to the rows of the
:py:class:`~csvio.CSVReader` as soon as they are read from the CSV file.
See :ref:`example code <csvreader_fp_usage>` for further details.

Similarly, in the case where a Field Processor Object is passed to the
constructor of :py:class:`~csvio.CSVWriter`, it is applied to the rows of the
:py:class:`~csvio.CSVWriter` as soon as they are added for writing to the
output CSV using the :py:func:`~csvio.CSVWriter.add_rows` method.

**Standalone Example Usage**

.. include:: examples/csvio.fieldprocessor.rst
        :start-after: start-standalone_field_processor
        :end-before: end-standalone_field_processor

.. autoclass:: csvio.processors.field_processor.FieldProcessor
    :show-inheritance:
    :members:
    :inherited-members:
