#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize


def my_sine(x, amplitude, period):
    """Extend the numpy.sin function with an amplitue and a period.

    Parameters
    ==========
    x : np.ndarray
        The values at which to evaluate the sine.
    amplitude : float
        The multiplicative amplitude of the since.
    period : float
        The period of the sine.

    Returns
    =======
    np.ndarray
        The values of the sine curve at x.
    """
    return amplitude * np.sin(x * period)


if __name__ == "__main__":

    # We set a "seed" which ensures that our random numbers are the same
    # each time we run the script. The seed can be any number you want.
    np.random.seed(17)

    # The problem definitions
    N = 100
    amplitude = 3
    period = 2
    rel_err = 0.1  # 10% measurement uncertainty

    # ------
    # Simulate sinusoidal data with Gaussian noise
    x = np.random.rand(N) * 2 * np.pi  # 100 random numbers between [0, 1) * 2pi
    x = np.sort(x)  # sort them for easier plotting later

    y = amplitude * np.sin(x * period)
    y_err = np.random.normal(loc=0, scale=rel_err * amplitude, size=N)

    # add the Gaussian noise to the data
    y += y_err

    # ------
    # Fit the data

    # p0 provides initial guesses for the parameters. If we do not provide a
    # good initial guess of the correct frequency, we get bad fits. Fitting
    # since curves is not trivial, but also not the focus of the tutorial, so we
    # don't mind here.
    popt, pcov = optimize.curve_fit(my_sine, x, y, p0=[1, 1.8])

    amp_fit, period_fit = popt
    amp_fit_err, period_fit_err = np.sqrt(np.diag(pcov))

    # ------
    # Plot the result
    fig, ax = plt.subplots()

    ax.errorbar(x, y, yerr=y_err, ls="", label="Data")
    ax.plot(x, my_sine(x, amp_fit, period_fit), ls="--", label="Fit")

    # We add the best fit parameters to the title. We could also use ax.text instead
    ax.set_title(
        f"A={amp_fit:.2f}+-{amp_fit_err:.2f}, P={period_fit:.2f}+-{period_fit_err:.2f}"
    )

    ax.set(xlabel="x", ylabel="y")
    ax.legend(frameon=False)

    plt.tight_layout()
    plt.show()
