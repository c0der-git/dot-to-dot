import sys
import types
import importlib


def setup_module(module):
    numpy = types.ModuleType('numpy')
    numpy.random = types.SimpleNamespace(randint=lambda *args, **kwargs: 0)
    numpy.sum = lambda x: sum(x)
    sys.modules.setdefault('numpy', numpy)

    scipy = types.ModuleType('scipy')
    sys.modules.setdefault('scipy', scipy)
    scipy.optimize = types.ModuleType('optimize')
    sys.modules.setdefault('scipy.optimize', scipy.optimize)


def test_point_to_line_index_returns_int():
    LineConnector = importlib.import_module('LineConnector').LineConnector
    lines = [[(0, 0), (1, 0)], [(2, 0), (3, 0)]]
    connector = LineConnector(lines)
    index = connector.pointToLineIndex((0, 0))
    assert isinstance(index, int)
