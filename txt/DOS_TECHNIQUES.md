DOS definitions & commands
==========================

Command Summaries:
------------------

### Select single command - Summarised with options

```DOS
command name /?

```

### All commands - Summarised

```DOS
help - summarises all command names
```

### Assigning attributes to files & folders

```DOS
attrib [+R : -R] [+A : -A] [+S:-S] [+H : -H] [+I : -I] [drive:][path][filename] [/S [/D] [/L]]

```

##### Options:

```
+R - Use the +R option to make a file read-only. Read-only files may be read but they can`t be changed or deleted.

-R - Use the -R option to change the file protection attribute back to normal (so it can be read, changed, or deleted).

+A - Use the +A option to set the ARCHIVE attribute of a file. When the +A option is used, this flags the file as available for archiving when using the BACKUP or XCOPY commands.

-A - Use the -A option to turn off the ARCHIVE attribute.

+H - Set the HIDDEN attribute of a file so that it will not appear in a directory listing.

-H - Use the -H option to turn off the HIDDEN attribute.

+S - Flags the file as a command file used only by DOS. The file will not appear in a directory listing. This attribute is generally reserved for programmers.

-S - Use the -S option to turn off the SYSTEM attribute.

/S - Use the /S switch to set attributes on subdirectories found within the specified path.

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
volume - Specifies the drive letter (followed by a colon), mount point, or volume name.
filename - FAT/FAT32 only: Specifies the files to check for fragmentation.
/F - Fixes errors on the disk.
/V - On FAT/FAT32: Displays the full path and name of every file on the disk.
On NTFS: Displays cleanup messages if any.
/R - Locates bad sectors and recovers readable information (implies /F).
/L:size - NTFS only:  Changes the log file size to the specified number of kilobytes.  
If size is not specified, displays current size.
/X - Forces the volume to dismount first if necessary.
/I - NTFS only: Performs a less vigorous check of index entries.
/C - NTFS only: Skips checking of cycles within the folder structure.
/B - NTFS only: Re-evaluates bad clusters on the volume (implies /R)
```
