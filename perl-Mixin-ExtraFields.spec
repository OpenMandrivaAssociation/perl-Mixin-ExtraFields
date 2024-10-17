%define upstream_name    Mixin-ExtraFields
%define upstream_version 0.100971

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Store extras in a hashy object's guts
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Mixin/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(String::RewritePrefix)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Sub::Install)

BuildArch:	noarch

%description
Sometimes your well-defined object needs a way to tack on arbirary extra
fields. This might be a set of session-specific ephemeral data, a stash of
settings that need to be easy to grow over time, or any sort of
name-and-value parameters. Adding more and more methods can be cumbersome,
and may not be helpful if the names vary greatly. Accessing an object's
guts directly is simple, but is difficult to control when subclassing, and
can make altering your object's structure difficult.

Mixin::ExtraFields provides a simple way to add an arbitrary number of
stashes for named data. These data can be stored in the object, in a
database, or anywhere else. The storage mechanism is abstracted away from
the provided interface, so one storage mechanism can be easily swapped for
another. Multiple ExtraFields stashes can be mixed into one class, using
one or many storage mechanisms.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.100.971-2mdv2011.0
+ Revision: 654252
- rebuild for updated spec-helper

* Wed Apr 07 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.971-1mdv2011.0
+ Revision: 532713
- update to 0.100971

* Tue Jan 19 2010 Jérôme Quelin <jquelin@mandriva.org> 0.8.0-1mdv2010.1
+ Revision: 493493
- adding missing buildrequires
- update to 0.008

* Fri May 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.7.0-1mdv2010.0
+ Revision: 380978
- adding missing buildrequires:
- import perl-Mixin-ExtraFields


* Fri May 29 2009 cpan2dist 0.007-1mdv
- initial mdv release, generated with cpan2dist

