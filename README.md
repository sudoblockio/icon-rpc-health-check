# ICON RPC Health-Checker Pod

This pod is a repackaging of the [Gruntwork Health Checker](https://github.com/gruntwork-io/health-checker) to allow it to proxy health check requests for ICON nodes externally.

## Environment Variables

[//]: # (- HC_CHECK_PORT)
- HC_CHECK_HOST
  - Required
- HC_LISTEN_PORT
  - Required
- HC_NETWORK_NAME
  - One of mainnet, sejong, lisbon, berlin
  - Defaults to `mainnet`
- HC_REFERENCE_HOSTS 
  - Comma separated list of nodes to check block height for a reference
  - Defaults to: `https://ctz.solidwallet.io,http://api.icon.community`
- HC_BLOCK_HEIGHT_THRESHOLD
  - Defaults to 30 (1 min of blocks)
