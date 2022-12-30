from scapy.all import *

def ping(ip_address: str, ttl: int = 5, verbose: bool = False) -> bool:
    packet = IP(dst=ip_address, ttl=ttl)/ICMP()
    reply = sr1(packet, timeout = ttl)
    if reply is not None:
        if verbose:
            print(reply)
        return True
    else:
        return False
    
if __name__ == '__main__':
    ping("8.8.8.8", verbose=True)
