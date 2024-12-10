import streamlit as st

def calculate(num1, num2, operation):
    
    try:
        num1 = float(num1)
        num2 = float(num2)
        
        if operation == 'Sum':
            return num1 + num2
        elif operation == 'Sub':
            return num1 - num2
        elif operation == 'Mult': 
            return num1 * num2
        elif operation == 'Div':
             if num2 == 0:
                return 'Error: division by zero!'
             return num1 / num2
    except ValueError:
        return 'Error: invalid input!Please insert numbers'

st.title('Basic Calculator')
st.write('Choose two numbers and the operation you want to do')

num1 = st.text_input('Type in the first number')
num2 = st.text_input('Type in the second number')
operation = st.selectbox('Choose the operation:', ['Sum', 'Sub', 'Mult', 'Div'])

if st.button('Calculate'):
   result = calculate(num1, num2, operation)
   st.write (f"Result: {result}")