#!/usr/bin/env python

from .config import Config

import json
import requests

def getDockerRegistry(version, *args, **kwargs):

  if( version == 2 ):
    return DockerRegistryV2(*args, **kwargs)

class DockerRegistryV2(object):

  def __init__(self, host=None, port=None):
    if( host is None ):
      self.host = Config.DEFAULT_DOCKER_REGISTRY_HOST
    else:
      self.host = host

    if( port is None ):
      self.port = Config.DEFAULT_DOCKER_REGISTRY_PORT
    else:
      self.port = port

    self.version = 2

    if( not self.testConnection() ):
      raise Exception('Unable to connect to %s' % '{URI}')

  def getUrl(self):
    return 'http://%s:%s/v%d' % (self.host, self.port, self.version)

  def __remoteRequest__(self, uri, method='GET', data=None):
    """Connects to the Docker Registry to perform a request.
    Inputs:
      uri: (str) Resource location for the request
      method: (str) Method to perform at URI locaiton
      data: (dict) Dictionary of data to send in the request
    Returns:
      dict: Dictionary of response data
    """
    request = requests.get('%s/%s' % (self.getUrl(), uri))
    return json.loads(request.text)

  def testConnection(self):
    """Tests connection to the Docker Registry
    Returns:
      boolean: True if connects, False if cannot connect
    """
    if( self.__remoteRequest__('') == {} ):
      return True
    return False

  def getRepositories(self):
    """  """
    return self.__remoteRequest__('_catalog')['repositories']

  def getRepositoryTags(self, repository):
    """  """
    return self.__remoteRequest__('%s/tags/list' % repository)['tags']

  def getRepositoryMetadata(self, repository, tag):
    """  """
    return self.__remoteRequest__('%s/manifests/%s' % (repository, tag))
