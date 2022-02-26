from json import load

if __name__ == '__main__':
    with open('./names.json', 'r') as f:
        names = load(f)
        print(names)