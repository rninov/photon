Summary:        Calico node and documentation for project calico.
Name:           calico
Version:        3.17.1
Release:        2%{?dist}
License:        Apache-2.0
URL:            https://github.com/projectcalico/node
Source0:        %{name}-%{version}.tar.gz
%define sha1 calico=55a9683f1a49d1ea3cba24bbd8a9cda266fb5cee
Group:          Development/Tools
Vendor:         VMware, Inc.
Distribution:   Photon
BuildRequires:  git
BuildRequires:  go
BuildRequires:  make

%description
Calico node is a container that bundles together various components reqiured for networking containers using project calico. This includes key components such as felix agent for programming routes and ACLs, BIRD routing daemon, and confd datastore monitor engine.

%prep
%setup -n node-%{version}

%build
mkdir -p dist
go build -v -i -o dist/calico-node cmd/calico-node/main.go

%install
install -vdm 755 %{buildroot}%{_bindir}
install dist/calico-node %{buildroot}%{_bindir}/
install -vdm 0755 %{buildroot}/usr/share/calico/docker/fs
cp -r filesystem/etc %{buildroot}/usr/share/calico/docker/fs/
cp -r filesystem/sbin %{buildroot}/usr/share/calico/docker/fs/
sed -i 's/. startup.env/source \/startup.env/g' %{buildroot}/usr/share/calico/docker/fs/etc/rc.local
sed -i 's/. startup.env/source \/startup.env/g' %{buildroot}/usr/share/calico/docker/fs/sbin/start_runit

%files
%defattr(-,root,root)
%{_bindir}/calico-node
/usr/share/calico/docker/fs/*

%changelog
*   Fri Jun 11 2021 Piyush Gupta<gpiyush@vmware.com> 3.17.1-2
-   Bump up version to compile with new go
*   Tue Feb 09 2021 Prashant S Chauhan <psinghchauha@vmware.com> 3.17.1-1
-   Update to version 3.17.1
*   Fri Feb 05 2021 Harinadh D <hdommaraju@vmware.com> 3.15.2-3
-   Bump up version to compile with new go
*   Fri Jan 15 2021 Piyush Gupta<gpiyush@vmware.com> 3.15.2-2
-   Bump up version to compile with new go
*   Sat Aug 29 2020 Ashwin H <ashwinh@vmware.com> 3.15.2-1
-   Update to 3.15.2
*   Wed Jun 17 2020 Ashwin H <ashwinh@vmware.com> 3.6.1-3
-   Fix dependency for cloud.google.com-go
*   Tue Jun 09 2020 Ashwin H <ashwinh@vmware.com> 3.6.1-2
-   Use cache for dependencies
*   Wed May 08 2019 Ashwin H <ashwinh@vmware.com> 3.6.1-1
-   Update to 3.6.1
*   Mon Jan 28 2019 Bo Gan <ganb@vmware.com> 2.6.7-4
-   Fix CVE-2018-17846 and CVE-2018-17143
*   Mon Jan 21 2019 Bo Gan <ganb@vmware.com> 2.6.7-3
-   Build using go 1.9.7
*   Mon Sep 24 2018 Tapas Kundu <tkundu@vmware.com> 2.6.7-2
-   Build using go version 1.9
*   Fri May 18 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 2.6.7-1
-   Calico Node v2.6.7.
*   Tue Dec 05 2017 Vinay Kulkarni <kulkarniv@vmware.com> 2.6.3-1
-   Calico Node v2.6.3.
*   Fri Nov 03 2017 Vinay Kulkarni <kulkarniv@vmware.com> 2.6.2-1
-   Calico Node v2.6.2.
*   Wed Nov 01 2017 Vinay Kulkarni <kulkarniv@vmware.com> 2.5.1-1
-   Calico Node v2.5.1.
*   Wed Aug 16 2017 Vinay Kulkarni <kulkarniv@vmware.com> 2.4.1-1
-   Calico Node for PhotonOS.
