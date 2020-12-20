# Scripts

Collection of scripts for accomplishing different tasks

## set_up_imaged_pi.sh 

Sets up the boot directory [of a microsd card imaged
with raspbian] to run in headless mode on the specified wifi network. Only one
argument must be passed: the SSID.

```sh
set_up_imaged_pi.sh WIFISSID [PASSWORD] [PATHTOBOOT]
```

PATHTOBOOT defaults to `/Volumes/boot` which is meaningless if you're not on a
mac. Requires a password be specified if changing PATHTOBOOT just because I don't know enough about command line arguments in bash.
