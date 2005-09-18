Summary:	Address book application
Summary(pl):	Ksi±¿ka adresowa
Name:		rubrica
Version:	1.1.60
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	19e2c79b6ec9912b3bc48fb15f93d8bd
URL:		http://rubrica.berlios.de
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libral-devel >= 0.50
BuildRequires:	rpm-build >= 4.1-10
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rubrica is an address book written using GTK+ and GNOME. It allows you
to add personal data (name, surname, address, etc.), Web links, email
addresses, telephone numbers, job information (company where contact
works, company infos, contact's assigment, etc.) and notes. XML is
used to store the data. It can import addressbooks from GnomeCard and
export to HTML.

%description -l pl
Rubrica to ksi±¿ka adresowa napisana z u¿yciem GTK+ i GNOME. Pozwala
na dodawanie danych osobowych (imiê, nazwisko, adres itp.), odno¶ników
WWW, adresów e-mail, numerów telefonów, informacji o pracy (firma, w
której osoba pracuje, informacje o firmie itp.) oraz notatek. Do
przechowywania danych u¿ywany jest XML. Aplikacja mo¿e importowaæ
ksi±¿ki adresowe z GnomeCard i eksportowaæ do HTML-a.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog NEWS TODO AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/%{name}.png
