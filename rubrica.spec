Summary:	Address book application
Name:		rubrica
Version:	0.9.9.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://digilander.libero.it/nfragale/download/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-am.patch
URL:		http://digilander.libero.it/nfragale/index_gb.html
BuildRequires:	libgnomeui-devel >= 2.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME2

%description
Rubrica is an address book written using GTK+ and GNOME. It allows you to
add personal data (name, surname, address, etc.), Web links, email
addresses, telephone numbers, job information (company where contact
works, company infos, contact's assigment, etc.) and notes. XML is used to
store the data. It can import addressbooks from GnomeCard and export to
HTML.

%prep
%setup -q
%patch0 -p1

%build
aclocal
%{__autoconf}
autoheader
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%post
GCONF_CONFIG_SOURCE="`%{_bindir}/gconftool-2 --get-default-source`" \
%{_bindir}/gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/*.schemas > /dev/null

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog NEWS TODO AUTHORS doc/examples.rub
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/%{name}
%{_pixmapsdir}/%{name}
