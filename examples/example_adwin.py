"""Detect a change in the mean of a stream with the ADWIN adaptive windowing statistic."""

import numpy as np

from pysad.statistics import ADWINMeter

if __name__ == "__main__":
    rng = np.random.default_rng(0)
    # The mean shifts from 0.25 to 0.55 halfway through the stream.
    values = np.concatenate([rng.uniform(0.0, 0.5, 1000), rng.uniform(0.3, 0.8, 1000)])

    # ADWIN assumes values are in [0, 1]. Rescale a known range [a, b] to (x - a) / (b - a).
    meter = ADWINMeter()

    for index, value in enumerate(values):
        meter.update(value)
        # drift_detected is True whenever the window shrinks due to a detected change.
        if meter.drift_detected:
            print(
                f"First change detected at index {index} (zero-based), "
                f"width {meter.width}, mean {meter.get():.2f}"
            )
            break
