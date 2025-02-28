import streamlit as st

def main():
    st.title("Simple Calculator")
    st.write("This is a basic calculator built with Streamlit")
    
    # Create two columns for input numbers
    col1, col2 = st.columns(2)
    
    with col1:
        num1 = st.number_input("Enter first number", value=0.0)
    
    with col2:
        num2 = st.number_input("Enter second number", value=0.0)
    
    # Operation selection
    operation = st.selectbox(
        "Select operation",
        ("Addition", "Subtraction", "Multiplication", "Division")
    )
    
    # Calculate button
    if st.button("Calculate"):
        if operation == "Addition":
            result = num1 + num2
            st.success(f"Result: {num1} + {num2} = {result}")
        
        elif operation == "Subtraction":
            result = num1 - num2
            st.success(f"Result: {num1} - {num2} = {result}")
        
        elif operation == "Multiplication":
            result = num1 * num2
            st.success(f"Result: {num1} × {num2} = {result}")
        
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
                st.success(f"Result: {num1} ÷ {num2} = {result}")
            else:
                st.error("Error: Division by zero is not allowed!")

    # Add some styling and information
    st.markdown("---")
    st.markdown("""
    ### Instructions:
    1. Enter two numbers in the input fields
    2. Select the desired operation
    3. Click the Calculate button to see the result
    """)

if __name__ == "__main__":
    main() 