# i can never get this to work since __init__ just never runs
from .VertexParser import VertexParser as VertexParser
from .VertexParser import NOPOSITIONDATA as NOPOSITIONDATA
from .VertexParser import NOTEXTUREDATA as NOTEXTUREDATA
from .VertexParser import NONORMALDATA as NONORMALDATA

__all__ = ["VertexParser", "NOPOSITIONDATA", "NOTEXTUREDATA", "NONORMALDATA"]
