Summary: Fakeroot subuid/subgid sync tool 
Name: fakerootuidsync
Version: 0.0.1
Release: 1
License: GPL
Group: System Environment/Base
Source0: %{name}-%{version}-%{release}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: python3 
Requires: systemd

%description
Tool to syncronise/generate /etc/subuid and /etc/subgid from users
in the passwd/groups environment.

%prep
%setup -n %{name}-%{version}-%{release}

%install
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_sysconfdir}
install -m 755 fakerootuidsync \
    %{buildroot}%{_sbindir}/fakerootuidsync
install -m 644 fakerootuidsync.yaml \
    %{buildroot}%{_sysconfdir}/fakerootuidsync.yaml
install -D -m644 fakerootuidsync.service \
    %{buildroot}/lib/systemd/systemd/fakerootuidsync.service

%postun
%systemd_post fakerootuidsync.service

%clean
rm -rf %{buildroot}

%files
%doc README LICENSE
%defattr(-,root,root,-)
%{_sbindir}/fakerootuidsync
/lib/systemd/systemd/fakerootuidsync.service
%config %{_sysconfdir}/fakerootuidsync.yaml

%changelog
* Thu Jan 23 2020 Miguel Gila <miguel.gila@cscs.ch> - 0.0.1-1
- Initial RPM packaging