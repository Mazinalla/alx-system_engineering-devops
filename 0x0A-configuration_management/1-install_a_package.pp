# Writing script using Puppet to install flask from pip3 

package { 'flask':
  ensure   => '2.3.0',
  provider => 'pip3',
}
