%include	/usr/lib/rpm/macros.perl
Summary:	Statistics-ChiSquare perl module
Summary(pl):	Modu³ perla Statistics-ChiSquare
Name:		perl-Statistics-ChiSquare
Version:	0.2
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Statistics/Statistics-ChiSquare-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Statistics-ChiSquare - How random is your data?

%description -l pl
Statistics-ChiSquare - Jak bardzo losowe s± twoje dane?

%prep
%setup -q -n Statistics

%build
cd ChiSquare
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
cd ChiSquare
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Statistics/ChiSquare
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
	Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChiSquare/Changes.gz
%{perl_sitelib}/Statistics/ChiSquare.pm
%{perl_sitearch}/auto/Statistics/ChiSquare

%{_mandir}/man3/*
