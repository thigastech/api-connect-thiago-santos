from flask import Flask, jsonify, request
from user_service import get_all_users, get_user_by_id, create_user,update_user, delete_user


app = Flask(__name__)


@app.route("/users", methods=["GET"])
def get_users():
    users = get_all_users()
    return jsonify(users), 200


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = get_user_by_id(user_id)

    if user:
        return jsonify(user), 200

    return jsonify({"error": "Usuário não encontrado"}), 404


@app.route("/users", methods=["POST"])
def create_user_route():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON não enviado"}), 400

    if "name" not in data or "email" not in data:
        return jsonify({
            "error": "Os campos name e email são obrigatórios"
        }), 400

    if not data["name"].strip() or not data["email"].strip():
        return jsonify({
            "error": "name e email não podem estar vazios"
        }), 400

    new_user = create_user(
        data["name"],
        data["email"]
    )

    return jsonify(new_user), 201


if __name__ == "__main__":
    app.run(debug=True)

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user_route(user_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON não enviado"}), 400

    if "name" not in data or "email" not in data:
        return jsonify({
            "error": "Os campos name e email são obrigatórios"
        }), 400

    if not data["name"].strip() or not data["email"].strip():
        return jsonify({
            "error": "name e email não podem estar vazios"
        }), 400

    updated_user = update_user(
        user_id,
        data["name"],
        data["email"]
    )

    if updated_user is None:
        return jsonify({
            "error": "Usuário não encontrado"
        }), 404

    return jsonify(updated_user), 200


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user_route(user_id):
    deleted_user = delete_user(user_id)

    if deleted_user is None:
        return jsonify({
            "error": "Usuário não encontrado"
        }), 404

    return jsonify({
        "message": "Usuário removido com sucesso",
        "user": deleted_user
    }), 200