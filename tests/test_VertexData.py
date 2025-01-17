from VertexData import *

o_data = """
"""

def test_cube():
    vd: VertexParser.VertexParser = VertexParser.VertexParser("Cube.triangulated.obj", '').parse()
    assert 1 + 1 == 2