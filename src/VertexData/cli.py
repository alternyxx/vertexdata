from argparse import ArgumentParser, Namespace
from sys import exit

class Args():
    def __init__(self) -> None:
        self.parser: ArgumentParser = ArgumentParser(
                                        prog='VertexData',
                                        description='For feeding data of .obj files to a vertex buffer'
        )
        self.parser.add_argument(
            'Obj_File', help='The file name of the .obj file'
        )
        self.parser.add_argument(
            'Target_File', 
            help='[Optional] Enter the target file name', 
            default='',
            nargs='?'
        )
        self.parser.add_argument(
            '-nvn', '--no-vn',
            action='store_true',
            dest='no_normal_data'
        )
        self.args: Namespace = self.parser.parse_args()

        if not self.args.Obj_File.endswith(".obj"):
            print(f"Expected .obj file, got: {self.args.Obj_File}")
            exit()
        elif self.args.Target_File and not self.args.Target_File.endswith(".obj"):
            print(f"Expected .obj file, got: {self.args.Target_File}")
            exit()