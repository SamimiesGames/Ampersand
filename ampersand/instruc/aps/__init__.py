from .flow import FLOW_EXPORT_TABLE
from .math import MATH_EXPORT_TABLE
from .memory import MEMORY_EXPORT_TABLE
from .registers import REGISTER_EXPORT_TABLE
from .stack import STACK_EXPORT_TABLE


APS_EXPORT_TABLE = {
    **FLOW_EXPORT_TABLE,
    **MATH_EXPORT_TABLE,
    **MEMORY_EXPORT_TABLE,
    **REGISTER_EXPORT_TABLE,
    **STACK_EXPORT_TABLE,
    "vectors": {
        "sp": 0xFEEE,
        "pc": 0x0
    }
}

