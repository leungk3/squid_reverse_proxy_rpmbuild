#
# Spec file for mod_qos 11.4
#
Summary:  mod_qos Apache Quality of Service module
Name: mod_qos
Version: 11.4
Release: 1%{?dist}
License: GPL
Group: Networking
Source: http://downloads.sourceforge.net/project/mod-qos/mod_qos-11.4.tar.gz
URL: http://opensource.adnovum.ch/mod_qos/
Distribution: CentOS 6.5
Vendor: SRI
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Packager: Kogee Leung <kleung@sri.utoronto.ca>
Requires: openssl >= 1.0.1e

%description

%prep
rm -rf $RPM_BUILD_DIR/mod_qos-11.4
tar zxfp $RPM_SOURCE_DIR/mod_qos-11.4.tar.gz
cd $RPM_BUILD_DIR/mod_qos-11.4/apache2
/usr/lib64/apr-1/build/libtool --silent --mode=compile gcc -prefer-pic -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -m64 -mtune=generic -Wformat-security -fno-strict-aliasing  -DLINUX=2 -D_REENTRANT -D_GNU_SOURCE -pthread -I/usr/include/httpd  -I/usr/include/apr-1   -I/usr/include/apr-1   -c -o mod_qos.lo mod_qos.c && touch mod_qos.slo
/usr/lib64/apr-1/build/libtool --silent --mode=link gcc -o mod_qos.la  -rpath /usr/lib64/httpd/modules -module -avoid-version mod_qos.lo

%install
mkdir -p %{buildroot}/usr/lib64/httpd/modules

/usr/lib64/apr-1/build/libtool --mode=install cp $RPM_BUILD_DIR/mod_qos-11.4/apache2/mod_qos.la %{buildroot}/usr/lib64/httpd/modules/

cp $RPM_BUILD_DIR/mod_qos-11.4/apache2/.libs/mod_qos.so %{buildroot}/usr/lib64/httpd/modules/mod_qos.so

#%post

%postun
rm /usr/lib64/httpd/modules/mod_qos.so /usr/lib64/httpd/modules/mod_qos.la 

%files
%defattr(-,root,root)
/usr/lib64/httpd/modules/
