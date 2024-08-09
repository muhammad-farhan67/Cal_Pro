import streamlit as st 
st.title("Simple Calculator")
num_1 = st.number_input("Enter the First Number ")
num_2 = st.number_input("Enter the Second Number ")
operation = st.selectbox("Select the operation",["Add","Subtract","Multiply","Divide"])
if operation == "Add":
    result = num_1+num_2
elif operation == "Subtract":
    result = num_1 - num_2
elif operation == "Multiply":
    result = num_1 * num_2
elif operation == "Divide" :
  if num_2 != 0:
      result = num_1 / num_2
  else :
      result = "Error! Zero can't be divided"
st.write("Result",result)