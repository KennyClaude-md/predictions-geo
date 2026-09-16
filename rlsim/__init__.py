"""RL-SIM: a fitted booking model for Rolling Loud lineups.

The same stance as GEO-SIM, applied to a much smaller problem. A festival
lineup is usually forecast by listing plausible names. That is a ranking, not a
forecast, and it cannot be scored. RL-SIM instead fits an explicit choice model
to the six US flagship editions Rolling Loud has actually staged since 2023,
backtests it leave-one-edition-out, and then integrates the fitted model forward
over both parameter uncertainty and artist availability to produce per-artist
probabilities with Monte Carlo error bars.

The honest headline about this model is that it is fitted to eighteen headline
bookings. That is a thin reference class, and the error bars the Monte Carlo
reports are sampling noise only -- the dominant uncertainty is in the features,
particularly the retrospective popularity ranks for pre-2026 editions. Read
`backtest()` before believing any single number.
"""

__version__ = "1.0.0"

from .data import Edition, Roster, load  # noqa: F401
from .model import (  # noqa: F401
    HeadlinerModel, UndercardModel, backtest, select_undercard,
)
from .simulate import simulate  # noqa: F401
from .days import assign_days  # noqa: F401
