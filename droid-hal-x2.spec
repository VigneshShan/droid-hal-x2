# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device x2
%define vendor leeco

%define vendor_pretty LeEco
%define device_pretty Le Max2

%define installable_zip 1
%define droid_target_aarch64 1
%define android_config \
#define WANT_ADRENO_QUIRKS 1 \
#define QCOM_BSP 1 \
%{nil}

%define straggler_files \
   /init.qcom.bt.sh\
   /file_contexts.bin\
   /bugreports\
   /d\
   /init.qcom.sh\
   /init.qcom.usb.sh\
   /property_contexts\
   /qfp_boot.sh\
   /sdcard\
   /selinux_version\
   /service_contexts\
   /vendor\
   %{nil}

%define additional_post_scripts \
/usr/bin/groupadd-user media_rw || :\
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

