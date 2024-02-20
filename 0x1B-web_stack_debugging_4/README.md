	web stACK DEBUGGING
root@94091d11a274:/# su - holberton
-su: /etc/profile: Too many open files
-su: /home/holberton/.bash_profile: Too many open files
-su-4.3$
-su-4.3$ ls
-su: start_pipeline: pgrp pipe: Too many open files
-su-4.3$ exit
logout
-su: /home/holberton/.bash_logout: Too many open files
-su: /etc/bash.bash_logout: Too many open files

------- after fixing the error --------------------
root@94091d11a274:/# sudo vi /etc/security/limits.conf
root@94091d11a274:/# sudo sysctl -p
root@94091d11a274:/# su - holberton
holberton@94091d11a274:~$ ls
holberton@94091d11a274:~$ ls /
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr
holberton@94091d11a274:~$
The issue was the number of file the user holberton was allowed to open as you notice from my terminal i opened the file /etc/security/limits.conf to increase the size and that was how i was able to solve it. Never forget debugging starts from the error gotten_

Cheers.
