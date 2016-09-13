#!/usr/bin/env python

class Config(object):
  CONFIG_FILES=['/etc/docker-registry.ini', '~/.docker-registry.ini']
  DEFAULT_DOCKER_REGISTRY_PORT = 5000
  DEFAULT_DOCKER_REGISTRY_HOST = 'localhost'
  DEFAULT_DOCKER_REGISTRY_URI_BASE = ''
  DEFAULT_DOCKER_REGISTRY_VERSION = 2
  DEFAULT_OUTPUT_FORMAT = 'simple'
