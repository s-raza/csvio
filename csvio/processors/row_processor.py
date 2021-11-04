from typing import List, Type, Union

from ..utils.types import RP, R
from .processor_base import ProcessorBase


class RowProcessor(ProcessorBase):
    """
    :param handle: Reference handle for the field processor
    :type handle: required
    """

    def __init__(self, handle: str) -> None:

        super().__init__(handle)

    def add_processor(
        self, func_: Union[List[RP], RP], handle: str = None
    ) -> None:

        pass

    def process_row(
        self, row: R, processor_handle: Union[Type[ProcessorBase], str] = None
    ) -> R:

        pass
