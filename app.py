import streamlit as st

# Calculator Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by Zero!"
    return x / y

# Streamlit UI
st.title("Simple Calculator")

# Operation selection
operation = st.selectbox("Select operation:", ("Add", "Subtract", "Multiply", "Divide"))

# Number input fields
num1 = st.number_input("Enter first number", value=0.0, step=0.1, format="%.2f")
num2 = st.number_input("Enter second number", value=0.0, step=0.1, format="%.2f")

# Perform the selected operation when the button is clicked
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    
    st.success(f"The result of {operation.lower()}ing {num1} and {num2} is: {result}")
