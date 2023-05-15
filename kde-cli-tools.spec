%define major %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kde-cli-tools
Version: 5.27.5.1
Release: 1
Source0: http://download.kde.org/%{stable}/plasma/%{major}/%{name}-%{version}.tar.xz
Source1000: %{name}.rpmlintrc
Summary: KDE Plasma 5 CLI (Command Line Interface) Tools
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xext)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5Su)
BuildRequires: cmake(KF5KDE4Support)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5ItemModels)
BuildRequires: cmake(KF5Init)
BuildRequires: cmake(KF5Activities)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(LibKWorkspace)
Requires: kinit

%description
KDE Plasma 5 CLI (Command Line Interface) Tools.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

# (tpg) use kdesu form KF5
ln -sf %{_libdir}/libexec/kf5/kdesu %{buildroot}%{_bindir}/kdesu

%find_lang %{name} --all-name --with-html --with-man

%files -f %{name}.lang
%{_bindir}/kbroadcastnotification
%{_bindir}/kdesu
%{_bindir}/kcmshell5
%{_bindir}/kde-inhibit
%{_bindir}/kde-open5
%{_bindir}/kdecp5
%{_bindir}/kdemv5
%{_bindir}/keditfiletype5
%{_bindir}/kinfo
%{_bindir}/kioclient5
%{_bindir}/kmimetypefinder5
%{_bindir}/kstart5
%{_bindir}/ksvgtopng5
%{_bindir}/ktraderclient5
%{_bindir}/plasma-open-settings
%{_bindir}/kde-open
%{_bindir}/kdecp
%{_bindir}/kdemv
%{_bindir}/keditfiletype
%{_bindir}/kioclient
%{_bindir}/kmimetypefinder
%{_bindir}/kstart
%{_bindir}/ksvgtopng
%{_libdir}/libexec/kf5/kdeeject
%{_libdir}/libexec/kf5/kdesu
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_filetypes.so
%{_datadir}/applications/kcm_filetypes.desktop
%{_datadir}/applications/org.kde.keditfiletype.desktop
%{_datadir}/applications/org.kde.plasma.settings.open.desktop
%{_mandir}/man1/kdesu.1*
