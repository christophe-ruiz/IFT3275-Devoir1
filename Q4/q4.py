# Filter given input in question 4
# lines = []
# if __name__ == '__main__':
#     with open('input4.txt', 'r', encoding="utf-8") as f:
#         lines = [line.strip("\n") for line in f if line != "\n"]
#         with open('output4.txt', 'w', encoding="utf-8") as o:
#             o.write("".join(lines))

if __name__ == '__main__':
    raw = ""
    with open('output4.txt', 'r', encoding='utf-8') as f:
        raw = f.readline()
    print(f'--RAW:{raw}')
