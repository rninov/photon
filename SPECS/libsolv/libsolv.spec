Summary:        A free package dependency solver
Name:           libsolv
Version:        0.7.19
Release:        1%{?dist}
License:        BSD
URL:            https://github.com/openSUSE/libsolv
Source0:        https://github.com/openSUSE/libsolv/archive/%{name}-%{version}.tar.gz
%define sha1    libsolv=b4101632c56b00e0bd8f41d772a7998a3d000a74
Group:          Development/Tools
Vendor:         VMware, Inc.
Distribution:   Photon
Requires:       rpm-libs
Requires:       libdb
Requires:       expat-libs
Requires:       zlib
BuildRequires:  libdb-devel
BuildRequires:  cmake
BuildRequires:  rpm-devel
BuildRequires:  expat-devel
BuildRequires:  zlib-devel

%description
Libsolv is a free package management library, using SAT technology to solve requests.
It supports debian, rpm, archlinux and haiku style distributions.

%package devel
Summary:        Development headers for libsolv
Requires:       %{name} = %{version}-%{release}
Requires:       expat-devel
Provides:       pkgconfig(libsolv)
Provides:       pkgconfig(libsolvext)
%description devel
The libsolv-devel package contains libraries, header files and documentation
for developing applications that use libsolv.

%prep
%setup -q

%build
cmake \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DENABLE_RPMDB=ON \
    -DENABLE_COMPLEX_DEPS=ON \
    -DENABLE_RPMDB_BYRPMHEADER=ON \
    -DENABLE_RPMDB_LIBRPM=ON \
    -DENABLE_RPMMD=ON

make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -delete

%check
make %{?_smp_mflags} test

%files
%defattr(-,root,root)
%{_bindir}/*
%{_lib64dir}/libsolv.so.*
%{_lib64dir}/libsolvext.so.*
%{_mandir}/man1/*


%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_lib64dir}/libsolv.so
%{_lib64dir}/libsolvext.so
%{_lib64dir}/pkgconfig/*
%{_datadir}/cmake/*
%{_mandir}/man3/*

%changelog
*   Fri Jun 11 2021 Oliver Kurth <okurth@vmware.com> 0.7.19-1
-   Bump version
*   Wed Jun 09 2021 Prashant S Chauhan <psinghchauha@vmware.com> 0.6.35-8
-   Fix CVE-2021-3200
*   Wed Dec 09 2020 Prashant S Chauhan <psinghchauha@vmware.com> 0.6.35-7
-   Add zstd-devel as Build Requires
*   Thu Dec 03 2020 Tapas Kundu <tkundu@vmware.com> 0.6.35-6
-   Further extend choicerule filtering check
-   Refactor solver addchoicerules function
*   Thu Oct 29 2020 Keerthana K <keerthanak@vmware.com> 0.6.35-5
-   Fix CVE-2018-20532 CVE-2018-20533 CVE-2018-20534
*   Fri Aug 14 2020 Ankit Jain <ankitja@vmware.com> 0.6.35-4
-   Added 2 patches required to build libdnf latest version in rpm-ostree
*   Tue Feb 25 2020 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 0.6.35-3
-   provides pkgconfig(libsolvext).
*   Mon Feb 03 2020 Keerthana K <keerthanak@vmware.com> 0.6.35-2
-   Fix CVE-2019-20387
*   Tue Jun 04 2019 Ankit Jain <ankitja@vmware.com> 0.6.35-1
-   Updated to 0.6.35 and added a patch to fix Index outofBound
*   Thu Feb 14 2019 Keerthana K <keerthanak@vmware.com> 0.6.26-5
-   Fix for CVE-2018-20532, CVE-2018-20533, CVE-2018-20534.
*   Thu Mar 01 2018 Xiaolin Li <xiaolinl@vmware.com> 0.6.26-4
-   provides pkgconfig(libsolv).
*   Fri Apr 21 2017 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 0.6.26-3
-   update libdb make config
*   Fri Apr 14 2017 Alexey Makhalov <amakhalov@vmware.com> 0.6.26-2
-   Requires expat-libs and expat-devel.
*   Tue Apr 04 2017 Kumar Kaushik <kaushikk@vmware.com>  0.6.26-1
-   Upgrade to 0.6.26
*   Mon Dec 19 2016 Xiaolin Li <xiaolinl@vmware.com> 0.6.19-4
-   Added -devel subpackage.
*   Thu Oct 27 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 0.6.19-3
-   use libdb
*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 0.6.19-2
-   GA - Bump release of all rpms
*   Tue Feb 23 2016 Anish Swaminathan <anishs@vmware.com>  0.6.19-1
-   Upgrade to 0.6.19
*   Fri Jan 22 2016 Xiaolin Li <xiaolinl@vmware.com> 0.6.17-1
-   Updated to version 0.6.17
*   Tue Sep 22 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 0.6.6-3
-   Updated build-requires after creating devel package for db.
*   Wed May 20 2015 Touseef Liaqat <tliaqat@vmware.com> 0.6.6-2
-   Updated group.
*   Tue Nov 25 2014 Divya Thaluru <dthaluru@vmware.com> 0.6.6-1
-   Initial build. First version
