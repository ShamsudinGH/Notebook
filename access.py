from fastapi import Request, HTTPException
from ipaddress import ip_address, ip_network

LOCAL_NETWORKS = [
    ip_network("127.0.0.0/8"),
    ip_network("192.168.0.0/16"),
]

def load_allowed_ips():
    with open("allowed_ips.txt") as f:
        return {line.strip() for line in f if line.strip()}

def check_ip(request: Request):
    client_ip = ip_address(request.client.host)

    # локальная сеть
    for net in LOCAL_NETWORKS:
        if client_ip in net:
            return

    # внешний IP
    allowed = load_allowed_ips()
    if str(client_ip) not in allowed:
        raise HTTPException(status_code=403, detail="IP not allowed")
