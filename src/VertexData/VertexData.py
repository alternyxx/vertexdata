from sys import exit

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
        except FileNotFoundError as e:
            print(e)
            print("Given obj file doesn't exist")
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

    def construct(self):
        triangle: str = ""
        for data in self.face:
            vertex, normal = data.split("//")
            try:
                vertex = int(vertex) - 1
                normal = int(normal) - 1
            except ValueError:
                print("invalid obj")
            print(", ".join(self.vertices[int(vertex) - 1].vertex))
        return triangle


class VertexData():
    def __init__(self, source, target) -> None:
        self.obj: Obj = Obj(source)
        self.vertices: list[Vertex] = []
        self.normals: list[Normal] = []

    def iterate(self):
        for line in self.obj.obj_data:
            if line[0] == 'v':
                if line[1] != 'n':
                    self.vertices.append(Vertex(line))
                else:
                    self.normals.append(Normal(line))
            elif line[0] == 'f':
                Face(line, self.vertices, self.normals).construct()


class Target():
    def __init__(self, vertexData: VertexData, target: str) -> None:
        self.vertexData: VertexData = vertexData
        self.target: str = target

    def write_file(self) -> None:
        try:
            with open(self.target, 'w') as file:
                file.write(self.vertexData.data)
        except:
            print("Unable to write in target file")
            exit()

