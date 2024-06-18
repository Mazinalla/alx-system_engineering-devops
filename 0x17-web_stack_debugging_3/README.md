# Puppet Configuration for Fixing Apache 500 Internal Server Error

## Overview

This project contains a Puppet manifest to diagnose and fix a 500 Internal Server Error returned by the Apache web server. The manifest ensures proper permissions and ownership of the necessary directories and files to prevent such errors.

## Files

- `0-strace_is_your_friend.pp`: Puppet manifest file that fixes common permission issues causing Apache to return a 500 error.

## Prerequisites

- Puppet installed on your server
- Apache web server installed on your server
- Access to the server where Apache is running

## Usage

### Step 1: Diagnose the Issue

1. Open `tmux` to split the terminal into multiple panes:

   ```bash
   tmux
   ```

2. In the first pane, find the Apache process ID (PID):

   ```bash
   pgrep -f apache2
   ```

3. Attach `strace` to the Apache process:

   ```bash
   strace -f -p <PID> -o /tmp/strace.log
   ```

4. In the second pane, make a request to the Apache server:

   ```bash
   curl -sI 127.0.0.1
   ```

5. Check the `strace` log for errors:

   ```bash
   less /tmp/strace.log
   ```

### Step 2: Apply the Puppet Manifest

1. Create the Puppet manifest file (`0-strace_is_your_friend.pp`) with the following content:

   ```puppet
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
   ```

2. Apply the Puppet manifest:

   ```bash
   puppet apply 0-strace_is_your_friend.pp
   ```

### Step 3: Verify the Fix

1. Restart Apache (if needed):

   ```bash
   systemctl restart apache2
   ```

2. Make a request to verify the server response:

   ```bash
   curl -sI 127.0.0.1
   ```

   You should receive a `200 OK` response if the issue is fixed.

## Contributing

If you encounter any issues or have suggestions for improvement, please feel free to create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This README provides clear instructions for diagnosing and fixing the Apache 500 error using Puppet. Feel free to adjust any section to better suit your specific setup or requirements.
