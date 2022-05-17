Field Processor
================

A Field Processor is used to transform the values in a row represented by
a dictionary that maps ``column->value`` pairs. This processor can be used to
transform the values of particular fields in a row, where the values of other
fields in the row are not required for making the transformation.

:doc:`Row Processors <csvio.rowprocessor>` can be used to make
transformations where values of other fields within the same row are required.

In *csvio* a CSV file is represented by a list of dictionaries that is
populated in the ``rows`` attribute of the :py:class:`~csvio.CSVReader` or
:py:class:`~csvio.CSVWriter` Classes.

Once instantiated, a Field Processor Object can be used by itself to process an
arbitrary dictionary that represents a row or can be passed to the constructors
of :doc:`CSVReader </local_rw/csvio.csvreader>` or :doc:`CSVWriter </local_rw/csvio.csvwriter>`.

In the case where a Field Processor Object is passed to the constructor of
:doc:`CSVReader </local_rw/csvio.csvreader>`, it is applied to the rows of the
:doc:`CSVReader </local_rw/csvio.csvreader>` as soon as they are read from the CSV file.
See :ref:`example code <csvreader_processors_usage>` for further details.

Similarly, in the case where a Field Processor Object is passed to the
constructor of :doc:`CSVWriter </local_rw/csvio.csvwriter>`, it is applied to the rows of
the :doc:`CSVWriter </local_rw/csvio.csvwriter>` as soon as they are added for writing to
the output CSV using its :py:func:`~csvio.CSVWriter.add_rows` method.
See :ref:`example code <csvwriter_processors_usage>` for further details.

.. _standalone_fp_usage:

.. include:: /examples/csvio.processors_standalone.rst
        :start-after: start-standalone_field_processor
        :end-before: end-standalone_field_processor

.. autoclass:: csvio.processors.field_processor.FieldProcessor
    :show-inheritance:
    :members:
    :inherited-members:
