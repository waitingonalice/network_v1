## Ansible


### Set up

To set up ansible, a list of packages will need to be installed:
- openssh-server
- sshpass
- ansible
- python3

To install these packages, run the following command:
```
sudo apt install openssh-server sshpass ansible python3
```
Steps: 
1. Create a new directory for the ansible project
2. Create a new file called `hosts` or `inventory` in the directory. This file will contain the IP addresses of the servers that ansible will be managing.
3. Create a new file called `playbook.yml` in the directory. This file will contain the tasks that ansible will perform on the servers.
4. Create a new file called `ansible.cfg` in the directory. This file will contain the configuration settings for ansible.

### Usage
- To test connectivity with hosts, execute this command:
```
ansible -i $inventory_filename $server_group -m ping --ask-pass
```

- To execute a playbook: 
```
ansible-playbook -kK -i $inventory_file $playbook_file
```
