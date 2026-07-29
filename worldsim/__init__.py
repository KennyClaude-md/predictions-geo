"""worldsim — a Monte Carlo engine for probabilistic world-futures forecasting.

Pipeline:
    params.load_base_model   research JSON -> WorldModel
    params.build_worldviews  -> five weighted opinions
    engine.CompiledModel     -> array form
    engine.calibrate_marginals -> baselines tuned so simulated == elicited
    engine.simulate          -> fire-time matrix
    analysis.*               -> marginals, joints, cascades, archetypes
    report.write_outputs     -> markdown + json
"""

__all__ = ["timeline", "hazard", "params", "engine", "continuous", "analysis", "report"]
