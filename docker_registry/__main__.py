#!/usr/bin/env python

from . import registry
from .config import Config
from tabulate import tabulate

import argparse
import sys

class ArgumentParser(object):
  def __init__(self):
    # Global arguments
    self.global_parser = argparse.ArgumentParser(add_help=False)
    
    # Master/Parent parsers
    self.master_parser = argparse.ArgumentParser(description='Interact with a Docker Registry')
    self.master_parser.add_argument('--host', '-H', dest='host', default=None, help='Host of Docker Registry')
    self.master_parser.add_argument('--port', '-P', dest='port', default=None, help='Port of Docker Registry')
    self.master_parser.add_argument('--registry-version', '-V', dest='registry_version', default=None, help='Docker Registry API version')
    self.master_parser.add_argument('--config-file', '-c', dest='config_file', default='~/.docker-registry.ini')

    # Sub-command Processors
    self.command_parsers = self.master_parser.add_subparsers(title='command', dest='command')
    self.command_parsers.required = True
    self.command_list_parser = self.command_parsers.add_parser('ls', parents=[self.global_parser])

    # Command 'list' arguments
    #self.command_ls_parser.add_argument()

  def parse(self, args=None):
    #return self.parsed_args
    return self.master_parser.parse_args()

def main(argv=None):
  """Main executable function for Docker Registry CLi tool"""
  if( argv is None ):
    argv = sys.argv[1:]

  parser = ArgumentParser()
  parsed_args = parser.parse()

  docker_registry = registry.getDockerRegistry(parsed_args.registry_version, host=parsed_args.host, port=parsed_args.port)
  print tabulate(docker_registry.getRepositories(), headers=['Repositories'], tablefmt=Config.DEFAULT_OUTPUT_FORMAT)

if( __name__ == '__main__' ):
  main()
