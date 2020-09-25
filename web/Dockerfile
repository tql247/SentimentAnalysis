FROM node:12.16.1-slim

# create destination directory
RUN mkdir -p /usr/src/nuxt-app
WORKDIR /usr/src/nuxt-app

# copy the app, note .dockerignore
COPY . /usr/src/nuxt-app/
RUN yarn install

# set app serving to permissive / assigned
ENV NUXT_HOST=0.0.0.0

# set app port
ENV NUXT_PORT=3000

# build necessary, even if no static files are needed,
# since it builds the server as well
RUN yarn build

EXPOSE $NUXT_PORT
# start the app
CMD [ "yarn", "start" ]