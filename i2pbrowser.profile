# Persistent local customizations

# Persistent global definitions
# added by included profile
#include globals.local
include i2p-browser.local
join-or-start i2p-browser

noblacklist ${HOME}/.mullvad
noblacklist ${HOME}/.i2pd
noblacklist ${HOME}/.nix-profile/bin/i2pd
noblacklist ${HOME}/.nix-profile/bin/mullvad-browser
noblacklist ${HOME}/.local/i2p-browser.py

mkdir ${HOME}/.local/i2p-browser.py
mkdir ${HOME}/.mullvad
mkdir ${HOME}/.i2pd
mkdir ${HOME}/.nix-profile/bin/

whitelist ${HOME}/.mullvad
whitelist ${HOME}/.i2pd
whitelist ${HOME}/.nix-profile/bin/i2pd
whitelist ${HOME}/.nix-profile/bin/mullvad-browser
whitelist ${HOME}/.local/i2p-browser.py

caps.drop all
ipc-namespace
#machine-id
netfilter
nodvd
nogroups
noinput
nonewprivs
noroot
notv
protocol unix,inet,netlink
seccomp !chroot

disable-mnt
private-tmp
dbus-system none
dbus-user none
