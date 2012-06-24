%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Statistics-ChiSquare perl module
Summary(pl):	Modu� perla Statistics-ChiSquare
Name:		perl-Statistics-ChiSquare
Version:	0.1
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Statistics/Statistics-ChiSquare-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Statistics-ChiSquare - How random is your data? 

%description -l pl
Statistics-ChiSquare - Jak bardzo losowe s� twoje dane?

%prep
%setup -q -n Statistics-ChiSquare-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Statistics/ChiSquare
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%{perl_sitelib}/Statistics/ChiSquare.pm
%{perl_sitearch}/auto/Statistics/ChiSquare

%{_mandir}/man3/*
