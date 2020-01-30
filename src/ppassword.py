import argparse

def main():
  parser = argparse.ArgumentParser(description="ppassword - a secure and reliable password manager")
  parser.add_argument('init', help="Init a device, to store the private key on")
  arguments = parser.parse_args()
  print(arguments.init)