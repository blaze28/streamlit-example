st.sidebar.title("Your Information")

Name = st.sidebar.text_input("Full Name")
Contact_Number = st.sidebar.text_input("Contact Number")
Email_address = st.sidebar.text_input("Email address")

if not Name or not Email_address:
   st.sidebar.warning("Please fill out your name and email address")
else:
   if st.sidebar.button("Submit"):
        # Define the path to store the entered data
       csv_path = "data.csv"

        # Prepare the data as a dictionary
       data = {
        "Name": Name,
         "Contact Number": Contact_Number,
         "Email Address": Email_address
          }

        # Write the data to a CSV file
       with open(csv_path, mode='a', newline='') as file:
         writer = csv.DictWriter(file, fieldnames=data.keys())
         if file.tell() == 0:
            writer.writeheader()  # Write the header if the file is empty
         writer.writerow(data)

       st.sidebar.success("Thanks for submitting your information!")
