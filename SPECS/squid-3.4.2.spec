#
# Spec file for Squid 3.4.2
#
Summary: Squid built as a reverse proxy
Name: squid
Version: 3.4.2
Release: 1%{?dist}
License: GPL
Group: Networking
Source: www.squid-cache.org/Versions/v4/3.4/squid-3.4.2.tar.bz2 
URL: http://www.squid-cache.org
Distribution: CentOS 6.5
Vendor: SRI
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Packager: Kogee Leung <kleung@sri.utoronto.ca>

%description
Squid is a caching proxy for the Web supporting HTTP, HTTPS, FTP, and more. It reduces bandwidth and improves response times by caching and reusing frequently-requested web pages. Squid has extensive access controls and makes a great server accelerator. It runs on most available operating systems, including Windows and is licensed under the GNU GPL

%prep
rm -rf $RPM_BUILD_DIR/squid-3.4.2
tar jxfp $RPM_SOURCE_DIR/squid-3.4.2.tar.bz2
%setup -T -D

%build
#%configure
./configure --build=x86_64-redhat-linux-gnu \
            --host=x86_64-redhat-linux-gnu \
            --target=x86_64-redhat-linux-gnu \
--prefix=/usr --bindir=/usr/bin --sbindir=/usr/sbin --sysconfdir=/etc/squid --datadir=/usr/share/squid --libdir=/usr/lib --libexecdir=/usr/libexec --localstatedir=/var --sharedstatedir=/var/lib --mandir=/usr/share/man --infodir=/usr/share/info --program-suffix=-3.4.2 --enable-async-io --with-pthreads --enable-storeio=ufs,aufs,diskd --enable-linux-netfilter --enable-arp-acl --enable-epoll --enable-removal-policies=lru,heap --enable-snmp --enable-delay-pools --enable-htcp --enable-cache-digests --enable-underscores --enable-referer-log --enable-useragent-log --enable-auth --enable-auth-basic=PAM,NCSA,LDAP --enable-auth-ntlm --enable-auth-digest --enable-carp --with-large-files --disable-internal-dns --enable-ssl --enable-ltdl-convenience

make

%install
make DESTDIR=%{buildroot} install

%post
ln -s %{_sbindir}/%{name}-%{version} %{_sbindir}/%{name}
%{_sbindir}/%{name} -z
touch %{_localstatedir}/logs/access.log
touch %{_localstatedir}/logs/cache.log
chown nobody:nobody %{_localstatedir}/logs/access.log
chown nobody:nobody %{_localstatedir}/logs/cache.log

%postun
rm %{_sbindir}/%{name}

%files
%defattr(-,root,root)

%config(noreplace) %{_sysconfdir}/%{name}/*.conf
%config(noreplace) %{_sysconfdir}/%{name}/*.css
%config %{_sysconfdir}/%{name}/*.default
%config %{_sysconfdir}/%{name}/*.documented
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/%{name}/*
%{_mandir}/man1/*
%{_mandir}/man8/*
%{_prefix}/lib/debug/*
%{_libexecdir}/*
%{_prefix}/src/debug/%{name}-%{version}/*
%dir %_localstatedir/cache/squid
%dir %_localstatedir/run/squid
%dir %_localstatedir/logs
