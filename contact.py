contacts = {}

while True:
    print('\n Contact Book App')
    print('1. Create Contact')
    print('2. View Contact')
    print('3. Update  Contact')
    print('4. Delete Contact')
    print('5. Search Contact')
    print('6. Count Contact')
    print('7. Exit ')

    choice = input('Enter Your Choice : ')

    if choice == '1':
        name = input('Enter Your Name : ')
        if name in contacts :
          print(f'Contact name {name} already exists ! ')
        else:
          age = input('Enter age = ')
          email = input('Enter email = ')
          mobile = input('Enter mobile number = ')
          contacts[name] = {'age': int(age), 'email': email, 'mobile' : mobile}
          print(f'Contact name {name} has been created successfully!')


    elif choice == '2':
      name = input('Enter Contact Name to view : ')
      if name in contacts :
         contact = contacts[name]
         print(f'Name : {name}, Age : {age}, Mobile Number : {mobile}')
      else:
         print('Contact not found')


    elif choice == '3':
        name = input('Enter Contact Name to Update Contact : ')
        if name in contacts :
       
          age = input('Enter updated age = ')
          email = input('Enter updated email = ')
          mobile = input('Enter updated mobile number = ')
          contacts[name] = {'age': int(age), 'email': email, 'mobile' : mobile}
          
        else:
            print('Contact not found')
         
       
    elif choice == '4':
         name = input('Enter Contact Name to delete contact : ')
         if name in contacts :
            del contacts[name]
            print(f'Contact name {name} has been deleted successfully!')
         else:
            print('Contact not found')

    elif choice == '5':
         search_name = input('Enter Contact Name to search : ')
         if name in contacts :
            found = False
            for name,contacts in contacts.items():
               if search_name.lower() in name.lower():
                  print(f"Found - Name {name}, Age:{age}, Mobile Number: {mobile}, Email : {email}") 
            if not found:
               print("No contact found with that name")

    elif choice == '6':
       print(f'Total contacts : {len(contacts)}')           
            
                
    elif choice == '7':
       print('Good Bye ...Closing the Program')
       break
    
    else:
       print("Invalid Input")
       