import click
from utils import json_manager


@click.group()
def cli():
    pass


@cli.command()
def users():
    data = json_manager.read_json()
    for user in data:
        print(f"{user['id']} - {user['first_name']} - {user['last_name']}")


@cli.command()
@click.option("--first_name", required=True, help="name of the user")
@click.option("--last_name", required=True, help="name of the user")
@click.pass_context
def new(ctx, first_name, last_name):
    if not first_name or not last_name:
        ctx.fail("The first_name and last_name are required")
    else:
        data = json_manager.read_json()
        new_id = len(data) + 1
        new_user = {
            'id': new_id,
            'first_name': first_name,
            'last_name': last_name
        }
        data.append(new_user)
        json_manager.write_json(data)
        print(f"User {first_name} {last_name} created successfully")

@cli.command()
@click.argument('id', type=int)
def user(id):
    data = json_manager.read_json()
    user = next((x for x in data if x['id']== id), None)
    if user is None:
        print(f"#404 - User with id #{id} not Found")
    else:
        print(f"{user['id']} - {user['first_name']} - {user['last_name']}")


@cli.command()
@click.argument('id', type=int)
def delete(id):
    data = json_manager.read_json()
    user = next((x for x in data if x['id']== id), None)
    if user is None:
        print('#404 - User not Found')
    else:
        data.remove(user)
        json_manager.write_json(data)
        print(f"User with id #{id} deleted successfully")


@cli.command()
@click.argument('id', type=int)
@click.option("--first_name", help="name of the user")
@click.option("--last_name", help="name of the user")
def update(id, first_name, last_name):
    data = json_manager.read_json()
    for user in data:
        if user['id'] == id:
            if first_name is not None:
                user['first_name'] = first_name
            if last_name is not None:
                user['last_name'] = last_name
            break
    json_manager.write_json(data)
    print(f"User with id #{id} updated successfully")


if __name__ == "__main__":
    cli()
