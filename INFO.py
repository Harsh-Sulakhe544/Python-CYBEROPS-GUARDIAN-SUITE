import subprocess

class SystemInformation:
    # use constructor 
    
    def __init__(self):
        # make system_info as dictionary 
        self.system_info = {}

    def run_command(self, command):
        result = subprocess.run(command, stdout=subprocess.PIPE, text=True)
        return result.stdout

    def get_value(self, output, key):
        start_index = output.find(key)
        end_index = output.find("\n", start_index)

        # Extract the value between the key and the newline character
        value = output[start_index + len(key):end_index].strip()

        return value

    def get_system_info(self):
        # Get general system information, run the system command systeminfo 
        systeminfo_output = self.run_command("systeminfo")

        # these below are the keys as we have in systemiunfo command 
        relevant_info = [
            "Host Name", "OS Name", "OS Version", "OS Manufacturer", "OS Configuration",
            "OS Build Type", "Registered Owner", "Registered Organization", "Product ID",
            "Original Install Date", "System Boot Time", "System Manufacturer",
            "System Model", "System Type", "Processor(s)", "BIOS Version",
            "Windows Directory", "System Directory", "Boot Device", "System Locale",
            "Input Locale", "Time Zone", "Total Physical Memory", "Available Physical Memory",
            "Virtual Memory: Max Size", "Virtual Memory: Available", "Virtual Memory: In Use",
            "Page File Location(s)", "Domain", "Logon Server", "Hyper-V Requirements",
        ]

        # u can CALL SAME FUNCTION IN SAME CLASS USING self.method() => otherwise error 
        for key in relevant_info:
            self.system_info[key] = self.get_value(systeminfo_output, key)

        # Get network information - use ipconfig-command 
        ipconfig_output = self.run_command("ipconfig /all")
        network_info = self.get_network_info(ipconfig_output)
        self.system_info["Network Card(s)"] = network_info

        # Get hotfix information , use comand  # wmic qfe list brief ->
        # it will give u everything about hostfix - quick correction-program for any software-issues 
        hotfix_output = self.run_command("wmic qfe list brief")
        hotfix_info = self.get_hotfix_info(hotfix_output)
        self.system_info["Hotfix(s)"] = hotfix_info

        return self.system_info

    def get_network_info(self, output):
        network_info = []
        interfaces = output.split("\n\n")

        for interface in interfaces:
            # search for Ethernet adapter and LAN
            if "Ethernet adapter" in interface or "Wireless LAN adapter" in interface:
                network_card = self.get_value(interface, "Description")
                dhcp_enabled = self.get_value(interface, "DHCP Enabled")
                ip_addresses = self.get_ip_addresses(interface)
                
                card_info = {
                    "Connection Name": network_card,
                    "DHCP Enabled": dhcp_enabled,
                    "IP address(es)": ip_addresses,
                }

                network_info.append(card_info)

        return network_info

    def get_ip_addresses(self, interface_output):
        # Extracts IPv4 addresses from the interface output using string methods
        ip_addresses = []
        lines = interface_output.split("\n")

        for line in lines:
            if "IPv4 Address" in line:
                parts = line.split(":")
                if len(parts) == 2:
                    ip_address = parts[1].strip()
                    ip_addresses.append(ip_address)

        return ip_addresses

    def get_hotfix_info(self, output):
        # Extracts hotfix information from the output of "wmic qfe list brief"
        hotfix_info = []
        lines = output.split("\n")

        for line in lines[2:]:
            hotfix_entry = line.strip().split(None, 2)
            if len(hotfix_entry) >= 3:
                hotfix_info.append(hotfix_entry)

        return hotfix_info
