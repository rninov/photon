Summary:        library for fast, message-based applications
Name:           zeromq
Version:        4.3.4
Release:        1%{?dist}
URL:            http://www.zeromq.org
License:        LGPLv3+
Group:          System Environment/Libraries
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        https://github.com/zeromq/libzmq/releases/download/v4.3.4/%{name}-%{version}.tar.gz
%define sha1 zeromq=47277a64749049123d1401600e8cfbab10a3ae28


Requires:       libstdc++

%description
The 0MQ lightweight messaging kernel is a library which extends the standard
socket interfaces with features traditionally provided by specialised messaging
middleware products. 0MQ sockets provide an abstraction of asynchronous message
queues, multiple messaging patterns, message filtering (subscriptions), seamless
access to multiple transport protocols and more.

%package    devel
Summary:    Header and development files for zeromq
Requires:   %{name} = %{version}
%description    devel
It contains the libraries and header files to create applications

%prep
%autosetup

%build
sh configure \
    --prefix=%{_prefix} \
    --with-libsodium=no \
    --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
find %{buildroot}%{_libdir} -name '*.la' -delete

%check
make check

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING COPYING.LESSER NEWS
%{_bindir}/
%{_libdir}/libzmq.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libzmq.so
%{_libdir}/pkgconfig/libzmq.pc
%{_includedir}/
%{_mandir}/*

%changelog
*   Sat Jun 12 2021 Siju Maliakkal <smaliakkal@vmware.com> 4.3.4-1
-   Upgrading to Fix CVE-2021-20236
*   Fri Apr 16 2021 Satya Naga Vasamsetty<svasamsetty@vmware.com> 4.2.3-5
-   Fix CVE-2021-20235
*   Thu Sep 03 2020 Shreenidhi Shedi <sshedi@vmware.com> 4.2.3-4
-   Fix CVE-2020-15166
*   Wed Aug 07 2019 Siju Maliakkal <smaliakkal@vmwre.com> 4.2.3-3
-   Apply patch for CVE-2019-6250
*   Mon Jul 22 2019 Siju Maliakkal <smaliakkal@vmware.com> 4.2.3-2
-   Apply patch for CVE-2019-13132
*   Thu Sep 13 2018 Siju Maliakkal <smaliakkal@vmware.com> 4.2.3-1
-   Updated to latest version
*   Fri Sep 15 2017 Bo Gan <ganb@vmware.com> 4.1.4-3
-   Remove devpts mount
*   Mon Aug 07 2017 Chang Lee <changlee@vmware.com> 4.1.4-2
-   Fixed %check
*   Thu Apr 13 2017 Dheeraj Shetty <dheerajs@vmware.com> 4.1.4-1
-   Initial build. First version
