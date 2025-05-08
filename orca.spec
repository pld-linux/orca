#
# Conditional build:
%bcond_with	spiel	# experimental Spiel support

Summary:	Flexible, extensible, and powerful assistive technology
Summary(pl.UTF-8):	Elastyczna, rozszerzalna i potężna technologia wspomagająca
Name:		orca
Version:	48.1
Release:	1
License:	LGPL v2+
Group:		X11/Applications/Accessibility
Source0:	https://download.gnome.org/sources/orca/48/%{name}-%{version}.tar.xz
# Source0-md5:	c58160b3c28b53bb2a253607a161ff81
URL:		https://orca.gnome.org/
BuildRequires:	at-spi2-atk-devel >= 2.50.0
BuildRequires:	at-spi2-core-devel >= 2.50.0
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gtk+3-devel >= 3.24
%{?with_spiel:BuildRequires:	libspiel-devel >= 1.0.1}
BuildRequires:	liblouis-devel
BuildRequires:	meson >= 1.0.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3-brlapi >= 3.9
BuildRequires:	python3-devel >= 1:3.10
BuildRequires:	python3-louis
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-pygobject3-devel >= 3.18
BuildRequires:	python3-speech-dispatcher >= 0.8
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires:	at-spi2-atk >= 2.50.0
Requires:	at-spi2-core >= 2.50.0
Requires:	gtk+3 >= 3.24
Requires:	hicolor-icon-theme
%{?with_spiel:Requires:	libspiel >= 1.0.1}
Requires:	python3-brlapi >= 3.9
Requires:	python3-gstreamer >= 1.0
Requires:	python3-modules >= 1:3.10
Requires:	python3-pycairo
Requires:	python3-pygobject3 >= 3.18
Requires:	python3-speech-dispatcher >= 0.8
Suggests:	libwnck >= 3.0
Suggests:	python3-louis
Suggests:	python3-psutil
Provides:	gnopernicus
Obsoletes:	gnopernicus < 1.2
BuildArch:	noarch
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
%meson \
	%{?with_spiel:-Dspiel=true}

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README.md TODO
%attr(755,root,root) %{_bindir}/orca
%{_datadir}/orca
%{_iconsdir}/hicolor/*/apps/orca.*
%{_iconsdir}/hicolor/symbolic/apps/orca-symbolic.svg
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
%dir %{py3_sitescriptdir}/orca/scripts/apps/SeaMonkey
%{py3_sitescriptdir}/orca/scripts/apps/SeaMonkey/*.py
%{py3_sitescriptdir}/orca/scripts/apps/SeaMonkey/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/Thunderbird
%{py3_sitescriptdir}/orca/scripts/apps/Thunderbird/*.py
%{py3_sitescriptdir}/orca/scripts/apps/Thunderbird/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/evince
%{py3_sitescriptdir}/orca/scripts/apps/evince/*.py
%{py3_sitescriptdir}/orca/scripts/apps/evince/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/evolution
%{py3_sitescriptdir}/orca/scripts/apps/evolution/*.py
%{py3_sitescriptdir}/orca/scripts/apps/evolution/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/gajim
%{py3_sitescriptdir}/orca/scripts/apps/gajim/*.py
%{py3_sitescriptdir}/orca/scripts/apps/gajim/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/gedit
%{py3_sitescriptdir}/orca/scripts/apps/gedit/*.py
%{py3_sitescriptdir}/orca/scripts/apps/gedit/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/gnome-shell
%{py3_sitescriptdir}/orca/scripts/apps/gnome-shell/*.py
%{py3_sitescriptdir}/orca/scripts/apps/gnome-shell/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/kwin
%{py3_sitescriptdir}/orca/scripts/apps/kwin/*.py
%{py3_sitescriptdir}/orca/scripts/apps/kwin/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/notification-daemon
%{py3_sitescriptdir}/orca/scripts/apps/notification-daemon/*.py
%{py3_sitescriptdir}/orca/scripts/apps/notification-daemon/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/pidgin
%{py3_sitescriptdir}/orca/scripts/apps/pidgin/*.py
%{py3_sitescriptdir}/orca/scripts/apps/pidgin/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/smuxi-frontend-gnome
%{py3_sitescriptdir}/orca/scripts/apps/smuxi-frontend-gnome/*.py
%{py3_sitescriptdir}/orca/scripts/apps/smuxi-frontend-gnome/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/soffice
%{py3_sitescriptdir}/orca/scripts/apps/soffice/*.py
%{py3_sitescriptdir}/orca/scripts/apps/soffice/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/apps/xfwm4
%{py3_sitescriptdir}/orca/scripts/apps/xfwm4/*.py
%{py3_sitescriptdir}/orca/scripts/apps/xfwm4/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/sleepmode
%{py3_sitescriptdir}/orca/scripts/sleepmode/*.py
%{py3_sitescriptdir}/orca/scripts/sleepmode/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/switcher
%{py3_sitescriptdir}/orca/scripts/switcher/*.py
%{py3_sitescriptdir}/orca/scripts/switcher/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/terminal
%{py3_sitescriptdir}/orca/scripts/terminal/*.py
%{py3_sitescriptdir}/orca/scripts/terminal/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/toolkits
%{py3_sitescriptdir}/orca/scripts/toolkits/*.py
%{py3_sitescriptdir}/orca/scripts/toolkits/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/toolkits/Chromium
%{py3_sitescriptdir}/orca/scripts/toolkits/Chromium/*.py
%{py3_sitescriptdir}/orca/scripts/toolkits/Chromium/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/toolkits/Gecko
%{py3_sitescriptdir}/orca/scripts/toolkits/Gecko/*.py
%{py3_sitescriptdir}/orca/scripts/toolkits/Gecko/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/toolkits/J2SE-access-bridge
%{py3_sitescriptdir}/orca/scripts/toolkits/J2SE-access-bridge/*.py
%{py3_sitescriptdir}/orca/scripts/toolkits/J2SE-access-bridge/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/toolkits/Qt
%{py3_sitescriptdir}/orca/scripts/toolkits/Qt/*.py
%{py3_sitescriptdir}/orca/scripts/toolkits/Qt/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/toolkits/WebKitGTK
%{py3_sitescriptdir}/orca/scripts/toolkits/WebKitGTK/*.py
%{py3_sitescriptdir}/orca/scripts/toolkits/WebKitGTK/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/toolkits/gtk
%{py3_sitescriptdir}/orca/scripts/toolkits/gtk/*.py
%{py3_sitescriptdir}/orca/scripts/toolkits/gtk/__pycache__
%dir %{py3_sitescriptdir}/orca/scripts/web
%{py3_sitescriptdir}/orca/scripts/web/*.py
%{py3_sitescriptdir}/orca/scripts/web/__pycache__
%{_mandir}/man1/orca.1*
%{_sysconfdir}/xdg/autostart/orca-autostart.desktop
