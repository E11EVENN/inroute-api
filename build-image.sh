docker buildx build \
    --build-arg GIT_COMMIT="$(git rev-parse HEAD)" \
    --build-arg GIT_AUTHOR="$(git log -1 --pretty=format:'%an')" \
    --build-arg VERSION="$(git describe --tags --abbrev=0)" \
    --build-arg BUILD_DATE="$(date -u +'%Y-%m-%dT%H:%M:%S%z')" \
    -t inroute-api .