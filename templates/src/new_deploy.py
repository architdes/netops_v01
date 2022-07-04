"""
This is the program is to pull data from the templates/csv/firewall_deployment.csv folder and 
create a fortinet template.
"""

import pandas as pd


class firewall_basic_info:

    def __init__(self, df):
        self.firewall_model = df.at['FIREWALL MODEL', 'USER INPUT']
        self.site_code = df.at['SITE CODE','USER INPUT']
        self.cluster_number = df.at['CLUSTER NUMBER', 'USER INPUT']
        self.segmentation_type = df.at['SEGMENTATION TYPE', 'USER INPUT']
        self.region = df.at['REGION', 'USER INPUT']
        self.mgmt_interface = df.at['MANAGEMENT INTERFACE', 'USER INPUT']
        self.mgmt_ips = df.at['MANAGEMENT IPS', 'USER INPUT']
        self.mgmt_netmask = df.at['MANAGEMENT NETMASK', 'USER INPUT']
        self.mgmt_gateway = df.at['MANAGEMENT GATEWAY', 'USER INPUT']
        self.ha_mode = df.at['HA MODE', 'USER INPUT']
        self.ha_interfaces = df.at['HA INTERFACES', 'USER INPUT']
        self.lacp_interfaces = df.at['LACP INTERFACES', 'USER INPUT']
        self.default_gateway = df.at['DEFAULT GATEWAY', 'USER INPUT']

    def firewall_basic_info_print(self):
        print("Firewall Model is " + self.firewall_model)
        print("site code is " + self.site_code)
        print("Cluster Number is" + self.cluster_number)
        print("Segmentation type is" + self.segmentation_type)
        print("Region is " + self.region)
        print("Management Interfaces is " + self.mgmt_interface)
        print("Management IPs are " + self.mgmt_ips)
        print("Management gateway is " + self.mgmt_gateway)
        print("HA mode is " + self.ha_mode)
        print("HA interfaces are " + self.ha_interfaces)
        print("LACP interfaces are " + self.lacp_interfaces)
        print("Default route is " + self.default_gateway)



def main():

    df_basic_info = pd.read_excel('./templates/workbook/firewall_deployment.xlsx', 
                                    nrows=12, 
                                    usecols= ['FIELD NAME', 'USER INPUT'],
                                    index_col=0)
    print(df_basic_info)
    p1 = firewall_basic_info(df_basic_info)

if __name__ == "__main__":
    main()