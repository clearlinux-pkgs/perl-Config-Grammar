#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Config-Grammar
Version  : 1.12
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/D/DS/DSCHWEI/Config-Grammar-1.12.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DS/DSCHWEI/Config-Grammar-1.12.tar.gz
Summary  : 'A grammar-based, user-friendly config parser'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Config-Grammar-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Config::Grammar
===============
Config::Grammar is a Perl module to parse configuration files by
following a grammar, which specifies how the configuration file should
look like. The configuration files are nice to work with for humans
and the error messages are helpful because it tells right away that
for example you are setting a variable which isn't defined.

%package dev
Summary: dev components for the perl-Config-Grammar package.
Group: Development
Provides: perl-Config-Grammar-devel = %{version}-%{release}

%description dev
dev components for the perl-Config-Grammar package.


%package license
Summary: license components for the perl-Config-Grammar package.
Group: Default

%description license
license components for the perl-Config-Grammar package.


%prep
%setup -q -n Config-Grammar-1.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Config-Grammar
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Config-Grammar/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Config/Grammar.pm
/usr/lib/perl5/vendor_perl/5.28.1/Config/Grammar/Document.pm
/usr/lib/perl5/vendor_perl/5.28.1/Config/Grammar/Dynamic.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Config::Grammar.3
/usr/share/man/man3/Config::Grammar::Dynamic.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Config-Grammar/LICENSE
