from VertexData import *

def main():
    args: cli.Args = cli.Args()
    v: VertexParser.VertexParser = VertexParser.VertexParser(
        args.args.Obj_File, args.args.Target_File, args.args.no_normal_data
    )
    v.parse()
    v.output()

if __name__ == "__main__":
    main()