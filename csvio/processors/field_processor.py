from .processor_base import ProcessorBase


class FieldProcessor(ProcessorBase):
    """
    :param handle: Reference handle for the field processor
    :type handle: required
    """

    def __init__(self, handle: str) -> None:

        super().__init__(handle)
