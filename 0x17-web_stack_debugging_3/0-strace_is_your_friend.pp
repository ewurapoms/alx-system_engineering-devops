# Fixes bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`

file {'/var/www/html/wp-includes/class-wp-locale.phpp':
  ensure => file,
  source => '/var/www/html/wp-includes/class-wp-locale.php',
  before => File['/var/www/html/wp-includes/class-wp-locale.php']
}

file {'/var/www/html/wp-includes/class-wp-locale.php':
  ensure => absent
}
