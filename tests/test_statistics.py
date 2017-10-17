#!/usr/bin/env python
from itertools import islice

from matplotlib.testing.decorators import image_comparison
from matplotlib.pyplot import plot, title
from numpy import arange

from sample import fib, collatz
from sample import average, tail

def test_average():
    f = islice(fib(), 1, 10)
    assert average(f) == 15.777

@image_comparison(baseline_images=['average'], extensions=['png'])
def test_plot_average():
    xs = arange(1, 100)
    ys = [average(range(x)) for x in xs]
    title('average(range(x))')
    plot(xs, ys)

if __name__ == '__main__':
    from logging import getLogger, basicConfig, INFO
    logger = getLogger(__name__)
    basicConfig(level=INFO)

    for test in [test_average, test_plot_average]:
        logger.info(f'Running {test}')
        test()
