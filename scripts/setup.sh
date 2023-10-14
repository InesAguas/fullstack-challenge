ROOT_DIR="$(pwd)"

# Create external volume for the DB if does not exist.
DB_VOLUME='postgres-data'
if [[ -z $(docker volume ls --filter "name=${DB_VOLUME}" --format "{{.Name}}") ]]; then
    echo '==> Creating a docker volume for the local DB instance...'
    docker volume create ${DB_VOLUME}
fi


# Create a directory for self-signed certificate if it does not exist.
DEVELOPMENT_CERTS_DIR="$ROOT_DIR/development-certs"
# Set extended pattern matching. It needs to be set before the context in which it is used (the `if` statement in this case).
shopt -s extglob
if [[ ! -d $DEVELOPMENT_CERTS_DIR ]]; then
    echo "==> 📜 Creating a certificate authority & generating a self-signed certificate..."
    mkdir $DEVELOPMENT_CERTS_DIR
    # Generate a self-signed certificates.
    cd $DEVELOPMENT_CERTS_DIR
    $ROOT_DIR/scripts/generate-development-certs.sh localhost
    chmod 0600 rootCA.crt localhost.crt localhost.key
    rm !(rootCA.crt|localhost.crt|localhost.key) # Remove certicate-related files which are not needed anymore.
    cd $ROOT_DIR
    TODO_LIST="$TODO_LIST\n    - Instruct your browser/OS to accept the created certificate authority by passing rootCA.crt."
fi

echo "🎉 Set up complete!"

# Print the TODO list.
if [[ -n "$TODO_LIST" ]]; then
    TODO_LIST_INTRO="📝 Do the following actions before starting apps:"
    printf "$TODO_LIST_INTRO$TODO_LIST\n"
fi