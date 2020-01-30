import platform

def get_drives_mac():
  return 'hey, mac user'

def get_drives():
  systems = {
    "Darwin": get_drives_mac,
  }
  return systems.get(platform.system(), lambda:'Your operating system is not yet supported')()