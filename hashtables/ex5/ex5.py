# Your code here
import pprint

def pp(str):
    pp = pprint.PrettyPrinter(indent=4)
    return pp.pprint(str)

def finder(files, queries):
    result = []
    cache = {}
    
    for path in files:
        path_end = path.split('/')[-1]
        if path_end in cache: cache[path_end].append(path)
        else: cache[path_end] = [path]

    for q in queries:
        if q in cache: result.extend(cache[q])

    return result

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
