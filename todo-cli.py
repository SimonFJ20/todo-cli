from sys import argv
from os.path import exists, expanduser

TODO_FILE_PATH = expanduser('~/.todolist')

def todo_file_exists():
    return exists(TODO_FILE_PATH)

def create_file():
    with open(TODO_FILE_PATH, 'w') as f:
        f.write('')
        f.close()

def check_file():
    if not todo_file_exists():
        create_file()
        print(f"'{TODO_FILE_PATH}' not found, new created!")

def load_file(dst):
    dst.clear()
    with open(TODO_FILE_PATH) as f:
        for v in f:
            if v.strip() != '':
                dst.append(v.strip())
        f.close()

def save_file(src):
    with open(TODO_FILE_PATH, 'w') as f:
        f.write('\n'.join(src))
        f.close()

def len3str(n: int):
    assert n < 1000, 'numbers must be <1000'
    s = str(n)
    while len(s) < 3:
        s = ' ' + s
    return s

def print_list(src):
    for i in range(len(src)):
        if i == 0:
            print(f"{len3str(i)} -> {src[i]}")
        else:
            print(f"{len3str(i)} - {src[i]}")

def insert_todo(src, i: int, v: str):
    src.insert(i, v)
    save_file(src)

def swap_todo(src, a: int, b: int):
    t = src[a]
    src[a] = src[b]
    src[b] = t
    save_file(src)

def update_todo(src, i: int, v: str):
    src[i] = v
    save_file(src)

def delete_todo(src, i: int):
    src.pop(i)
    save_file(src)

def check_args(argv, n):
    if len(argv) < n:
        print('Too few arguments')
        exit(1)

def print_usage():
    print('USAGE: python3 todo-cli.py <option> [...values]')
    print('\t-p, --print\tPrint TODO list. Same as no option.')
    print('\t--help, --usage\tPrint this message.')
    print('\t-i, --insert\t(i, v) Insert TODO into list at `i`.')
    print('\t-s, --swap\t(a, v) Swap TODO `a` with `b`.')
    print('\t-u, --update\t(i, v) Replace TODO at `i` with new string.')
    print('\t-d, --delete\t(i) Delete TODO at `i`.')

if __name__ == '__main__':
    check_file()
    todo_list = []
    load_file(todo_list)
    if len(argv) <= 1:
        pass
    elif len(argv) >= 2:
        option = argv[1]
        if option in ['--print', '-p']:
            pass
        elif option in ['--insert', '-i']:
            check_args(argv, 4)
            insert_todo(todo_list, int(argv[2]), ' '.join(argv[3:]))
        elif option in ['--swap', '-s']:
            check_args(argv, 4)
            swap_todo(todo_list, int(argv[2]), int(argv[3]))
        elif option in ['--update', '-u']:
            check_args(argv, 4)
            update_todo(todo_list, int(argv[2]), ' '.join(argv[3:]))
        elif option in ['--delete', '-d']:
            check_args(argv, 3)
            delete_todo(todo_list, int(argv[2]))
        else:
            print_usage()
            exit(1)
    if not '-np' in argv and not '--no-print' in argv:
        print_list(todo_list)

