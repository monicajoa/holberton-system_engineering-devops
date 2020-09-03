# Add a custom HTTP header with Puppet
# set up a new Ubuntu machine to automate the task of
# creating a custom HTTP header response, but with Puppet

exec { 'update':
  command  => '/usr/bin/sudo apt-get update',
}

package { 'nginx':
  ensure   => 'installed',
  name     => 'nginx',
  provider => 'apt',
}

file_line { 'add_header':
  path     => '/etc/nginx/sites-available/default',
  line     => 'add_header X-Served-By $HOSTNAME;',
  after    => 'server_name _;',
}

exec {'start':
  command  => '/usr/bin/sudo service nginx restart',
}
