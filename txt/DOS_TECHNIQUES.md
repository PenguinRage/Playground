MS-DOS definitions & commands
=============================

Basic information on the tools available on CMD for all Windows machines.

Command Summaries:
------------------

### Select single command - Summarised with options

```DOS
command name /?

```

### All commands - Summarised

```DOS
help -- summarises all command names
```

### Assigning attributes to files & folders

```DOS
attrib [+R : -R] [+A : -A] [+S:-S] [+H : -H] [+I : -I] [drive:][path][filename] [/S [/D] [/L]]

```

##### Options:

```
+R -- Use the +R option to make a file read-only. Read-only files may be read but they can`t be changed or deleted.
-R -- Use the -R option to change the file protection attribute back to normal (so it can be read, changed, or deleted).
+A -- Use the +A option to set the ARCHIVE attribute of a file. When the +A option is used, this flags the file as available for archiving when using the BACKUP or XCOPY commands.
-A -- Use the -A option to turn off the ARCHIVE attribute.
+H -- Set the HIDDEN attribute of a file so that it will not appear in a directory listing.
-H -- Use the -H option to turn off the HIDDEN attribute.
+S -- Flags the file as a command file used only by DOS. The file will not appear in a directory listing. This attribute is generally reserved for programmers.
-S -- Use the -S option to turn off the SYSTEM attribute.
/S -- Use the /S switch to set attributes on subdirectories found within the specified path.
```

### Process Management

#### List active processes

```DOS
  tasklist
```

#### Kill active processes

```DOS
  taskkill

```

### Disk Management

#### Disk Defragmentation

```DOS
defrag <volume>
```

#### Clean out temporary files from Disk Drives

```DOS
cleanmgr
```

#### Check Disk for errors

```
CHKDSK [volume[[path]filename]]] [/F] [/V] [/R] [/X] [/I] [/C] [/L[:size]] [/B]
```

##### Options:

```
volume -- Specifies the drive letter (followed by a colon), mount point, or volume name.
filename -- FAT/FAT32 only: Specifies the files to check for fragmentation.
/F -- Fixes errors on the disk.
/V -- On FAT/FAT32: Displays the full path and name of every file on the disk.
On NTFS: Displays cleanup messages if any.
/R -- Locates bad sectors and recovers readable information (implies /F).
/L:size -- NTFS only:  Changes the log file size to the specified number of kilobytes.  
If size is not specified, displays current size.
/X -- Forces the volume to dismount first if necessary.
/I -- NTFS only: Performs a less vigorous check of index entries.
/C -- NTFS only: Skips checking of cycles within the folder structure.
/B -- NTFS only: Re-evaluates bad clusters on the volume (implies /R)
```

#### Diskpart - Microsoft Partitioning Tool

```
diskpart
```

### System Information

```
systeminfo | more
```

#### Listing available servers

```
net view
```

#### Gather information on server - remote access

```
systeminfo /S server_name
```

#### Performance Monitor

```
perfmon
```

#### File Checker - for corrupted or missing files

```
sfc /SCANNOW
```

#### Driver Information

```
driverquery | more
```

### Monitoring Active Internet Services

```
netstat [-a] [-n] [-b]
-a -- Displays all connections and listening ports
-n -- Displays addresses and port numbers in numerical form
-b -- Displays the executable involved in each connection (note: also provides PID)

```

#### Windows IP Configuration

```
ipconfig
/renew -- Renew the IPv4 address for the specified adaptor
/flushdns -- Purges the DNS Resolver cache
```

#### Ping & Tracing route from Destination to Local Machine

```
ping url
tracert url
```

### Network Services

```
netsh
```

#### Changing IP Address

```
netsh interface ip set address name=”Local Area Connection” static 192.168.0.1 255.255.255.0 192.168.0.254
```

This assumes the following:

-	The name of the interface you want to change the IP address for is Local Area Network

-	You want to statically assign an IP address of 192.168.0.1

-	You want to set a subnet mask of 255.255.255.0

-	You want to set a default gateway of 192.168.0.254

#### Changing DNS Address

```
netsh interface ip set dns name=”Local Area Connection” static 192.168.0.250
```

This assumes the following:

-	The name of the interface you want to change the primary DNS setting for is Local Area Network

-	The IP address of the DNS Server is 192.168.0.250

##### Change IP address of the secondary DNS server

Note: Google public DNS servers: 8.8.8.8

```
netsh interface ip add dns name=”Local Area Connection” 8.8.8.8 index=2
```

##### Set DNS Servers to assign Dynamically

```
netsh interface ip set dnsservers name=”Local Area Connection” source=dhcp
```

### Windows Registery

#### List of Operations

```
REG QUERY [ROOT\]RegKey /v ValueName [/s]
REG QUERY [ROOT\]RegKey /ve --This returns the (default) value

REG ADD [ROOT\]RegKey /v ValueName [/t DataType] [/S Separator] [/d Data] [/f]
REG ADD [ROOT\]RegKey /ve [/d Data] [/f] -- Set the (default) value

REG DELETE [ROOT\]RegKey /v ValueName [/f]
REG DELETE [ROOT\]RegKey /ve [/f] -- Remove the (default) value
REG DELETE [ROOT\]RegKey /va [/f] -- Delete all values under this key

REG COPY \[\\SourceMachine\][ROOT\]RegKey \[\\DestMachine\][ROOT\]RegKey

REG EXPORT [ROOT\]RegKey FileName.reg
REG IMPORT FileName.reg
REG SAVE [ROOT\]RegKey FileName.hiv
REG RESTORE \\MachineName\[ROOT]\KeyName FileName.hiv

REG LOAD KeyName FileName
REG UNLOAD KeyName

REG COMPARE [ROOT\]RegKey [ROOT\]RegKey [/v ValueName] [Output] [/s]
REG COMPARE [ROOT\]RegKey [ROOT\]RegKey [/ve] [Output] [/s]
```

##### Key:

```
   ROOT :
         HKLM = HKey_Local_machine (default)
         HKCU = HKey_current_user
         HKU  = HKey_users
         HKCR = HKey_classes_root

   ValueName : The value, under the selected RegKey, to edit.
               (default is all keys and values)

   /d Data   : The actual data to store as a "String", integer etc

   /f        : Force an update without prompting "Value exists, overwrite Y/N"

   \\Machine : Name of remote machine - omitting defaults to current machine.
                Only HKLM and HKU are available on remote machines.

   FileName  : The filename to save or restore a registry hive.

   KeyName   : A key name to load a hive file into. (Creating a new key)

   /S        : Query all subkeys and values.

   /S Separator : Character to use as the separator in REG_MULTI_SZ values
                  the default is "\0"

   /t DataType  : REG_SZ (default) | REG_DWORD | REG_EXPAND_SZ | REG_MULTI_SZ

   /reg:32   : Force REG.exe to write to the 32-bit registry location
   /reg:64   : Force REG.exe to write to the 64-bit registry location

             By default a 32-bit process (such as an SCCM client or a 32 bit MSI installer)
             on a 64 bit machine, will use a 32-bit view of the registry: HKLM\SOFTWARE\Wow6432Node
             Use the /REG switch to over-ride this. See Q305097 for more details.

   Output    : /od (only differences) /os (only matches) /oa (all) /on (no output)
```
