Summary:        The source repository for the TPM (Trusted Platform Module) 2 tools
Name:           tpm2-tools
Version:        4.3.0
Release:        5%{?dist}
License:        BSD 2-Clause
URL:            https://github.com/tpm2-software/tpm2-tools
Group:          System Environment/Security
Vendor:         VMware, Inc.
Distribution:   Photon

Source0:        %{name}-%{version}.tar.gz
%define sha1    tpm2=bdf84d825119e4022ac2aa5f860b199cd7af2990
Patch0:         0001-support-for-openssl-3.0.0.patch

BuildRequires:  openssl-devel curl-devel tpm2-tss-devel

Requires:       openssl curl tpm2-tss
%if %{with_check}
BuildRequires:  ibmtpm
BuildRequires:  systemd
%endif

%description
The source repository for the TPM (Trusted Platform Module) 2 tools

%prep
%autosetup -p1

%build
sed -i "/compatibility/a extern int BN_bn2binpad(const BIGNUM *a, unsigned char *to, int tolen);" lib/tpm2_openssl.c
%configure --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%check
if [ ! -f /dev/tpm0 ];then
   systemctl start ibmtpm_server.service
   export TPM2TOOLS_TCTI=mssim:host=localhost,port=2321
   tpm2_startup -c
   tpm2_pcrlist
fi
make %{?_smp_mflags} check

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1
/usr/share/bash-completion/*

%changelog
*   Thu Jul 15 2021 Satya Naga Vasamsetty <svasamsetty@vmware.com> 4.3.0-5
-   Openssl 3.0.0 support
*   Tue Feb 09 2021 Alexey Makhalov <amakhalov@vmware.com> 4.3.0-4
-   Fix compilation issue with BN_bn2binpad
*   Tue Jan 19 2021 Shreenidhi Shedi <sshedi@vmware.com> 4.3.0-3
-   Removed patch which was added to fix a build issue
*   Thu Oct 15 2020 Shreenidhi Shedi <sshedi@vmware.com> 4.3.0-2
-   Fix build warnings
*   Tue Sep 01 2020 Gerrit Photon <photon-checkins@vmware.com> 4.3.0-1
-   Automatic Version Bump
*   Fri Jul 24 2020 Gerrit Photon <photon-checkins@vmware.com> 4.2.1-1
-   Automatic Version Bump
*   Wed Jun 10 2020 Michelle Wang <michellew@vmware.com> 3.1.3-2
-   update make check with ibmtpm
*   Thu Feb 21 2019 Alexey Makhalov <amakhalov@vmware.com> 3.1.3-1
-   Initial build. First version
