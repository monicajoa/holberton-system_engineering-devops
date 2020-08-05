# Client configuration file (w/ Puppet)
# Configuring a client's SSH configuration file to be ...
# able to connect to a server without entering a password

file_line { 'Identity_file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'Aasswordless_authentication':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}
