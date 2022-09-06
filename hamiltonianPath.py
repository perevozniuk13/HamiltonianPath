def HamilthonPath(strArr):
    visited = []
    verticles = strArr[0]
    edges = strArr[1]
    path = strArr[2]
    edges = edges.rstrip(edges[-1])
    edges = edges.lstrip(edges[0])
    edges = edges.split(",")
    path = path.rstrip(path[-1])
    path = path.lstrip(path[0])
    path = path.split(",")
    for i in range(len(path)-1):
        if f"{path[i]}-{path[i+1]}" in edges or f"{path[i+1]}-{path[i]}" in edges:
            if f"{path[i]}-{path[i+1]}" not in visited or f"{path[i+1]}-{path[i]}" not in visited:
                visited.append(f"{path[i]}-{path[i+1]}")
                visited.append(f"{path[i]}-{path[i + 1]}")
            else:
                return path[i]
        else:
            return path[i]
    return True

print(HamilthonPath(["(A,B,C,D)", "(A-B,B-C,A-D)", "(A,B,C)"]))
print(HamilthonPath(["(A,B,C,D)", "(A-B,B-C,A-D)", "(A, D, C)"]))

