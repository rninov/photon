Summary:        setuid implementation of a subset of user namespaces.
Name:           bubblewrap
Version:        0.4.1
Release:        1%{?dist}
License:        LGPLv2+
URL:            https://github.com/projectatomic/bubblewrap
Group:          Applications/System
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        https://github.com/projectatomic/bubblewrap/releases/download/v%{version}/bubblewrap-%{version}.tar.xz
%define sha1    bubblewrap=00e121950ea494fcd9cfbe23971c0938d6be6755

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  libcap-devel

Requires:       libcap

%description
Bubblewrap could be viewed as setuid implementation of a subset of user namespaces. Emphasis on subset - specifically relevant to the above CVE, bubblewrap does not allow control over iptables.

The original bubblewrap code existed before user namespaces - it inherits code from xdg-app helper which in turn distantly derives from linux-user-chroot.

%prep
%autosetup -p1

%build
%configure \
    --disable-silent-rules \
    --with-priv-mode=none
make %{?_smp_mflags}

%install
[ %{buildroot} != "/"] && rm -rf %{buildroot}/*
make install DESTDIR=%{buildroot} %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%{_bindir}/bwrap
%{_datadir}/bash-completion/completions/bwrap

%changelog
*   Mon Jun 22 2020 Gerrit Photon <photon-checkins@vmware.com> 0.4.1-1
-   Automatic Version Bump
*   Mon Sep 03 2018 Keerthana K <keerthanak@vmware.com> 0.3.0-1
-   Updated to version 0.3.0.
*   Thu Aug 03 2017 Xiaolin Li <xiaolinl@vmware.com> 0.1.8-1
-   Initial build.  First version
