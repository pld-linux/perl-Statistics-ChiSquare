#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Statistics
%define	pnam	ChiSquare
Summary:	Statistics::ChiSquare Perl module
Summary(cs):	Modul Statistics::ChiSquare pro Perl
Summary(da):	Perlmodul Statistics::ChiSquare
Summary(de):	Statistics::ChiSquare Perl Modul
Summary(es):	Módulo de Perl Statistics::ChiSquare
Summary(fr):	Module Perl Statistics::ChiSquare
Summary(it):	Modulo di Perl Statistics::ChiSquare
Summary(ja):	Statistics::ChiSquare Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Statistics::ChiSquare ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul Statistics::ChiSquare
Summary(pl):	Modu³ Perla Statistics::ChiSquare
Summary(pt):	Módulo de Perl Statistics::ChiSquare
Summary(pt_BR):	Módulo Perl Statistics::ChiSquare
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Statistics::ChiSquare
Summary(sv):	Statistics::ChiSquare Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Statistics::ChiSquare
Summary(zh_CN):	Statistics::ChiSquare Perl Ä£¿é
Name:		perl-Statistics-ChiSquare
Version:	0.5
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1c02a8eabeed699e0e8b2de9f09dc2ca
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Statistics::ChiSquare - How random is your data?

%description -l pl
Statistics::ChiSquare - Jak bardzo losowe s± twoje dane?

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Statistics/ChiSquare.pm
# empty autosplit.ix
#%dir %{perl_vendorlib}/auto/Statistics/ChiSquare
#%%{perl_vendorlib}/auto/Statistics/ChiSquare/autosplit.ix
%{_mandir}/man3/*
