from flask import Flask, jsonify
import requests

app = Flask(__name__)

customers = {
    101: {"id": 101, "name": "Customer-1"},
    102: {"id": 102, "name": "Customer-2"}
}

@app.route("/customers/<int:user_id>/orders")
def get_account_details(user_id):

    customer = customers.get(user_id)

    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    try:
        response = requests.get(
            f"http://localhost:5002/orders/user/{user_id}",
            timeout=3
        )
        orders = response.json()
    except:
        orders = []

    return jsonify({
        "customer": customer,
        "orders": orders
    })

@app.route("/")
def home():
    return jsonify({"service": "Customer Service Running"})

if __name__ == "__main__":
   if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)