# User limit
# Using Puppet, set user limit
exec {'fix-user-limit':
  path    => '/bin/',
  command => 'sed -i s/holberton/foo/ /etc/security/limits.conf',
}
