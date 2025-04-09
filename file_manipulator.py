import sys

def reverse():
    with open('test.txt') as f:
        content = f.read()
    reversed_str = "".join(reversed(content))
    with open('test_dump.txt', 'w') as f:
        f.write(reversed_str)

def copy():
    with open('test.txt') as f:
        content = f.read()
    with open('test_dump.txt', 'w') as f:
        f.write(content)

def duplicate_contents(n):
    with open('test.txt') as f:
        content = f.read()
    contents = content * int(n)
    with open('test.txt', 'w') as f:
        f.write(contents)

def replace_string(replace_str, new_str):
    with open('test.txt') as f:
        content = f.read()
    replaced_content = content.replace(replace_str, new_str)
    with open('test.txt', 'w') as f:
        f.write(replaced_content)

# コマンドは["reverse", "copy", "duplicate-contents", "replace-string"]のいずれか
commands = ["reverse", "copy", "duplicate-contents"]
while True:
    args = sys.argv
    command = args[1] 
    if len(args) == 4 and command in commands:
        break
    elif len(args) == 5 and command == "replace-string":
        break
    else:
        print(len(args))
        sys.stdout.buffer.write(b"Invalid input. Try again.\n")
        sys.stdout.flush()
        sys.exit(1)

match command:
    case "reverse":
        reverse()
    case "copy":
        copy()
    case "duplicate-contents":
        duplicate_contents(args[3])
    case "replace-string":
        replace_string(args[3], args[4])

sys.stdout.buffer.write(b"done\n")
sys.stdout.flush()

