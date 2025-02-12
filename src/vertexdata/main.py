from vertexdata.cli import Args
from vertexdata import *

def main():
    args: Args = Args()
    flags = [flag for opt, flag in (
        (args.args.no_position_data, NOPOSITIONDATA),
        (args.args.no_normal_data, NONORMALDATA),
        (args.args.no_texture_data, NOTEXTUREDATA),
    ) if opt]
    v: VertexParser = VertexParser(
        args.args.obj_file, args.args.target_file, True, *flags
    )
    v.parse()
    v.output_file()

if __name__ == "__main__":
    main()