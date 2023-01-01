# Changelog

All notable changes to this project will be documented in this file. See
[Conventional Commits](https://conventionalcommits.org) for commit guidelines.

## [1.14.0](https://github.com/emma-simbot/common/compare/v1.13.2...v1.14.0) (2023-01-01)


### Features

* **telemetry:** setup metrics exporting for the API ([84ae862](https://github.com/emma-simbot/common/commit/84ae86255cfc6229f9a53b150d00a610f58ed505))

## [1.13.2](https://github.com/emma-simbot/common/compare/v1.13.1...v1.13.2) (2022-12-23)


### Bug Fixes

* explicitly do not install otel instrumentation v0.36b0 ([86d5ecf](https://github.com/emma-simbot/common/commit/86d5ecf6ce739e5c403990f48318e6b02215e058))
* set the worker timeout to 60 secs ([5a7b1cf](https://github.com/emma-simbot/common/commit/5a7b1cf4a3048fdb9997fcdad2b1822cef52840c))

## [1.13.1](https://github.com/emma-simbot/common/compare/v1.13.0...v1.13.1) (2022-12-19)


### Bug Fixes

* install all deps with fastapi ([e0ebbba](https://github.com/emma-simbot/common/commit/e0ebbbaa93e3120aed4fe66154431dd0cb974c05))

## [1.13.0](https://github.com/emma-simbot/common/compare/v1.12.2...v1.13.0) (2022-12-17)


### Features

* cleanup and add some more helper functions ([08da822](https://github.com/emma-simbot/common/commit/08da8229e47a2350be68f4267f41752323e04ff6))


### Bug Fixes

* add httpx as a dep ([9fc0f97](https://github.com/emma-simbot/common/commit/9fc0f97a8d9fc866cce9944f0500fcbcce5c1abb))
* lint errors ([d36a34e](https://github.com/emma-simbot/common/commit/d36a34e6f288f57b4e37963951b992dcc242193c))

## [1.12.2](https://github.com/emma-simbot/common/compare/v1.12.1...v1.12.2) (2022-12-17)


### Bug Fixes

* **deps:** move all api and aws deps to the main group ([051b83e](https://github.com/emma-simbot/common/commit/051b83ebc8ebe3b40d5bd568081198d629f4a2ec))

## [1.12.1](https://github.com/emma-simbot/common/compare/v1.12.0...v1.12.1) (2022-12-16)


### Bug Fixes

* **deps:** allow torch from 1.10.0 ([1864d3c](https://github.com/emma-simbot/common/commit/1864d3ca4af7f407e195df229fbafc7a6dd72d83))
* **deps:** unconstrain torch version but prevent 1.13.0 ([ebaaa4a](https://github.com/emma-simbot/common/commit/ebaaa4a1f4bbcb83de2b664bc6f67d8f4dc01691))

## [1.12.0](https://github.com/emma-simbot/common/compare/v1.11.0...v1.12.0) (2022-12-14)


### Features

* **cloudwatch logger:** add option to enable trace logging to cloudwatch logs ([3f03571](https://github.com/emma-simbot/common/commit/3f0357131a0535492b3bb2934297b0df0a5d5d42))

## [1.11.0](https://github.com/emma-simbot/common/compare/v1.10.0...v1.11.0) (2022-12-14)


### Features

* **logging:** improve typing for `setup_logging` function ([58fc214](https://github.com/emma-simbot/common/commit/58fc214899aea37a7dedc2b08b3252868f074ffd))


### Bug Fixes

* **logging:** allow any handler to be the `root_handler` ([2d74796](https://github.com/emma-simbot/common/commit/2d74796b2b3555338fddb66ae96e3cdeff9a42be))

## [1.10.0](https://github.com/emma-simbot/common/compare/v1.9.0...v1.10.0) (2022-12-14)


### Features

* **deps:** make `api` and `aws` group optional ([e36bb3e](https://github.com/emma-simbot/common/commit/e36bb3ebfa757aeb6ed5368ba34ae8fbc89c9074))
* **logging:** create InterceptHandler for instrumented logging ([7671966](https://github.com/emma-simbot/common/commit/7671966e9700a784dad93b5c0f6588bf2d4e434b))

## [1.9.0](https://github.com/emma-simbot/common/compare/v1.8.0...v1.9.0) (2022-12-13)


### Features

* **logging:** add `PropogateHandler` to automatically send to the default logging module ([b20b48a](https://github.com/emma-simbot/common/commit/b20b48a807261cc968f74e3ef11f9b9e3e3ee8c2))

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
