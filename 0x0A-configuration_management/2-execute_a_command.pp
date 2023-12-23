# Define the exec resource to kill the process named "killmenow"
exec { 'kill_killmenow_process':
  command     => 'pkill killmenow',
  refreshonly => true, # Only run when notified by another resource
  subscribe   => Exec['notify_killmenow_process'], # Subscribe to a notification
}

# Notify the exec resource to trigger its execution
exec { 'notify_killmenow_process':
  command => '/bin/true',
  notify  => Exec['kill_killmenow_process'],
}
