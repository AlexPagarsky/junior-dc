from typing import List
import yaml
import os.path


def generator(file: str, timestamps: bool) -> List[str]:
    statements = []

    with open(file, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

        for name, outer in data.items():
            statement = ['CREATE TABLE ', name, ' ( ']

            for _, fields in outer.items():
                statement.extend((name.lower(), '_id', ' SERIAL PRIMARY KEY, '))
                for var, data_type in fields.items():
                    statement.extend((name.lower(), '_', var, ' ', data_type, ', '))

            if timestamps:
                statements.extend()

            statement[-1] = ' );'
            statements.append(''.join(statement))

    return statements


if __name__ == "__main__":
    statements = generator(file='scheme.yaml', timestamps=False)
    for i in statements:
        print(i)