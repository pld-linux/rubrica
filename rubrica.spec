Summary:	Address book application
Summary(pl.UTF-8):	Książka adresowa
Name:		rubrica
Version:	1.1.40
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://digilander.libero.it/nfragale/download/rubrica/%{name}-%{version}.tar.bz2
# Source0-md5:	7b9ef08cfbd8893e94bda1cae296618d
URL:		http://digilander.libero.it/nfragale/index_gb.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libgnomeui-devel >= 2.4.0
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

%description -l pl.UTF-8
Rubrica to książka adresowa napisana z użyciem GTK+ i GNOME. Pozwala
na dodawanie danych osobowych (imię, nazwisko, adres itp.), odnośników
WWW, adresów e-mail, numerów telefonów, informacji o pracy (firma, w
której osoba pracuje, informacje o firmie itp.) oraz notatek. Do
przechowywania danych używany jest XML. Aplikacja może importować
książki adresowe z GnomeCard i eksportować do HTML-a.

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
%doc AUTHORS ChangeLog README doc/examples.rub
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/%{name}
