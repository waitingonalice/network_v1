# K3s
## Pre-requisites
1. A server with Ubuntu 24.04 installed
2. A user with sudo privileges
3. A static IP address
4. A fully qualified domain name (FQDN) pointing to the static IP address
5. A firewall configured to allow traffic on ports 80, 443, and 6443
6. A basic understanding of Kubernetes
7. A basic understanding of Docker
8. A basic understanding of Helm
9. A basic understanding of networking
  
## Setup

### Install k3s

```
 curl -sfL https://get.k3s.io | sh -s - server \
    --token=$TOKEN \
    --cluster-init \
    --tls-san=$IP_ADDRESS --tls-san=$FQDN
```
- this command will install k3s on the server and configure it as a master node
- replace `$IP_ADDRESS` with the static IP address of the server
- replace `$FQDN` with the fully qualified domain name of the server
- the `--cluster-init` flag will configure the server as a master node
- `TOKEN` is a unique token that is used to authenticate nodes in the cluster. To be generated by the user.

### Adding more nodes as master
```
curl -sfL https://get.k3s.io | sh -s - server \
    --token=$TOKEN \
    --server=https://$IP_ADDRESS:6443 \
    --tls-san=$IP_ADDRESS --tls-san=$FQDN
```

- This command will link a new node with the --server flag pointing to the master node

### Adding worker nodes
```
sudo k3s agent --server https://$IP_ADDRESS:6443 --token $TOKEN
```
