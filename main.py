from server import app
from db_orm import *

def main():
    with db:
        db.create_tables([User, Chat, Message])
    app.run(debug=True)


if __name__ == "__main__":
    main()