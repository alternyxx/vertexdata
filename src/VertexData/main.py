from VertexData import *

def main():
    args: cli.Args = cli.Args()
    v: VertexParser.VertexParser = VertexParser.VertexParser(
        args.args.obj_file, args.args.target_file, args.args.no_normal_data
    )
    v.parse()
    v.output()

if __name__ == "__main__":
    main()