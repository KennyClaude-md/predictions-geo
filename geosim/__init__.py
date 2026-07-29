"""GEO-SIM: a coupled Monte Carlo simulator of world futures.

Parameters are elicited from web-grounded domain analysts and adversarially
audited before compilation; the engine integrates over both stochastic and
parameter uncertainty; outputs are calibrated probabilities with Monte Carlo
error bars, systemic-amplification factors, and emergent scenario clusters.
"""

__version__ = "1.0.0"

from .params import CompiledParams, load  # noqa: F401
from .engine import Simulator  # noqa: F401
