import streamlit as st
st.set_page_config(page_title="Calculator", page_icon="🧮", layout="wide")
def main():
    st.title("calculator")
    num1 = st.text_input("Enter a num")
    sign = st.text_input("Enter a sign(+, -, x, /)")
    num2 = st.text_input("Enter a 2nd numnber")
    if st.button("Calculate"):
        try:
            num1 = float(num1)
            num2 = float(num2)
            if sign == "+":
                result = num1 + num2
            elif sign == "-":
                result = num1 - num2
            elif sign == "x":
                result = num1 * num2
            elif sign == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    st.error("Cannot divide by zero")
                    return
            else:
                st.error("Invalid sign")
                return
            st.success(f"The result is: {result}")
        except ValueError:
            st.error("Please enter valid numbers")
if __name__ == "__main__":
    main()