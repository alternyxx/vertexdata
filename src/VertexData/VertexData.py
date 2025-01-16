from sys import exit
from re import split

class Obj():
    def __init__(self, source: str) -> None:
        self._obj_data = self.read_file(source)

    @property
    def obj_data(self) -> list[str]:
        return self._obj_data
    
    @staticmethod
    def read_file(source) -> list[str] | None:
        try:
            with open(source, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            print("Given obj file doesn't exist")
            exit()


class Target():
    def __init__(self, target: str, data: str) -> None:
        self.target: str = target
        self.data: str = data

    def write_file(self) -> None:
        try:
            with open(self.target, 'w') as file:
                file.write(self.data)
        except:
            print("Unable to write in target file")
            exit()


class Vertex():
    def __init__(self, vertex: str) -> None:
        self.vertex: list[str] = vertex

    @property
    def vertex(self) -> list[str]:
        return self._vertex
    
    @vertex.setter
    def vertex(self, v: str) -> None:
        self._vertex = v.split()
        self._vertex.pop(0)


class Normal():
    def __init__(self, normal) -> None:
        self.normal: list[str] = normal

    @property
    def normal(self) -> list[str]:
        return self._normal
    
    @normal.setter
    def normal(self, vn: str) -> None:
        self._normal = vn.split()
        self._normal.pop(0)


class Face():
    seperator = None
    def __init__(self, face: str, vertices: list[Vertex], normals: list[Normal]) -> None:
        self.face: list[str] = face
        self.vertices = vertices
        self.normals = normals

    @property
    def face(self) -> list[str]:
        return self._face
    
    @face.setter
    def face(self, f: str) -> None:
        self._face: list[str] = f.split()
        self._face.pop(0)

    def construct(self) -> str:
        triangle: str = ""
        for data in self.face:
            info = split(r"\/\/?", data)
            vertex, normal, texture = ["" for i in range(3)]
            match len(info):
                case 3:
                    vertex, normal, texture = info
                case 2:
                    vertex, normal = info
                case 1:
                    vertex = info
            try:
                if vertex:
                    vertex = ", ".join(self.vertices[int(vertex) - 1].vertex)
                if normal:
                    normal = ", ".join(self.normals[int(normal) - 1].normal)                    
            except ValueError as e:
                print(e)
                print("invalid obj")
                exit()
            else:
                triangle += vertex + ",\n"
        return triangle


class VertexData():
    def __init__(self, source, target) -> None:
        self.obj: Obj = Obj(source)
        self.target: Target = Target(target, '')
        self.vertices: list[Vertex] = []
        self.normals: list[Normal] = []

    def parse(self) -> None:
        for line in self.obj.obj_data:
            if line[0] == 'v':
                if line[1] != 'n':
                    self.vertices.append(Vertex(line))
                else:
                    self.normals.append(Normal(line))
            elif line[0] == 'f':
                face = Face(line, self.vertices, self.normals).construct()
                self.target.data += face

    def output(self) -> None:
        self.target.write_file()