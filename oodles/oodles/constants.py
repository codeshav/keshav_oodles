from enum import Enum
from oodles.core.lib.model_signal_funcs import *


class ModelSignal(Enum):
    DEFAULT = 1
    CROSS_ENTROPY_CONFIDENCE = 2
    BINARY_ENTROPY_CONFIDENCE = 3
    PASS_ALL = 4


MODEL_SIGNAL_TO_FN_MAPPING = {
    ModelSignal.DEFAULT: pass_none,
    ModelSignal.CROSS_ENTROPY_CONFIDENCE: cross_entropy_confidence,
    ModelSignal.BINARY_ENTROPY_CONFIDENCE: binary_entropy_confidence,
    ModelSignal.PASS_ALL: pass_all,
}


class AnnotationMethod(Enum):
    MASTER_FILE = 1


class Anomaly(Enum):
    EDGE_CASE = "edge_case"
    DATA_DRIFT = "data_drift"
    CUSTOM_MONITOR = "custom_monitor"


class DataDrift(Enum):
    DDM = "DDM"
