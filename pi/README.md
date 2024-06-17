## Setup:
- Clone repo and cd into directory
- Run script from ./setup-packages.sh 
	- It will set up docker and install other relevant packages

## Pihole

To set Pihole, you would need to disable Ubuntu's DNS resolver, and set the DNS server to the Pihole's IP address.

```
sudo systemctl stop systemd-resolved.service
sudo systemctl disable systemd-resolved.service
sudo nano /etc/resolv.conf
```

Edit nameserver to something accessible first.
nameserver 8.8.8.8

To revert the settings,
```
sudo systemctl enable systemd-resolved.service
sudo systemctl start systemd-resolved.service
sudo nano /etc/resolv.conf
```

Edit nameserver to the original address
nameserver 127.0.0.53
options edns0 trust-ad
search .


### Usage
Pihole should contain these volumes to run:
- etc-dnsmasq.d
- etc-pihole

