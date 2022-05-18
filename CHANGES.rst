**2022-05-18**

*Version 1.1.0*

- Read CSV files from a FTP location.
  `read more <https://csvio.readthedocs.io/en/latest/remote_rw/ftp/csvio.ftp_reader.html>`_.
- Test FTP reader using Docker fixtures, using a live FTP server.
- Refactor documentation.

**2021-11-07**

*Version 1.0.0*

- Process and transform row values using row processors
  `read more <https://csvio.readthedocs.io/en/latest/processors/csvio.rowprocessor.html>`_.
- Define and pass multiple types of processors to constructors of CSVReader and
  CSVWriter.
- **Breaking update**: ``fieldprocessor`` argument to constructors of CSVWriter and
  CSVReader renamed to ``processors``, that takes accepts a list of processors.

**2021-11-01**

*Version 0.3.0*

- Process and transform row values using field processors
  `read more <https://csvio.readthedocs.io/en/latest/processors/csvio.fieldprocessor.html>`_.

**2021-10-03**

*Version 0.2.0*

- Construct a nested dictionary from rows based on a list of ordered column names.
  names `read more <https://csvio.readthedocs.io/en/latest/base_classes/csvio.csvbase.html#csvio.csvbase.CSVBase.rows_to_nested_dicts>`_.

**2021-09-24**

*Version 0.1.0*

- First release.
