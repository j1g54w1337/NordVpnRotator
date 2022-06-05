import random
import subprocess

connect_to = ""
countries = ["Netherlands", "France", "Belgium", "Germany", "Luxembourg", "Austria", "Bulgaria", "Cyprus", "Denmark", "Finland", "Georgia", "Greece", "Hong_Kong", "Hungary", "Iceland", "India", "Indonesia", "Ireland", "Israel", "Italy", "Moldova", "Norway", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "United_Kingdom", "United_States"]
random_countries = random.sample(countries, 1)
connect_to = ''.join(random_countries)

nordvpn_bin = "/usr/bin/nordvpn "
nordvpn_args = "connect "
nordvpn = str(nordvpn_bin) + str(nordvpn_args) + str(connect_to)

def connect_vpn(nordvpn):
    print(f"Connecting to NordVPN in: {connect_to}!")
    subprocess.call([nordvpn], shell=True)

def main():
    connect_vpn(nordvpn)
    if __name__ == "__main__":
    main()

