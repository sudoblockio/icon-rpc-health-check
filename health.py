import os
import json
import logging
import requests

REFERENCE_HOSTS = {
    'mainnet': 'https://ctz.solidwallet.io,https://api.icon.community',
    'sejong': 'https://sejong.net.solidwallet.io,https://api.sejong.icon.community',
    'berlin': 'https://berlin.net.solidwallet.io,https://api.berlin.icon.community',
    'lisbon': 'https://lisbon.net.solidwallet.io,https://api.lisbon.icon.community',
}


def health_check():
    target_host = os.environ.get('HC_CHECK_HOST')
    network = os.environ.get('HC_NETWORK_NAME', 'mainnet')
    reference_hosts = os.environ.get('HC_REFERENCE_HOSTS', REFERENCE_HOSTS[network])
    block_height_threshold = int(os.environ.get('HC_BLOCK_HEIGHT_THRESHOLD', 30))

    rpc_request = {"jsonrpc": "2.0", "method": "icx_getLastBlock", "id": 1234}
    current_block_height = 0
    reference_block_height = 0
    for i in reference_hosts.split(','):
        url = i + '/api/v3'
        r = requests.post(url, data=json.dumps(rpc_request))
        if r.status_code != 200:
            continue
        reference_block_height = r.json()['result']['height']
        if reference_block_height > current_block_height:
            current_block_height = reference_block_height

    if current_block_height == 0:
        logging.warning("Reference nodes down. Don't flip health check.")
        exit(0)

    if reference_block_height == 0:
        logging.warning("Nodes not able to be reached. Unhealthy.")
        exit(1)

    r = requests.post(target_host + '/api/v3', data=json.dumps(rpc_request))
    if r.status_code != 200:
        logging.warning("Target not able to be reached. Unhealthy.")
        exit(1)

    # TODO: Add multiple hosts / make multiple calls
    #  Currently we do not support active health checks so making one call could fail when
    #  one host is out of sync and that is the response over a load balancer. Not sure what
    #  best solution is.

    target_block_height = r.json()['result']['height']
    if target_block_height + block_height_threshold < reference_block_height:
        logging.warning("Nodes are out of sync. Unhealthy.")
        exit(1)


if __name__ == '__main__':
    health_check()
