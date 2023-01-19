from ampersand.architectures.aps.flow import FLOW_EXPORT_TABLE
from ampersand.architectures.aps.math import MATH_EXPORT_TABLE
from ampersand.architectures.aps.memory import MEMORY_EXPORT_TABLE
from ampersand.architectures.aps.registers import REGISTER_EXPORT_TABLE
from ampersand.architectures.aps.stack import STACK_EXPORT_TABLE


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

