#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	DelimMatch
Summary:	Text::DelimMatch - Perl extension to find regexp delimited strings with proper nesting
#Summary(pl.UTF-8):	
Name:		perl-Text-DelimMatch
Version:	1.06a
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/N/NW/NWALSH/DelimMatch-%{version}.tar.gz
# Source0-md5:	8efb70c2326d0b8f551708e9cdc2b649
URL:		http://search.cpan.org/dist/DelimMatch/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These routines allow you to match delimited substrings in a
buffer.  The delimiters can be specified with any regular
expression and the start and end delimiters need not be the
same.  If the delimited text is properly nested, entire nested
groups are returned.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n DelimMatch-1.06

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/*/*.pm
%{_mandir}/man3/*
