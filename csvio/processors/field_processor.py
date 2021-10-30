from .processor_base import ProcessorBase


class FieldProcessor(ProcessorBase):
    def __init__(self, handle: str) -> None:

        super().__init__(handle)
