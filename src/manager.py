import click
from action import Action


@click.group()
def main():
    pass


@click.command()
@click.option('--api', help='Name of action.')
def gitlab_api(api):
    action = Action()

    getattr(action, api)()

main.add_command(gitlab_api)

if __name__ == "__main__":
    main()
