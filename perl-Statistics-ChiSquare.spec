%include	/usr/lib/rpm/macros.perl
%define	pdir	Statistics
%define	pnam	ChiSquare
Summary:	Statistics-ChiSquare perl module
Summary(pl):	Modu³ perla Statistics-ChiSquare
Name:		perl-Statistics-ChiSquare
Version:	0.2
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Statistics-ChiSquare - How random is your data?

%description -l pl
Statistics-ChiSquare - Jak bardzo losowe s± twoje dane?

%prep
%setup -q -n %{pdir}

%build
cd ChiSquare
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd ChiSquare
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChiSquare/*.gz
%{perl_sitelib}/Statistics/ChiSquare.pm
%{_mandir}/man3/*
