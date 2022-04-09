import zipfile
import json

result = 0

with zipfile.ZipFile('input.zip', 'r') as arch:
    stack = [zipfile.Path(arch)]
    while stack:
        path = stack.pop()
        for p in path.iterdir():
            if p.is_dir():
                stack.append(p)
            if p.is_file():
                if p.name.split('.')[1] == 'json':
                    with p.open('w') as file:
                        content = json.load(file)
                        if content['city'] == 'Moscow':
                            result += 1
print(result)