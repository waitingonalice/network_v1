# Nginx + Let's Encrypt

## Topology
```
viewer → jellyfin.wilson-crib.com (Cloudflare DNS, gray cloud) → VPS nginx :443 → Tailscale → home Jellyfin (100.99.14.22:8096)
```
- Nginx runs bare metal on a public VPS that is on the tailnet. Only the VPS IP is public; the home network stays behind Tailscale.
- Media hostnames are gray cloud (DNS only) to skip the Cloudflare proxy hop and its free-plan video limits. The other hostnames can stay orange.
- With gray cloud, Cloudflare no longer presents a client cert, so the `ssl_client_certificate` / `ssl_verify_client` lines (Authenticated Origin Pulls) must be removed or commented out.
- [nginx-template.conf](nginx-template.conf) is a reference copy. The live config is on the VPS.

## Issue a cert
`-d` takes a bare hostname (no `https://`), and the hostname needs an A/AAAA record. `wilson-crib.com` itself has none.

**HTTP challenge** (needs port 80 open on the VPS and the record pointing at the VPS):
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d jellyfin.wilson-crib.com
```

Injects `ssl_certificate` lines (`# managed by Certbot`) into the server block whose `server_name` matches. Renewal runs from a systemd timer and reloads nginx. To test it:
```bash
sudo certbot renew --dry-run
```

## Streaming settings
Put these inside `location /` of the media server block, so nginx streams without buffering:
```nginx
proxy_buffering off;
proxy_request_buffering off;
proxy_read_timeout 3600s;
proxy_send_timeout 3600s;
client_max_body_size 0;
```
Apply with `sudo nginx -t && sudo systemctl reload nginx`.

## Checks
- `dig +short jellyfin.wilson-crib.com` returns the VPS IP, not Cloudflare's 104.21.x / 172.67.x.
- `tailscale ping 100.99.14.22` from the VPS shows `via <ip>:<port>`. If it shows `via DERP`, traffic is relayed and streaming will be slow. Open UDP 41641 and check `tailscale netcheck` on both ends.
- The VPS firewall only allows 80, 443, SSH (preferably Tailscale-only) and UDP 41641.
- Watch the VPS egress allowance, since every remote stream passes through it.
