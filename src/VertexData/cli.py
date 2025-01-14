from argparse import ArgumentParser, Namespace

class Args():
    def __init__(self) -> None:
        self.parser: ArgumentParser = ArgumentParser(
                                            prog = 'VertexData',
                                            description = 'For feeding data of .obj files to a vertex buffer'
        )
        self.parser.add_argument(
            'Obj_File', help = 'The file name of the .obj file'
        )
        
        self.parser.add_argument(
            'Target_File', help = 'Enter the target file name'
        )
        self.args: Namespace = self.parser.parse_args()