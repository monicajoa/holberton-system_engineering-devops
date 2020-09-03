# Install Nginx web server (w/ Puppet)
package { 'nginx':
  ensure   => 'latest',
  name     => 'nginx',
  provider => 'apt'
}

file { 'index':
  path    => '/var/www/html/index.html',
  mode    => '0644',
  content => 'Holberton School'
}

file_line { 'redirect_301':
  path  => '/etc/nginx/sites-available/default',
  line  => "\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}",
  after => '^server {',
}

service { 'nginx':
  ensure => running,
  enable => true
}
