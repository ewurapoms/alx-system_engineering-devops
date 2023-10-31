# Installs and Configures Nginx server with Puppet Manifest

package { 'nginx':
  listen_port => 80,
}
file { '/etc/nginx/sites-available/redirect_me':
  ensure => file,
}
nginx::resource::server { 'default':
  ensure   => present,
  location => [
    {
      location => '/',
      content  => 'Hello World!',
    },
    {
      location => '^/redirect_me$',
      rewrite  => "https://medium.com/@abenapomaa permanent;",
    },
  ],
  require  => File['/etc/nginx/sites-available/redirect_me'],
}
