import os

basic_config = f''
lines =     []
routes =    []
dirs =      []
dir

def add_working_directory(config):
    route = os.getcwd()
    config+='route '+route+ ' '
    return config

def delete_new_line(line):
    return not line == '\n'

def clear_lines(lines):
    lines = list(filter(delete_new_line,lines))
    return lines
def clear_route(line):
    if line[-1] == '\n':
        return line[:-1]
    return line
def is_route(line):
    return 'route' in line[:6]

def classify(lines):
    lines = clear_lines(lines)
    routes = list(filter(is_route, lines))
    routes = list(map(clear_route, routes))
    data = (routes)
    return data
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if os.path.exists('file.config'):
        f = open('file.config', 'r')
        while True:
            line = f.readline()
            if not line:
                break
            lines.append(line)
        print(lines)

        routes = classify(lines)

        print(lines)
        print(routes)
        f.close()
    else:
        f = open("file.config", "x")
        f.write(add_working_directory(''))
        f.close()
