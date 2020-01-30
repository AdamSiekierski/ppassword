import platform
import psutil

def get_drives():
  all_drives = psutil.disk_partitions()
  drives = []

  for drive in all_drives:
    if (drive.fstype == 'msdos' or drive.fstype == 'fat32'):
      drives.append(drive)

  return drives
