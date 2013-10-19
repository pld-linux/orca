Summary:	Flexible, extensible, and powerful assistive technology
Summary(pl.UTF-8):	Elastyczna, rozszerzalna i potężna technologia wspomagająca
Name:		orca
Version:	3.10.1
Release:	1
License:	LGPL v2+
Group:		X11/Applications/Accessibility
Source0:	http://ftp.gnome.org/pub/GNOME/sources/orca/3.10/%{name}-%{version}.tar.xz
# Source0-md5:	ef375460818c5ee81973253a3a2ef897
URL:		http://www.gnome.org/projects/orca/
BuildRequires:	at-spi2-atk-devel >= 2.10
BuildRequires:	at-spi2-core-devel >= 2.10
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	gnome-doc-utils >= 0.18.0
BuildRequires:	gtk+3-devel >= 3.6.2
BuildRequires:	intltool >= 0.40.0
BuildRequires:	liblouis-devel
BuildRequires:	pkgconfig
#BuildRequires:	python3-brlapi >= 3.8
BuildRequires:	python3-devel >= 3.3
BuildRequires:	python3-louis
BuildRequires:	python3-modules >= 3.3
BuildRequires:	python3-pyatspi >= 2.10
BuildRequires:	python3-pygobject3 >= 3.10
BuildRequires:	python3-speech-dispatcher
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
BuildRequires:	yelp-tools
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme
#Requires:	python3-brlapi >= 3.8
Requires:	python3-pyatspi >= 2.10
Requires:	python3-pycairo
Requires:	python3-pygobject3 >= 3.10
Requires:	python3-speech-dispatcher
Suggests:	python3-louis
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
%{_iconsdir}/hicolor/*/apps/orca.*
%dir %{py3_sitescriptdir}/orca
%{py3_sitescriptdir}/orca/*.py
%{py3_sitescriptdir}/orca/__pycache__
%dir %{py3_sitescriptdir}/orca/backends
%{py3_sitescriptdir}/orca/backends/*.py
%{py3_sitescriptdir}/orca/backends/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts
%{py3_sitescriptdir}/orca/scripts/*.py
%{py3_sitescriptdir}/orca/scripts/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps
%{py3_sitescriptdir}/orca/scripts/apps/*.py
%{py3_sitescriptdir}/orca/scripts/apps/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/Banshee
%{py3_sitescriptdir}/orca/scripts/apps/Banshee/*.py
%{py3_sitescriptdir}/orca/scripts/apps/Banshee/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/Eclipse
%{py3_sitescriptdir}/orca/scripts/apps/Eclipse/*.py
%{py3_sitescriptdir}/orca/scripts/apps/Eclipse/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/Instantbird
%{py3_sitescriptdir}/orca/scripts/apps/Instantbird/*.py
%{py3_sitescriptdir}/orca/scripts/apps/Instantbird/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/Mozilla
%{py3_sitescriptdir}/orca/scripts/apps/Mozilla/*.py
%{py3_sitescriptdir}/orca/scripts/apps/Mozilla/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/Thunderbird
%{py3_sitescriptdir}/orca/scripts/apps/Thunderbird/*.py
%{py3_sitescriptdir}/orca/scripts/apps/Thunderbird/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/ddu
%{py3_sitescriptdir}/orca/scripts/apps/ddu/*.py
%{py3_sitescriptdir}/orca/scripts/apps/ddu/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/ekiga
%{py3_sitescriptdir}/orca/scripts/apps/ekiga/*.py
%{py3_sitescriptdir}/orca/scripts/apps/ekiga/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/empathy
%{py3_sitescriptdir}/orca/scripts/apps/empathy/*.py
%{py3_sitescriptdir}/orca/scripts/apps/empathy/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/evince
%{py3_sitescriptdir}/orca/scripts/apps/evince/*.py
%{py3_sitescriptdir}/orca/scripts/apps/evince/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/evolution
%{py3_sitescriptdir}/orca/scripts/apps/evolution/*.py
%{py3_sitescriptdir}/orca/scripts/apps/evolution/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/gajim
%{py3_sitescriptdir}/orca/scripts/apps/gajim/*.py
%{py3_sitescriptdir}/orca/scripts/apps/gajim/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/gcalctool
%{py3_sitescriptdir}/orca/scripts/apps/gcalctool/*.py
%{py3_sitescriptdir}/orca/scripts/apps/gcalctool/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/gdm-simple-greeter
%{py3_sitescriptdir}/orca/scripts/apps/gdm-simple-greeter/*.py
%{py3_sitescriptdir}/orca/scripts/apps/gdm-simple-greeter/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/gdmlogin
%{py3_sitescriptdir}/orca/scripts/apps/gdmlogin/*.py
%{py3_sitescriptdir}/orca/scripts/apps/gdmlogin/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/gedit
%{py3_sitescriptdir}/orca/scripts/apps/gedit/*.py
%{py3_sitescriptdir}/orca/scripts/apps/gedit/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/gnome-documents
%{py3_sitescriptdir}/orca/scripts/apps/gnome-documents/*.py
%{py3_sitescriptdir}/orca/scripts/apps/gnome-documents/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/gnome-keyring-ask
%{py3_sitescriptdir}/orca/scripts/apps/gnome-keyring-ask/*.py
%{py3_sitescriptdir}/orca/scripts/apps/gnome-keyring-ask/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/gnome-mud
%{py3_sitescriptdir}/orca/scripts/apps/gnome-mud/*.py
%{py3_sitescriptdir}/orca/scripts/apps/gnome-mud/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/gnome-panel
%{py3_sitescriptdir}/orca/scripts/apps/gnome-panel/*.py
%{py3_sitescriptdir}/orca/scripts/apps/gnome-panel/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/gnome-screensaver-dialog
%{py3_sitescriptdir}/orca/scripts/apps/gnome-screensaver-dialog/*.py
%{py3_sitescriptdir}/orca/scripts/apps/gnome-screensaver-dialog/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/gnome-search-tool
%{py3_sitescriptdir}/orca/scripts/apps/gnome-search-tool/*.py
%{py3_sitescriptdir}/orca/scripts/apps/gnome-search-tool/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/gnome-system-monitor
%{py3_sitescriptdir}/orca/scripts/apps/gnome-system-monitor/*.py
%{py3_sitescriptdir}/orca/scripts/apps/gnome-system-monitor/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/gnome-terminal
%{py3_sitescriptdir}/orca/scripts/apps/gnome-terminal/*.py
%{py3_sitescriptdir}/orca/scripts/apps/gnome-terminal/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/gnome_segv2
%{py3_sitescriptdir}/orca/scripts/apps/gnome_segv2/*.py
%{py3_sitescriptdir}/orca/scripts/apps/gnome_segv2/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/gtk-window-decorator
%{py3_sitescriptdir}/orca/scripts/apps/gtk-window-decorator/*.py
%{py3_sitescriptdir}/orca/scripts/apps/gtk-window-decorator/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/gnome-window-properties
%{py3_sitescriptdir}/orca/scripts/apps/gnome-window-properties/*.py
%{py3_sitescriptdir}/orca/scripts/apps/gnome-window-properties/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/liferea
%{py3_sitescriptdir}/orca/scripts/apps/liferea/*.py
%{py3_sitescriptdir}/orca/scripts/apps/liferea/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/metacity
%{py3_sitescriptdir}/orca/scripts/apps/metacity/*.py
%{py3_sitescriptdir}/orca/scripts/apps/metacity/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/nautilus
%{py3_sitescriptdir}/orca/scripts/apps/nautilus/*.py
%{py3_sitescriptdir}/orca/scripts/apps/nautilus/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/notification-daemon
%{py3_sitescriptdir}/orca/scripts/apps/notification-daemon/*.py
%{py3_sitescriptdir}/orca/scripts/apps/notification-daemon/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/notify-osd
%{py3_sitescriptdir}/orca/scripts/apps/notify-osd/*.py
%{py3_sitescriptdir}/orca/scripts/apps/notify-osd/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/packagemanager
%{py3_sitescriptdir}/orca/scripts/apps/packagemanager/*.py
%{py3_sitescriptdir}/orca/scripts/apps/packagemanager/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/pidgin
%{py3_sitescriptdir}/orca/scripts/apps/pidgin/*.py
%{py3_sitescriptdir}/orca/scripts/apps/pidgin/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/planner
%{py3_sitescriptdir}/orca/scripts/apps/planner/*.py
%{py3_sitescriptdir}/orca/scripts/apps/planner/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/rhythmbox
%{py3_sitescriptdir}/orca/scripts/apps/rhythmbox/*.py
%{py3_sitescriptdir}/orca/scripts/apps/rhythmbox/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/soffice
%{py3_sitescriptdir}/orca/scripts/apps/soffice/*.py
%{py3_sitescriptdir}/orca/scripts/apps/soffice/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/xfwm4
%{py3_sitescriptdir}/orca/scripts/apps/xfwm4/*.py
%{py3_sitescriptdir}/orca/scripts/apps/xfwm4/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/toolkits
%{py3_sitescriptdir}/orca/scripts/toolkits/*.py
%{py3_sitescriptdir}/orca/scripts/toolkits/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/toolkits/CALLY
%{py3_sitescriptdir}/orca/scripts/toolkits/CALLY/*.py
%{py3_sitescriptdir}/orca/scripts/toolkits/CALLY/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/toolkits/Gecko
%{py3_sitescriptdir}/orca/scripts/toolkits/Gecko/*.py
%{py3_sitescriptdir}/orca/scripts/toolkits/Gecko/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/toolkits/J2SE-access-bridge
%{py3_sitescriptdir}/orca/scripts/toolkits/J2SE-access-bridge/*.py
%{py3_sitescriptdir}/orca/scripts/toolkits/J2SE-access-bridge/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/toolkits/WebKitGtk
%{py3_sitescriptdir}/orca/scripts/toolkits/WebKitGtk/*.py
%{py3_sitescriptdir}/orca/scripts/toolkits/WebKitGtk/__pycache__
%{_mandir}/man1/orca.1*
%{_sysconfdir}/xdg/autostart/orca-autostart.desktop
