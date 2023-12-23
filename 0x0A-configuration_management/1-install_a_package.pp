#!/usr/bin/pup
# Define the package resource for Flask
package { 'flask':
  ensure => '2.1.0',  # Specify the desired version
  provider => 'pip3', # Use pip3 as the provider for Python 3
}
