# Reference: dhd/droid-hal-device.inc

%define vendor xiaomi
%define device whyred

%define vendor_pretty Xiaomi
%define device_pretty Xiaomi Redmi Note 5 Pro

%define droid_target_aarch64 1
%define enable_kernel_update 1

%define android_config \
  #define WANT_ADRENO_QUIRKS 1 \
%{nil}

%define straggler_files \
  /bt_firmware \
  /dsp \
  /firmware \
  /persist \
%{nil}

%define makefstab_skip_entries /sys/fs/pstore

%include rpm/dhd/droid-hal-device.inc
