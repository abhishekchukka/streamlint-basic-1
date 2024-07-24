import streamlit as st
st.title("Prime")
a=st.text_input(label="Enter a number")
print(a)
if st.button("Submit"):
    num=abs(int(a)) 
    f=0
    for i in range(1,num+1):
        if (num%i==0):
            f+=1
    if(f==1):
        st.subheader(" 1 is neither Prime nor Co-prime")
    elif(f==2):
        st.subheader(" Prime Number")
    else:
        st.subheader("Not a Prime Number")
