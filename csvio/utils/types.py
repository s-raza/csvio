from typing import Any, Callable, Dict, List

R = Dict[str, Any]
RS = List[R]
FN = List[str]
KW = Dict[str, Any]
FP = Callable[[str], Any]
DFP = Dict[str, List[FP]]
RP = Callable[[R], Any]
LRP = List[RP]
