%define upstream_name    Mixin-ExtraFields
%define upstream_version 0.100971

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Store extras in a hashy object's guts
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Mixin/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(String::RewritePrefix)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Sub::Install)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


