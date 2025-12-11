Name:           lab2
Version:        1.0
Release:        1%{?dist}
Summary:        Script to count files in /etc directory
License:        GPL
Group:          Applications/System
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       bash, findutils, coreutils
Source0:        lab2-1.0.tar.gz

%description
This is the package for lab #2.
It installs a script that counts files excluding directories and links in the /etc directory.

%prep

%setup -q

%build

%install
rm -rf %{buildroot}
#Install the script
install -D -m 755 lab1.sh %{buildroot}/usr/bin/lab2

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/lab2

%changelog
* Thu Dec 11 2025 Maria Fesiun <mariafesyun@gmail.com> - 1.0-1
- Initial build
