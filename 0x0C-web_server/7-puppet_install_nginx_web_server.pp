# Installs and Configures Nginx server with Puppet Manifest

package { 'nginx':
  ensure => present,
}

file_path { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://medium.com/@abenapomaa permanent;',
}
file { '/var/www/html/index.html':
  content  => 'Hello World!',
}

service { 'nginx':
  ensure  => active,
  require => Package['nginx'],
}
