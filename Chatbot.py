def classify_query(query):
    query=query.lower()
    if "service" in query:
        return "Services"
    elif "career" in query or "job" in query:
        return "Career Enquiries"
    elif "product" in query or "Raid" in query or "DataMaster" in query:
        return "Products"
    else:
        return "Unknown"
def Charlie():
    print("Hello! I'm Charlie.")
    print("How can i Help you today!")
    while True:
        print("Please choose an option from the menu below:")
        print("1. Services")
        print("2. Career Enquiries")
        print("3. Products")
        print("4. Exit")
        choice=input("Enter the number of your choice: ")
        if choice == "1":
            service=input("Which service would you like to choose? (Infrastructure, Cloud, Data Modernization, etc.): ")
            username=input("What's your name? ")
            contact=input("Please provide your contact number: ")
            print(f"Thank you, {username}! Our team will get in touch with you soon at {contact} regarding {service}.")
        elif choice=="2":
            print("You can find career opportunities on our Careers page.")
        elif choice == "3":
            product_info=input("Which product would you like to know about? (Raid, DataMaster): ")
            username=input("What is your name? ")
            contact=input("Please enter your contact number: ")
            print(f"Thank you, {username}! We will keep you updated soon about {product_info}.")
        elif choice == "4":
            print("Thank you for using our chatbot! Have a wonderful day!")
            break
        else:
            print("Invalid choice, please select a valid option.")
        additional_query = input("Do you have any other questions? (yes/no): ").lower()
        if additional_query != "yes":
            break
if __name__ == '__main__':
    Charlie()
