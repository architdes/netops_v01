#COMMENTED OUT MODULE - UNCOMMMENT IN PROD ENVIRONMENT
#import maskpass
import inquirer
import time
from templates.src import new_deploy
from templates.src import firewall_policy
from templates.src import basic_firewall_validation
from templates.src import advance_firewall_validation

def service_select():
    # list of function performed by the program
    fortios_functions = ['New Deployment', 'Firewall Policy', 'Firewall validation basic', 'Firewall validation advance', 'Return']
    
    # user selection for required service
    user_choice = inquirer.List('select', 
                                message="What is function you want proceed with?",
                                choices=fortios_functions,
                                ),
    
    selected_choice = inquirer.prompt(user_choice)


    # nested if for each of the function to redirect program to correct function. individual function will be in ./template directory
    if selected_choice['select'] == fortios_functions[0]:
        new_deploy.main()
    elif selected_choice['select'] == fortios_functions[1]:
        firewall_policy.main()
    elif selected_choice['select'] == fortios_functions[2]:
        basic_firewall_validation.main()
    elif selected_choice['select'] == fortios_functions[3]:
        advance_firewall_validation.main()
    elif selected_choice['select'] == fortios_functions[4]:
        print("")
    else:
        # this option will be only visibile to user, if there is code issue within nestedif
        print("Contact Admministrator")
    
    return


if __name__ == "__main__":

    ts = time.time()
    
    #REQUEST FOR THE USERNAME AND SECRET TO CONNECT THE FIREWALL
    #COMMENTED OUT FOR DEV ENVIRONTMENT
    #username = input("Enter the username: ")
    #password = maskpass.askpass()
    
    #USING USERNAME AND PASSWORD VARIABLES FOR DEV ENVIRONMENT
    username = 'adesai'
    password = 'QAZX!@34qazx'

    #CALLING SERVICE QUESTIONARY FUNCTION
    service_select()

    tf = time.time()
    print('End of Program, ended in ' + str(tf-ts) + ' seconds')