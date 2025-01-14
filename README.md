# .obj to vertex data

## Intended Usage
This is to make .obj files with triangle data, for example,
```
v 1 0 0
v 0 1 0
v 0 0 1

vn 0.577 0.577 0.577

f 1//1 2//2 3//3
```
to
```
1, 0, 0, 0.5777, 0.5777, 0.5777,
0, 1, 0, 0.5777, 0.5777, 0.5777,
0, 0, 1, 0.5777, 0.5777, 0.5777,
```
This is for feeding obj files to a vertex buffer.