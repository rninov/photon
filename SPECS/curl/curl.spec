Summary:        An URL retrieval utility and library
Name:           curl
Version:        7.77.0
Release:        1%{?dist}
License:        MIT
URL:            http://curl.haxx.se
Group:          System Environment/NetworkingLibraries
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        http://curl.haxx.se/download/%{name}-%{version}.tar.gz
%define sha1    curl=fdbb773251bba86ff95a3fe51f9969fd5004bdde
BuildRequires:  ca-certificates
BuildRequires:  openssl-devel
BuildRequires:  krb5-devel
BuildRequires:  libssh2-devel
BuildRequires:  libmetalink-devel
Requires:       ca-certificates
Requires:       openssl
Requires:       krb5
Requires:       libssh2
Requires:       libmetalink
Requires:       curl-libs = %{version}-%{release}

%description
The cURL package contains an utility and a library used for
transferring files with URL syntax to any of the following
protocols: FTP, FTPS, HTTP, HTTPS, SCP, SFTP, TFTP, TELNET,
DICT, LDAP, LDAPS and FILE. Its ability to both download and
upload files can be incorporated into other programs to support
functions like streaming media.

%package        devel
Summary:        Libraries and header files for curl
Requires:       %{name} = %{version}-%{release}
%description    devel
Static libraries and header files for the support library for curl

%package        libs
Summary:        Libraries for curl
Group:          System Environment/Libraries
Requires:       ca-certificates-pki
%description    libs
This package contains minimal set of shared curl libraries.

%prep
%setup -q

%build
%configure \
    CFLAGS="%{optflags}" \
    CXXFLAGS="%{optflags}" \
    --disable-static \
    --enable-threaded-resolver \
    --with-ssl \
    --with-gssapi \
    --with-libssh2 \
    --with-ca-bundle=/etc/pki/tls/certs/ca-bundle.crt \
    --with-libmetalink
make %{?_smp_mflags}

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make DESTDIR=%{buildroot} install
install -v -d -m755 %{buildroot}/%{_docdir}/%{name}-%{version}
find %{buildroot}/%{_libdir} -name '*.la' -delete
%{_fixperms} %{buildroot}/*

%check
make %{?_smp_mflags} check

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_mandir}/man3/*
%{_datarootdir}/aclocal/libcurl.m4
%{_docdir}/%{name}-%{version}

%files libs
%{_libdir}/libcurl.so.*

%changelog
*   Mon Jun 28 2021 Nitesh Kumar <kunitesh@vmware.com> 7.77.0-1
-   Upgrade to 7.77.0, Fix for CVE-2021-22897
*   Mon Apr 12 2021 Gerrit Photon <photon-checkins@vmware.com> 7.76.1-1
-   Automatic Version Bump
*   Wed Jan 13 2021 Siju Maliakkal <smaliakkal@vmware.com> 7.74.0-1
-   Upgrade to 7.74.0
*   Mon Dec 07 2020 Dweep Advani <dadvani@vmware.com> 7.72.0-3
-   Patched for  CVE-2020-8284, CVE-2020-8285 and CVE-2020-8286
*   Tue Sep 29 2020 Satya Naga Vasamsetty <svasamsetty@vmware.com> 7.72.0-2
-   openssl 1.1.1
*   Tue Jul 14 2020 Gerrit Photon <photon-checkins@vmware.com> 7.72.0-1
-   Automatic Version Bump
*   Wed Jun 17 2020 Ankit Jain <ankitja@vmware.com> 7.61.1-5
-   Fix for CVE-2020-8177
*   Thu Jun 04 2020 Tapas Kundu <tkundu@vmware.com> 7.61.1-4
-   Build with libmetalink support
*   Tue Sep 24 2019 Dweep Advani <dadvani@vmware.com> 7.61.1-3
-   Fix CVEs CVE-2018-16890, CVE-2019-{3822/3823/5436/5481/5482}
*   Tue Jan 08 2019 Dweep Advani <dadvani@vmware.com> 7.61.1-2
-   Fix of CVE-2018-16839, CVE-2018-16840 and CVE-2018-16842
*   Mon Sep 10 2018 Ajay Kaher <akaher@vmware.com> 7.61.1-1
-   Upgraded to version 7.61.1
*   Wed Apr 04 2018 Dheeraj Shetty <dheerajs@vmware.com> 7.59.0-1
-   Update to version 7.59.0
*   Thu Feb 08 2018 Xiaolin Li <xiaolinl@vmware.com> 7.58.0-1
-   Fix CVE-2017-8817.
*   Thu Dec 21 2017 Xiaolin Li <xiaolinl@vmware.com> 7.56.1-2
-   Fix CVE-2017-8818.
*   Wed Dec 13 2017 Xiaolin Li <xiaolinl@vmware.com> 7.56.1-1
-   Update to version 7.56.1
*   Mon Nov 27 2017 Xiaolin Li <xiaolinl@vmware.com> 7.54.1-4
-   Fix CVE-2017-1000257
*   Mon Nov 06 2017 Xiaolin Li <xiaolinl@vmware.com> 7.54.1-3
-   Fix CVE-2017-1000254
*   Thu Nov 02 2017 Xiaolin Li <xiaolinl@vmware.com> 7.54.1-2
-   Fix CVE-2017-1000099, CVE-2017-1000100, CVE-2017-1000101
*   Tue Jul 11 2017 Divya Thaluru <dthaluru@vmware.com> 7.54.1-1
-   Update to 7.54.1
*   Mon Apr 24 2017 Bo Gan <ganb@vmware.com> 7.54.0-1
-   Update to 7.54.0
*   Fri Apr 14 2017 Alexey Makhalov <amakhalov@vmware.com> 7.51.0-5
-   Added -libs subpackage
*   Wed Dec 07 2016 Xiaolin Li <xiaolinl@vmware.com> 7.51.0-4
-   Added -devel subpackage.
*   Wed Nov 30 2016 Xiaolin Li <xiaolinl@vmware.com> 7.51.0-3
-   Enable sftp support.
*   Thu Nov 24 2016 Alexey Makhalov <amakhalov@vmware.com> 7.51.0-2
-   Required krb5-devel.
*   Wed Nov 02 2016 Anish Swaminathan <anishs@vmware.com> 7.51.0-1
-   Upgrade curl to 7.51.0
*   Wed Oct 05 2016 ChangLee <changlee@vmware.com> 7.50.3-2
-   Modified %check
*   Thu Sep 15 2016 Xiaolin Li <xiaolinl@vmware.com> 7.50.3-1
-   Update curl to version 7.50.3.
*   Tue Aug 23 2016 Xiaolin Li <xiaolinl@vmware.com> 7.47.1-3
-   Enable gssapi in curl.
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 7.47.1-2
-   GA - Bump release of all rpms
*   Tue Feb 23 2016 Xiaolin Li <xiaolinl@vmware.com> 7.47.1-1
-   Updated to version 7.47.1
*   Thu Jan 14 2016 Xiaolin Li <xiaolinl@vmware.com> 7.46.0-1
-   Updated to version 7.46.0
*   Thu Aug 13 2015 Divya Thaluru <dthaluru@vmware.com> 7.43.0-1
-   Update to version 7.43.0.
*   Mon Apr 6 2015 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 7.41.0-1
-   Update to version 7.41.0.
