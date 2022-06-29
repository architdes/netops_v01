import maskpass
import inquirer



def func_call_redirect(choice):
    
    
    if choice['select'] == 'New Deployment':
        print('selected 1')
        #deployment_new_firewall()
    elif choice['select'] == 'Firewall Policy':
        print('selected 2')
        #deployment_()
    return

def tech_selection():
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