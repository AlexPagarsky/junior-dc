from typing import List

import yaml  # pip install PyYAML


def generator(file: str, timestamps: bool = False, multiline: bool = False) -> List[str]:
    statements = []

    separator, indent = ('\n', '\t') if multiline else (' ', '')

    with open(file, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

        for name, outer in data.items():
            statement = ['CREATE TABLE ', name, ' (', separator]
            fields = outer['fields']
            statement.extend((indent, name.lower() + '_id', ' SERIAL PRIMARY KEY,', separator))

            for var_name, data_type in fields.items():
                statement.extend((indent, name.lower(), '_' + var_name, ' ', data_type.upper(), ',', separator))

            if timestamps:
                statement.extend(
                    (
                        indent, name.lower(), '_created TIMESTAMP DEFAULT current_timestamp', ',', separator,
                        indent, name.lower(), '_updated TIMESTAMP DEFAULT current_timestamp', separator, ','
                    )
                )
                statements.extend(
                    (
                        ''.join(
                            (
                                'CREATE FUNCTION update_date() RETURNS TRIGGER', separator,
                                'LANGUAGE plpgsql',separator,
                                'AS $update$', separator,
                                'BEGIN', separator,
                                indent, 'NEW.' + name.lower() + '_updated := current_timestamp;', separator,
                                indent, 'RETURN NEW;', separator,
                                'END;', separator,
                                '$update$;'
                            )
                        ),
                        ''.join(
                            (
                                'CREATE FUNCTION create_date() RETURNS TRIGGER', separator,
                                'LANGUAGE plpgsql',separator,
                                'AS $update$', separator,
                                'BEGIN', separator,
                                indent, 'NEW.' + name.lower() + '_created := current_timestamp;', separator,
                                indent, 'RETURN NEW;', separator,
                                'END;', separator,
                                '$update$;'
                            )
                        )
                    )
                )
                statements.extend(
                    (
                        ''.join(
                            (
                                'CREATE TRIGGER update_time AFTER UPDATE ON ', name, separator,
                                'FOR EACH STATEMENT', separator,
                                'EXECUTE PROCEDURE update_date();', separator
                            )
                        ),
                        ''.join(
                            (
                                'CREATE TRIGGER create_time AFTER INSERT ON ', name, separator,
                                'FOR EACH STATEMENT', separator,
                                'EXECUTE PROCEDURE create_date();', separator
                            )
                        )
                    )
                )
            statement[-1] = ');'
            statements.insert(-2, ''.join(statement))

            # TODO: Finish second trigger (?)
            # TODO: SET PRICE NOT NULL IN STATEMENTS, DURILA

    return statements


if __name__ == "__main__":
    statements = generator(file='scheme.yaml', timestamps=True, multiline=True)
    for query in statements:
        print(query, '\n')
