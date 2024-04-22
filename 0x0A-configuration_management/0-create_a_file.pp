# This Puppet script creates a file in /tmp with specific permissions, owner, group, and content.

# Define a file resource named '/tmp/school'
file { '/tmp/school':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
