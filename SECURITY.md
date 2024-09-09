# Security Policy

Report your findings to our H1 program: https://hackerone.com/coinbase
grpcurl -import-path ./proto/ -proto blockchain.proto -d '{\"asset\": {\"chain\": \"100\", \"code\": \"ether\"}, \"address\": {\"address_single\": {\"address\": \"0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2\"}}}' -plaintext 127.0.0.1:2449 emerald.Blockchain/SubscribeBalance
