import maskpass
import inquirer



def func_call_redirect(choice):
    

    if choice['select'] == fortios_functions[0]:
        print(choice['select'])
    elif choice['select'] == fortios_functions[1]:
        print(choice['select'])
    elif choice['select'] == fortios_functions[2]:
        print(choice['select'])
    elif choice['select'] == fortios_functions[3]:
        print(choice['select'])
    else:
        print("Contact Admministrator")
    return

def tech_selection():
    global fortios_functions
    
    fortios_functions = ['New Deployment', 'Firewall Policy', 'Firewall validation basic', 'Firewall validation advance']
    user_choice = inquirer.List('select', 
                                message="What is function you want proceed with?",
                                choices=fortios_functions,
                                ),
    
    selected_choice = inquirer.prompt(user_choice)
    func_call_redirect(selected_choice)
    
    return

def main():
    #username = input("Enter the username: ")
    #password = maskpass.askpass()
    #host = input("Enter the hostname: ")
    
    #username = 'adesai'
    #password = 'QAZX!@34qazx'
    #host = '10.0.0.31'
    
    #print(username)
    #print(password)
    #print(host)
    tech_selection()
    
    return

if __name__ == "__main__":
    main()