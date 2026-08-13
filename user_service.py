import json
import os

USERS_FILE = "users.json"


def load_users():
    if not os.path.exists(USERS_FILE):
        return []

    with open(USERS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4, ensure_ascii=False)


def generate_id(users):
    return max(
        [user["id"] for user in users],
        default=0
    ) + 1


def get_all_users():
    return load_users()


def get_user_by_id(user_id):
    users = load_users()

    for user in users:
        if user["id"] == user_id:
            return user

    return None


def create_user(name, email):
    users = load_users()

    new_id = generate_id(users)

    new_user = {
        "id": new_id,
        "name": name,
        "email": email
    }

    users.append(new_user)
    save_users(users)

    return new_user


def update_user(user_id, name, email):
    users = load_users()

    for index, user in enumerate(users):
        if user["id"] == user_id:
            users[index]["name"] = name
            users[index]["email"] = email

            save_users(users)

            return users[index]

    return None


def delete_user(user_id):
    users = load_users()

    for index, user in enumerate(users):
        if user["id"] == user_id:
            deleted_user = users.pop(index)

            save_users(users)

            return deleted_user

    return None