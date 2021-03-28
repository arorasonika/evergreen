# /main.py

from vendors.app import app
from vendors.database.init_db import init_db


def main():
    init_db()
    app.run()


if __name__ == '__main__':
    main()
