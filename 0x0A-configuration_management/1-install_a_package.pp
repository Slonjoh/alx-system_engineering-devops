# installs flask
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# installs Werkzeug
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
