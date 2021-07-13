def get_route(string):
    def branch(tree, start):

        end = tree[-1]
        index = tree.index(start)

        best = []

        for point in tree[index:]:
            if point == end:
                if end not in best:
                    best.append(end)

            elif point > start:
                result = branch(tree, point)

                if len(result) + 1 >= len(best):
                    best = [point, *result]

        return best

    tree = list(map(int, string.split()))
    tree = [tree[0]] + branch(tree, tree[0])

    return " ".join(map(str, tree))
