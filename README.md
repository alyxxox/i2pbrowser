# I2P Browser

## Dependencies
- Python3>=
- i2pd
- mullvad-browser
## Installation:
(proper installation method coming soon)
- Install mullvad-browser
  - on Arch:
  ```
  pacman -S mullvad-browser
  ```
  - on Debian:
  ```
  $ apt install mullvad-browser
  ```
  - on NixOS/using Nix package manager (Recommended):
  ```
  nix-env -iA nixpkgs.mullvad-browser
  ```
- Install i2pd
  - on Arch:
  ```
  pacman -S i2pd
  ```
  - on Debian:
  ```
  $ apt install i2pd
  ```
  - on NixOS/using Nix package manager (Recommended):
  ```
  nix-env -iA nixpkgs.i2pd
  ```
- Finally, move the python script to allow it to run
  ```
  mv i2p-browser.py /usr/local/bin/i2pbrowser
   ```
    - You could run it manually from anywhere if you wish using
    ```
    /path/to/i2p-browser.py
    ```
