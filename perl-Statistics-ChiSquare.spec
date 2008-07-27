#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Statistics
%define		pnam	ChiSquare
Summary:	Statistics::ChiSquare Perl module
Summary(cs.UTF-8):	Modul Statistics::ChiSquare pro Perl
Summary(da.UTF-8):	Perlmodul Statistics::ChiSquare
Summary(de.UTF-8):	Statistics::ChiSquare Perl Modul
Summary(es.UTF-8):	Módulo de Perl Statistics::ChiSquare
Summary(fr.UTF-8):	Module Perl Statistics::ChiSquare
Summary(it.UTF-8):	Modulo di Perl Statistics::ChiSquare
Summary(ja.UTF-8):	Statistics::ChiSquare Perl モジュール
Summary(ko.UTF-8):	Statistics::ChiSquare 펄 모줄
Summary(nb.UTF-8):	Perlmodul Statistics::ChiSquare
Summary(pl.UTF-8):	Moduł Perla Statistics::ChiSquare
Summary(pt.UTF-8):	Módulo de Perl Statistics::ChiSquare
Summary(pt_BR.UTF-8):	Módulo Perl Statistics::ChiSquare
Summary(ru.UTF-8):	Модуль для Perl Statistics::ChiSquare
Summary(sv.UTF-8):	Statistics::ChiSquare Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Statistics::ChiSquare
Summary(zh_CN.UTF-8):	Statistics::ChiSquare Perl 模块
Name:		perl-Statistics-ChiSquare
Version:	0.5
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1c02a8eabeed699e0e8b2de9f09dc2ca
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Statistics::ChiSquare - How random is your data?

%description -l pl.UTF-8
Statistics::ChiSquare - Jak bardzo losowe są twoje dane?

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
