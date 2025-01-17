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
    def __init__(self, source: str, target: str, data: str) -> None:
        self.target: str = target if target else f"{source.removesuffix('.obj')}.vd.obj"
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


class Texture():
    def __init__(self, texture: str) -> None:
        self.texture: list[str] = texture

    @property
    def texture(self) -> list[str]:
        return self._texture
    
    @texture.setter
    def texture(self, vt: str) -> None:
        self._texture = vt.split()
        self._texture.pop(0)


class Normal():
    def __init__(self, normal: str) -> None:
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
    def __init__(self, face: str, 
        vertices: list[Vertex], normals: list[Normal], textures: list[Texture], no_normal_data: bool
    ) -> None:
        self.face: list[str] = face
        self.vertices: list[Vertex] = vertices
        self.normals: list[Normal] = normals
        self.textures: list[Texture] = textures
        self.no_normal_data: bool = no_normal_data

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
                    vertex, texture, normal = info
                case 2:
                    vertex, normal = info
                case 1:
                    vertex = info[0]
            try:
                if vertex:
                    vertex = ", ".join(self.vertices[int(vertex) - 1].vertex) + ', '
                if not self.no_normal_data:
                    if texture:
                        texture = ", ".join(self.textures[int(texture) - 1].texture) + ', '                
                    if normal:
                        normal = ", ".join(self.normals[int(normal) - 1].normal) + ','
                else:
                    normal = texture = ''
            except ValueError:
                print("Obj file contains strings as indexing vertex info :sob:")
                exit()
            else:
                triangle += vertex + texture + normal + '\n'
        return triangle


class VertexParser():
    def __init__(self, source: str, target: str, no_normal_data: bool=False) -> None:
        self.obj: Obj = Obj(source)
        self.target: Target = Target(source, target, '')
        self.vertices: list[Vertex] = []
        self.normals: list[Normal] = []
        self.textures: list[Texture] = []
        self.no_normal_data: bool = no_normal_data

    def parse(self) -> None:
        for line in self.obj.obj_data:
            if line[0] == 'v':
                match line[1]:
                    case ' ':
                        self.vertices.append(Vertex(line))
                    case 'n':
                        self.normals.append(Normal(line))
                    case 't':
                        self.textures.append(Texture(line))
                    case _:
                        print("what kind of vertex info do you have??")
                        exit()
            elif line[0] == 'f':
                face = Face(line, self.vertices, self.normals, self.textures, self.no_normal_data).construct()
                self.target.data += face

    def output(self) -> None:
        self.target.write_file()