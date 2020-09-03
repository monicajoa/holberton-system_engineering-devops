# Add a custom HTTP header with Puppet
# set up a new Ubuntu machine to automate the task of
# creating a custom HTTP header response, but with Puppet

exec { 'update':
  command => 'apt-get update'
}

package { 'nginx':
  name    => 'nginx',
  ensure  => 'installed'
}

file_line { 'add_header':
  path    => '/etc/nginx/sites-available/default',
  line    => 'a add_header X-Served-By $HOSTNAME;',
  after   => 'server_name _'
}

exec {'start':
  command => 'service nginx start'
}
