# Install Nginx web server (w/ Puppet)

package {'nginx':
  ensure   => 'latest',
  name     => 'nginx',
  provider => 'apt'
}

file {'index':
  path    => '/var/www/html/index.nginx-debian.html',
  mode    => '0644',
  content => 'Holberton School'
}

file_line { '301 Moved Permanently':
  path  => '/etc/nginx/sites-available/default',
  line  => '\trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  after => '^server {'
}

service { 'nginx':
  ensure => running,
  enable => true
}
