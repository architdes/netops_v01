"""
This is the program is to pull data from the templates/csv/firewall_deployment.csv folder and 
create a fortinet template.
"""

import pandas as pd

def standalone_mode_configuration(dict):
    print("")
    print("WORKING IN PROGRESS")
    return

def active_passive_mode_configuration(dict):
    print("")
    print("WORKING IN PROGRESS")
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

"""
class firewall_basic_info:

    def __init__(self, *args, **kwargs):
        self.firewall_model = df_basic_info.at["FIREWALL MODEL", 'USER INPUT']
        self.site_code = df_basic_info.at['SITE CODE','USER INPUT']
        self.cluster_number = df_basic_info.at['CLUSTER NUMBER', 'USER INPUT']
        self.segmentation_type = df_basic_info.at['SEGMENTATION TYPE', 'USER INPUT']
        self.region = df_basic_info.at['REGION', 'USER INPUT']
        self.mgmt_interface = df_basic_info.at['MANAGEMENT INTERFACE', 'USER INPUT']
        self.mgmt_ips = df_basic_info.at['MANAGEMENT IPS', 'USER INPUT']
        self.mgmt_netmask = df_basic_info.at['MANAGEMENT NETMASK', 'USER INPUT']
        self.mgmt_gateway = df_basic_info.at['MANAGEMENT GATEWAY', 'USER INPUT']
        self.ha_mode = df_basic_info.at['HA MODE', 'USER INPUT']
        self.ha_interfaces = df_basic_info.at['HA INTERFACES', 'USER INPUT']
        self.lacp_interfaces = df_basic_info.at['LACP INTERFACES', 'USER INPUT']
        self.default_gateway = df_basic_info.at['DEFAULT GATEWAY', 'USER INPUT']

    def firewall_basic_info_print(self):
        print("Firewall Model is " + self.firewall_model)
        print("site code is " + self.site_code)
        print("Cluster Number is" + str(self.cluster_number))
        print("Segmentation type is" + self.segmentation_type)
        print("Region is " + self.region)
        print("Management Interfaces is " + self.mgmt_interface)
        print("Management IPs are " + self.mgmt_ips)
        print("Management gateway is " + self.mgmt_gateway)
        print("HA mode is " + self.ha_mode)
        print("HA interfaces are " + self.ha_interfaces)
        print("LACP interfaces are " + self.lacp_interfaces)
        print("Default route is " + self.default_gateway)

"""

def main():
    global dict_basic

    # parsing the firewall deployment.xlsx to pandas data frame
    df_basic_info = pd.read_excel('./templates/workbook/firewall_deployment.xlsx',
                                    nrows=13,
                                    usecols= ['FIELD NAME', 'USER INPUT'],
                                    index_col=0)

    # converting the panda dataframe to dictonary
    dict_basic = df_basic_info.to_dict().get('USER INPUT')
    print(dict_basic['HA MODE'])
    basic_info_append(dict_basic)


if __name__ == "__main__":
    main()