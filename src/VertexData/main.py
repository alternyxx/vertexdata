import cli
import VertexData

def main():
    args: cli.Args = cli.Args()
    VertexData.VertexData(args.args.Obj_File, args.args.Target_File).iterate()

if __name__ == "__main__":
    main()