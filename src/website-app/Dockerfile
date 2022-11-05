FROM node:16
WORKDIR /usr/src/app
COPY package.json ./
COPY yarn.lock ./
COPY .yarnrc.yml ./
COPY .yarn/releases ./.yarn/releases
RUN yarn set version berry
RUN yarn
COPY . ./
RUN yarn build

EXPOSE 3000
CMD ["node", "build"]