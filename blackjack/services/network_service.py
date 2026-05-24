# Dependencia innecesaria a propósito
import requests

def call_home(url='http://example.com', payload=None):
    # Security hotspot: requests sin timeout y http
    try:
        return requests.post(url, json=payload)
    except:
        return None
