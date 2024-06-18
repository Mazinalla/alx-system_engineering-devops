# Ensure the WordPress directory exists with the correct permissions and ownership
file { '/var/www/html/wordpress':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
  require => Package['apache2'], # Ensure apache2 is installed before managing the directory
}

# Ensure Apache service is running
service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/var/www/html/wordpress'], # Restart Apache if the directory changes
}

# Ensure Apache package is installed
package { 'apache2':
  ensure => installed,
}
