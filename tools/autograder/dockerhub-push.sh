VERSION="datasciencecourse-test"

docker build . --tag "gauravmm/$VERSION"
docker push "gauravmm/$VERSION"
