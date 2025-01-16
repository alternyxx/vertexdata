import cli
import VertexData

def main():
    args: cli.Args = cli.Args()
    vd: VertexData.VertexData = VertexData.VertexData(args.args.Obj_File, args.args.Target_File)
    vd.parse()
    vd.output()

if __name__ == "__main__":
    main()