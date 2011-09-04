Summary:	Flexible, extensible, and powerful assistive technology
Summary(pl.UTF-8):	Elastyczna, rozszerzalna i potężna technologia wspomagająca
Name:		orca
Version:	3.0.4
Release:	1
License:	LGPL v2
Group:		X11/Applications/Accessibility
Source0:	http://ftp.gnome.org/pub/GNOME/sources/orca/3.0/%{name}-%{version}.tar.bz2
# Source0-md5:	54bc9ec64be25f827e90c0af789b61e9
URL:		http://www.gnome.org/projects/orca/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils >= 0.18.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-brlapi
BuildRequires:	python-dbus
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-gnome-bonobo >= 2.20.0
BuildRequires:	python-gnome-desktop-libwnck
BuildRequires:	python-gnome-gconf
BuildRequires:	python-pyatspi >= 2.0.0
BuildRequires:	python-pygtk-devel >= 2:2.12.0
BuildRequires:	python-pyorbit
BuildRequires:	python-pyxdg
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk-update-icon-cache
Requires:	gnome-speech-driver
Requires:	hicolor-icon-theme
Requires:	python-brlapi
Requires:	python-dbus
Requires:	python-gnome-gconf
Requires:	python-pyatspi >= 2.0.0
Requires:	python-pygobject
Requires:	python-pygtk-atk
Requires:	python-pygtk-gtk
Requires:	python-pyxdg
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
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

%find_lang %{name} --with-gnome

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
%{_datadir}/orca
%{_desktopdir}/orca.desktop
%{_iconsdir}/hicolor/*/*/orca.*
%dir %{py_sitedir}/orca
%{py_sitedir}/orca/*.py[co]
%dir %{py_sitedir}/orca/backends
%{py_sitedir}/orca/backends/*.py[co]
%dir %{py_sitedir}/orca/scripts
%{py_sitedir}/orca/scripts/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps
%{py_sitedir}/orca/scripts/apps/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/Banshee
%{py_sitedir}/orca/scripts/apps/Banshee/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/Eclipse
%{py_sitedir}/orca/scripts/apps/Eclipse/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/Instantbird
%{py_sitedir}/orca/scripts/apps/Instantbird/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/Mozilla
%{py_sitedir}/orca/scripts/apps/Mozilla/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/Thunderbird
%{py_sitedir}/orca/scripts/apps/Thunderbird/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/acroread
%{py_sitedir}/orca/scripts/apps/acroread/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/ddu
%{py_sitedir}/orca/scripts/apps/ddu/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/ekiga
%{py_sitedir}/orca/scripts/apps/ekiga/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/empathy
%{py_sitedir}/orca/scripts/apps/empathy/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/epiphany
%{py_sitedir}/orca/scripts/apps/epiphany/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/evolution
%{py_sitedir}/orca/scripts/apps/evolution/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/gajim
%{py_sitedir}/orca/scripts/apps/gajim/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/gcalctool
%{py_sitedir}/orca/scripts/apps/gcalctool/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/gdm-simple-greeter
%{py_sitedir}/orca/scripts/apps/gdm-simple-greeter/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/gdmlogin
%{py_sitedir}/orca/scripts/apps/gdmlogin/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/gedit
%{py_sitedir}/orca/scripts/apps/gedit/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/gnome-keyring-ask
%{py_sitedir}/orca/scripts/apps/gnome-keyring-ask/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/gnome-mud
%{py_sitedir}/orca/scripts/apps/gnome-mud/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/gnome-panel
%{py_sitedir}/orca/scripts/apps/gnome-panel/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/gnome-screensaver-dialog
%{py_sitedir}/orca/scripts/apps/gnome-screensaver-dialog/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/gnome-search-tool
%{py_sitedir}/orca/scripts/apps/gnome-search-tool/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/gnome-system-monitor
%{py_sitedir}/orca/scripts/apps/gnome-system-monitor/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/gnome-terminal
%{py_sitedir}/orca/scripts/apps/gnome-terminal/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/gnome_segv2
%{py_sitedir}/orca/scripts/apps/gnome_segv2/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/gtk-window-decorator
%{py_sitedir}/orca/scripts/apps/gtk-window-decorator/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/gnome-window-properties
%{py_sitedir}/orca/scripts/apps/gnome-window-properties/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/liferea
%{py_sitedir}/orca/scripts/apps/liferea/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/metacity
%{py_sitedir}/orca/scripts/apps/metacity/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/nautilus
%{py_sitedir}/orca/scripts/apps/nautilus/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/notification-daemon
%{py_sitedir}/orca/scripts/apps/notification-daemon/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/notify-osd
%{py_sitedir}/orca/scripts/apps/notify-osd/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/packagemanager
%{py_sitedir}/orca/scripts/apps/packagemanager/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/pidgin
%{py_sitedir}/orca/scripts/apps/pidgin/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/planner
%{py_sitedir}/orca/scripts/apps/planner/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/rhythmbox
%{py_sitedir}/orca/scripts/apps/rhythmbox/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/soffice
%{py_sitedir}/orca/scripts/apps/soffice/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/xfwm4
%{py_sitedir}/orca/scripts/apps/xfwm4/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/yelp
%{py_sitedir}/orca/scripts/apps/yelp/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/yelp/yelp_v2
%{py_sitedir}/orca/scripts/apps/yelp/yelp_v2/*.py[co]
%dir %{py_sitedir}/orca/scripts/apps/yelp/yelp_v3
%{py_sitedir}/orca/scripts/apps/yelp/yelp_v3/*.py[co]
%dir %{py_sitedir}/orca/scripts/toolkits
%{py_sitedir}/orca/scripts/toolkits/*.py[co]
%dir %{py_sitedir}/orca/scripts/toolkits/CALLY
%{py_sitedir}/orca/scripts/toolkits/CALLY/*.py[co]
%dir %{py_sitedir}/orca/scripts/toolkits/Gecko
%{py_sitedir}/orca/scripts/toolkits/Gecko/*.py[co]
%dir %{py_sitedir}/orca/scripts/toolkits/J2SE-access-bridge
%{py_sitedir}/orca/scripts/toolkits/J2SE-access-bridge/*.py[co]
%dir %{py_sitedir}/orca/scripts/toolkits/WebKitGtk
%{py_sitedir}/orca/scripts/toolkits/WebKitGtk/*.py[co]
%{_mandir}/man1/orca.1*
%{_sysconfdir}/xdg/autostart/orca-autostart.desktop
