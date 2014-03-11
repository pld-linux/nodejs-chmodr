Summary:	Like `chmod -R`
Name:		nodejs-chmodr
Version:	0.1.0
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/chmodr/-/chmodr-%{version}.tgz
# Source0-md5:	6461673dd949fdf7de4be40792914931
URL:		https://github.com/isaacs/chmodr
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Like `chmod -R`.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/chmodr
cp -p chmodr.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/chmodr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/chmodr
