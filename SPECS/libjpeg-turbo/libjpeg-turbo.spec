Summary:        fork of the original IJG libjpeg which uses SIMD.
Name:           libjpeg-turbo
Version:        2.0.0
Release:        1%{?dist}
License:        IJG
URL:            http://sourceforge.net/projects/libjpeg-turbo
Group:          System Environment/Libraries
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        http://downloads.sourceforge.net/libjpeg-turbo/%{name}-%{version}.tar.gz
%define sha1    libjpeg-turbo=6d74b609294b6bae5a7cde035f7d6b80d60ebb77
Patch0:         libjpeg-turbo-CVE-2018-20330.patch
Patch1:         CVE-2018-19664.patch
Patch2:         CVE-2020-13790.patch
BuildRequires:  nasm
BuildRequires:  cmake
Requires:       nasm
%description
libjpeg-turbo is a fork of the original IJG libjpeg which uses SIMD to accelerate baseline JPEG compression and decompression. libjpeg is a library that implements JPEG image encoding, decoding and transcoding.

%package        devel
Summary:        Header and development files
Requires:       %{name} = %{version}-%{release}
%description    devel
It contains the libraries and header files to create applications

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
mkdir -p build
cd build
cmake \
      -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
      -DCMAKE_SKIP_RPATH:BOOL=YES \
      -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
      -DENABLE_STATIC:BOOL=NO ..
make %{?_smp_mflags}

%install
cd build
make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -delete

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*.so*
%{_datadir}/*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
*   Fri Sep 11 2020 Tapas Kundu <tkundu@vmware.com> 2.0.0-1
-   Initial release with photon 1.0

