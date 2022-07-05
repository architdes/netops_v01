"""
This is the program is to pull data from the templates/csv/firewall_deployment.csv folder and 
create a fortinet template.
"""

import pandas as pd
import inquirer
import maskpass

def validate_mgmt_ips(management_ips):
    

    pass

def host_names(dict):

    primary_hostname = dict['SITE CODE'] + '-' +dict['SEGMENTATION TYPE'] + '-FORT-FW01'
    secondary_hostname = dict['SITE CODE'] + '-'+ dict['SEGMENTATION TYPE'] + '-FORT-FW02'

    user_choice = inquirer.List('select',
                                message=("Are you good with firewall hostnames " + primary_hostname + ' and ' + secondary_hostname + '?'),
                               choices=['Yes', 'No']),

    selected_choice = inquirer.prompt(user_choice)['select']

    if selected_choice == 'Yes':
        dict.update({"primary_hostname": primary_hostname, "secondary_hostname": secondary_hostname})
    else:
        primary_hostname = input("Enter Hostname for Primary Firewall: ")
        secondary_hostname = input("Enter Hostname for Slave Firewall: ")
        dict.update({"primary_hostname": primary_hostname, "secondary_hostname": secondary_hostname})

    pass


def standalone_mode_configuration(dict):
    print("")
    print("WORKING IN PROGRESS")
    pass

def active_passive_mode_configuration(dict):
    print("")
    host_names(dict)
    management_ips = dict['MANAGEMENT IPS'].split(',')
    validate_mgmt_ips(management_ips)
    dict.update({'mgmt_ip1': management_ips[0], 'mgmt_ip2': management_ips[1]})
    ha_interfaces = dict['HA INTERFACES'].split(',')
    dict.update({'ha_intf1': ha_interfaces[0], 'ha_intf2': ha_interfaces[1]})
    tacacs_secret = maskpass.askpass(prompt='Enter TACACS KEY: ')
    dict.update({'tacacs_key': tacacs_secret})

    pass

def active_active_mode_configuraton(dict):
    print("")
    print("WORKING IN PROGRESS")
    pass

def basic_info_append(dict):
    if dict['HA MODE'] == 'standalone':
        standalone_mode_configuration(dict_basic)
    elif dict['HA MODE'] == "a-p":
        active_passive_mode_configuration(dict_basic)
    elif dict['HA MODE'] == 'a-a':
        active_active_mode_configuraton(dict_basic)
    else:
        print("Incorrect HA Mode selected")
    pass


def main():
    global dict_basic

    # parsing the firewall deployment.xlsx to pandas data frame
    df_basic_info = pd.read_excel('./templates/workbook/firewall_deployment.xlsx',
                                    nrows=13,
                                    usecols= ['FIELD NAME', 'USER INPUT'],
                                    index_col=0)

    # converting the panda dataframe to dictonary
    dict_basic = df_basic_info.to_dict().get('USER INPUT')

    basic_info_append(dict_basic)

    print(dict_basic)
    pass


if __name__ == "__main__":
    main()