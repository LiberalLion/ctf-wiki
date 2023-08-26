import sys
with open(sys.argv[1], encoding='utf-8') as f:
    f1 = open(f'{sys.argv[1][:-3]}1.md', 'w', encoding='utf-8')
    for line in f:
        if line.startswith('#'):
            line = f'#{line}'
        f1.writelines(line)
f1.close()