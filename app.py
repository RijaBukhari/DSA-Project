import streamlit as st

# Classes for Data Structures
class User:
    def __init__(self, name, product, quantity, bill):
        self.name = name
        self.product = product
        self.quantity = quantity
        self.bill = bill

class DeliveryUser:
    def __init__(self, user, address, delivery_charges, distance_delivery):
        self.user = user
        self.address = address
        self.delivery_charges = delivery_charges
        self.distance_delivery = distance_delivery
        self.next = None

class TakeAway:
    def __init__(self, name, product, quantity, bill, order_id):
        self.name = name
        self.product = product
        self.quantity = quantity
        self.bill = bill
        self.order_id = order_id
        self.left = None
        self.right = None

# Placeholder functions for AVL operations
def insert_takeaway(root, name, product, quantity, bill, order_id):
    # Simplified AVL insert logic
    # Add rotations if needed
    if root is None:
        return TakeAway(name, product, quantity, bill, order_id)
    if order_id < root.order_id:
        root.left = insert_takeaway(root.left, name, product, quantity, bill, order_id)
    else:
        root.right = insert_takeaway(root.right, name, product, quantity, bill, order_id)
    return root

def display_takeaway_orders(root):
    if root:
        display_takeaway_orders(root.left)
        st.write(f"Name: {root.name}, Product: {root.product}, Quantity: {root.quantity}, Bill: {root.bill}, Order ID: {root.order_id}")
        display_takeaway_orders(root.right)

# Streamlit Interface
st.title("E-Commerce Store")

# Example data
products = {
    1: {"name": "Sony FX30", "price": 45500},
    2: {"name": "Canon EOS 90D", "price": 289000},
    3: {"name": "Nikon D6", "price": 155700}
}

# Store Orders
takeaway_root = None

# Main Menu
option = st.sidebar.selectbox("Choose an option", ["Display Products", "Place Takeaway Order", "View Takeaway Orders"])

if option == "Display Products":
    st.header("Available Products")
    for pid, details in products.items():
        st.write(f"{pid}. {details['name']} - Rs. {details['price']}")

elif option == "Place Takeaway Order":
    st.header("Place an Order")
    name = st.text_input("Enter your name")
    product_id = st.selectbox("Select a product", list(products.keys()))
    quantity = st.number_input("Enter quantity", min_value=1, step=1)
    order_id = st.number_input("Enter order ID", min_value=1, step=1)
    
    if st.button("Place Order"):
        bill = products[product_id]["price"] * quantity
        takeaway_root = insert_takeaway(takeaway_root, name, products[product_id]["name"], quantity, bill, order_id)
        st.success(f"Order placed! Total Bill: Rs. {bill}")

elif option == "View Takeaway Orders":
    st.header("Takeaway Orders")
    if takeaway_root:
        display_takeaway_orders(takeaway_root)
    else:
        st.write("No orders available.")
