Summary:	Flexible, extensible, and powerful assistive technology
Summary(pl.UTF-8):	Elastyczna, rozszerzalna i potężna technologia wspomagająca
Name:		orca
Version:	2.26.1
Release:	1
License:	LGPL
Group:		X11/Applications/Accessibility
Source0:	http://ftp.gnome.org/pub/GNOME/sources/orca/2.26/%{name}-%{version}.tar.bz2
# Source0-md5:	7c8b995b0e55cf902d3a658f1adae0cf
URL:		http://www.gnome.org/projects/orca/
BuildRequires:	ORBit2-devel >= 1:2.14.8
BuildRequires:	at-spi-devel >= 1.24.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	brlapi-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.18.0
BuildRequires:	gnome-mag >= 0.14.8
BuildRequires:	gnome-speech >= 0.4.11
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libbonobo-devel >= 2.24.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-gnome-bonobo >= 2.20.0
BuildRequires:	python-pygtk-devel >= 2:2.12.0
BuildRequires:	python-pyorbit
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	gnome-mag >= 0.14.8
Requires:	gnome-speech-driver
Requires:	python-pyatspi
# XXX: based on spotted runtime errors:
Requires:	libgail-gnome
#
Requires:	python-pygobject
Requires:	python-pygtk-atk
Provides:	gnopernicus
Obsoletes:	gnopernicus
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Orca is a flexible, extensible, and powerful assistive technology for
people with visual impairments. Using various combinations of speech
synthesis, braille, and magnification, Orca helps provide access to
applications and toolkits that support the AT-SPI (e.g., the GNOME
desktop).

%description -l pl.UTF-8
Orca to elastyczna, rozszerzalna i potężna technologia wspomagająca
dla ludzi z zaburzeniami widzenia. Przy użyciu różnych kombinacji
syntezy mowy, braille'a i powiększania Orca pomaga w uzyskaniu dostępu
do aplikacji i toolkitów obsługujących AT-SPI (np. pochodzących ze
środowiska GNOME).

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/orca/brlmodule.la
%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README TODO
%attr(755,root,root) %{_bindir}/orca
%dir %{_datadir}/orca
%dir %{_datadir}/orca/glade
%{_datadir}/orca/glade/*.glade
%{_desktopdir}/orca.desktop
%{_iconsdir}/hicolor/*/*/orca.*
%dir %{py_sitedir}/orca
%attr(755,root,root) %{py_sitedir}/orca/brlmodule.so
%{py_sitedir}/orca/*.py[co]
%dir %{py_sitedir}/orca/scripts
%{py_sitedir}/orca/scripts/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps
%{py_sitedir}/orca/scripts/apps/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/Thunderbird
%{py_sitedir}/orca/scripts/apps/Thunderbird/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/evolution
%{py_sitedir}/orca/scripts/apps/evolution/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/gcalctool
%{py_sitedir}/orca/scripts/apps/gcalctool/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/gedit
%{py_sitedir}/orca/scripts/apps/gedit/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/gnome-window-properties
%{py_sitedir}/orca/scripts/apps/gnome-window-properties/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/pidgin
%{py_sitedir}/orca/scripts/apps/pidgin/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/planner
%{py_sitedir}/orca/scripts/apps/planner/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/rhythmbox
%{py_sitedir}/orca/scripts/apps/rhythmbox/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/soffice
%{py_sitedir}/orca/scripts/apps/soffice/*.py[co]
%dir %{py_sitedir}/orca/scripts/toolkits
%{py_sitedir}/orca/scripts/toolkits/*.py[co]
%dir %{py_sitedir}/orca/scripts/toolkits/Gecko
%{py_sitedir}/orca/scripts/toolkits/Gecko/*.py[co]
%dir %{py_sitedir}/orca/scripts/toolkits/J2SE-access-bridge
%{py_sitedir}/orca/scripts/toolkits/J2SE-access-bridge/*.py[co]
%{_mandir}/man1/orca.1*
