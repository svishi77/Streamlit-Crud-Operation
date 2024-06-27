import mysql.connector
from requests import post
import streamlit as st
# Establish Database Connection

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@123",
    database="crud_new1"
)
mycursor = mydb.cursor()
print("Connection Establish")

def main():
    st.title("CRUD Operation with MYSQL")
    # Creating Side bar for CRUD Options
    option = st.sidebar.selectbox("Select an Option",["Create", "Read", "Update","Delete"])
    if option == "Create":
        st.subheader("Create Records")
        name = st.text_input("Enter Name")
        email = st.text_input("Enter Email")
        if st.button("Create"):
            sql = "insert into users(name,email) values(%s,%s)"
            val = (name, email)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record created successfully!")
    
    elif option == "Read":
        st.subheader("Read Records")
        mycursor.execute("select * from users")
        results = mycursor.fetchall()
        for result in results:
            st.write(result)

    elif option == "Update":
        st.subheader("Update the Records")
        id = st.number_input("Enter User ID")
        name = st.text_input("Enter User Name")
        email = st.text_input("Enter User Email")
        if st.button("Update"):
            sql = "UPDATE users SET name=%s, email=%s WHERE id=%s"
            val = (name,email,id)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Updated Successfully")
    
    elif option == "Delete":
        st.subheader("Delete the Records")
        id = st.number_input("Enter User ID")
        if st.button("Delete"):
            sql = "DELETE from users WHERE id=%s"
            val = (id,)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Deleted Successfully")
    

if __name__ == "__main__":
    main()