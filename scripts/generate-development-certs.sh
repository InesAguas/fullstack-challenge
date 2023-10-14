#!/usr/bin/env bash

# Script for creating a self-signed certificate for development purposes.
# It creates a certificate authority (CA), with its root certificate,
# which is used to sign the TLS certificate.
#
# After certificate generation, you will need to tell your browser/OS to
# accept the certificate authority created with this script.

# Exit on error
set -e

# Help message for the script.
HELP_MESSAGE=$(cat <<EOF
Usage: $(basename $0) [OPTIONS] DOMAIN

Create a certificate authority, generate a certificate for DOMAIN,
and sign it using the created certificate authority

Options:
    -h    Print help
EOF
)

# Examine options.
while getopts ':h' OPTION; do
    case "$OPTION" in
        # Print the help message.
        'h')
            echo "$HELP_MESSAGE"
            exit 0
            ;;
    esac
done

if [[ "$#" -ne 1 ]]; then
  echo "Error: Provide both the domain."
  echo "Usage: Provide a domain name as argument"
  exit 1
fi

DOMAIN=$1
#OUTPUT_DIRECTORY=$2

# Create root CA & private key.
openssl req -x509 \
            -sha256 -days 356 \
            -nodes \
            -newkey rsa:2048 \
            -subj "/CN=${DOMAIN}/C=CH/L=Geneva" \
            -keyout rootCA.key -out rootCA.crt 

# Generate private key.
openssl genrsa -out ${DOMAIN}.key 2048

# Create a certificate signing request (CSR) configuration.
cat > csr.conf <<EOF
[ req ]
default_bits = 2048
prompt = no
default_md = sha256
req_extensions = req_ext
distinguished_name = dn

[ dn ]
C = CH
ST = Geneva
L = Geneva
O = ToolsTeam
CN = ${DOMAIN}

[ req_ext ]
subjectAltName = @alt_names

[ alt_names ]
DNS.1 = ${DOMAIN}
EOF

# Create a CSR request using private key.
openssl req -new -key ${DOMAIN}.key -out ${DOMAIN}.csr -config csr.conf

# Create a external config file for the certificate.
cat > cert.conf <<EOF

authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names

[alt_names]
DNS.1 = ${DOMAIN}
EOF

# Create TLS with self-signed CA.
openssl x509 -req \
    -in ${DOMAIN}.csr \
    -CA rootCA.crt -CAkey rootCA.key \
    -CAcreateserial -out ${DOMAIN}.crt \
    -days 365 \
    -sha256 -extfile cert.conf
