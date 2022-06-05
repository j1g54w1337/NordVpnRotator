# NordVPN IP Rotator
## Info
This little program rotates your VPN location and IP address. When you configre crontab, you can automate this process every couple of minutes, hours, etc.

## Pre-requesites
* Python 3
* [NordVPN Linux Client](https://support.nordvpn.com/Connectivity/Linux/1325531132/Installing-and-using-NordVPN-on-Debian-Ubuntu-Raspberry-Pi-Elementary-OS-and-Linux-Mint.htm)
* Logged in to NordVPN

## Setup
1. Checkout the repository: `git clone https://github.com/j1g54w1337/NordVpnRotator.git`
2. Install required modules with `pip install -r ./requirements`
3. Login to NordVPN
4. OPTIONAL: Create a crontab (See example)

## Example
### Crontab
* To refresh your location and IP every 5 minutes and start at `boot` time, you can use the following crontab:
```
@reboot /usr/local/bin/NordVpnRotator/NordVpnRotator.py
*/5 * * * * /usr/local/bin/NordVpnRotator/NordVpnRotator.py
```

## ToDo
* For starting at boot time it's maybe better to use systemd, but for now the crontab will also do the trick.

