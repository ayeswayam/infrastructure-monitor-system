def validate_host_payload(payload):
    required = ['hostname','ip_address']
    missing = [r for r in required if r not in payload]
    return missing
