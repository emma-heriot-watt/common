# Changelog

All notable changes to this project will be documented in this file. See
[Conventional Commits](https://conventionalcommits.org) for commit guidelines.

## [1.8.0](https://github.com/emma-simbot/common/compare/v1.7.0...v1.8.0) (2022-12-13)


### Features

* **gunicorn:** add function to create a gunicorn server for the api app ([4ec1721](https://github.com/emma-simbot/common/commit/4ec1721d387120c27eff56eac140b748dc7411b4))

## [1.7.0](https://github.com/emma-simbot/common/compare/v1.6.0...v1.7.0) (2022-12-12)


### Features

* support getting secrets from AWS Secrets Manager ([#11](https://github.com/emma-simbot/common/issues/11)) ([f41df86](https://github.com/emma-simbot/common/commit/f41df8660c23359b697d2e19a6c06f43d8a6be8d))

## [1.6.0](https://github.com/emma-simbot/common/compare/v1.5.0...v1.6.0) (2022-12-12)


### Features

* improve logging and easily instrument APIs ([#10](https://github.com/emma-simbot/common/issues/10)) ([33dda8e](https://github.com/emma-simbot/common/commit/33dda8e4df16392cc2bd9b6f924d845668bc97f3))

## [1.5.0](https://github.com/emma-simbot/common/compare/v1.4.0...v1.5.0) (2022-12-01)


### Features

* **gunicorn:** add gunicorn-specific objects that are compatible with the logger ([#8](https://github.com/emma-simbot/common/issues/8)) ([e387f13](https://github.com/emma-simbot/common/commit/e387f135cf281673b82ee6db1eb05450b4543aa0))

## [1.4.0](https://github.com/emma-simbot/common/compare/v1.3.0...v1.4.0) (2022-10-30)


### Features

* **logging:** add new arg to enable/disable showing locals in rich tracebacks ([3c98aab](https://github.com/emma-simbot/common/commit/3c98aab67acd64b9f16a371beb918aa6d3dcddcd))


### Bug Fixes

* **logging:** handler cannot be None ([178c184](https://github.com/emma-simbot/common/commit/178c1841eeae7e120e4cfcd6bba3c47fab98b5f9))
* **logging:** make sure log level is uppercase ([692d226](https://github.com/emma-simbot/common/commit/692d22696e88bfd893f01bd187e6f9a8f00354d1))

## [1.3.0](https://github.com/emma-simbot/common/compare/v1.2.0...v1.3.0) (2022-10-20)


### Features

* add the loguru logger into the __init__ so everyone can use it ([5ddb7e3](https://github.com/emma-simbot/common/commit/5ddb7e34aefc9cd39505e0df26973bbbe1ecbb6e))

## [1.2.0](https://github.com/emma-simbot/common/compare/v1.1.0...v1.2.0) (2022-10-19)


### Features

* add `EmmaExtractedFeatures` datamodel so that it can be consistent across repos ([#3](https://github.com/emma-simbot/common/issues/3)) ([a4acb45](https://github.com/emma-simbot/common/commit/a4acb4561765604782e453a1e343683656b7a3d3))

## [1.1.0](https://github.com/emma-simbot/common/compare/v1.0.0...v1.1.0) (2022-10-14)


### Features

* setup loguru for logging ([#1](https://github.com/emma-simbot/common/issues/1)) ([41d29f8](https://github.com/emma-simbot/common/commit/41d29f896dbdc6f6ed1a224123ee3404d60e3f35))

## 1.0.0 (2022-10-14)


### Features

* setup the repository ([0d64d14](https://github.com/emma-simbot/common/commit/0d64d1476db8e3ef4481a072cdf736942dd43b31))
