#!/usr/bin/env bash
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
LBLUE='\033[0;36m'
NC='\033[0m' # No Color
printf "\n${LBLUE}Hello there :)${NC}\n"
echo "The script start and it will ${LBLUE}build docker image${NC} and ${LBLUE} run it${NC} for You."
printf "\n\n"

docker build . -t qredo

printf "\n\n"
echo "The image has been created."
echo "Start running the image."
printf "\n\n"
docker run --name assignment -p 8000:8000/tcp -it -d qredo:latest

echo "Now the image is running in the background."
echo "You can get auth endpoint on ${GREEN}localhost:8000${NC}"
echo " "
echo "${RED}ATTENTION !!!${NC}"
echo "We have to create a real user, please create one."
docker exec -it assignment python manage.py createsuperuser
printf "\n\n"
echo "${BLUE}Thank You for cooperation.${NC} Now You can start working with the service."

echo "First, get your token to be authenticated, before you get sum endpoint:"
echo """${GREEN}curl --header \"Content-Type: application/json\" --request POST \
--data '{\"username\":\"admin\",\"password\":\"admin\"}' localhost:8000/auth${NC}"""

echo "Secondly, use your token and hit the sum endpoint:"
echo """${GREEN}curl localhost:8000/sum -i -H \"Authorization:Bearer x.y.z\" \
-H \"Accept: application/json\" --request POST -d '[1,2,\"ala\",[3,-3]]'${NC}"""