%define debug_package %{nil}
%define major %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kde-cli-tools
Version: 5.9.1
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
Requires: kinit

%description
KDE Plasma 5 CLI (Command Line Interface) Tools.

%prep
%setup -qn %{name}-%{major}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

# (tpg) use kdesu form KF5
ln -sf %{_libdir}/libexec/kf5/kdesu %{buildroot}%{_bindir}/kdesu

%find_lang filetypes || touch filetypes.lang
%find_lang kcmshell || touch kcmshell.lang
%find_lang kdesu || touch kdesu.lang
%find_lang kioclient || touch kioclient.lang
%find_lang kmimetypefinder || touch kmimetypefinder.lang
%find_lang kstart || touch kstart.lang
%find_lang ktraderclient || touch ktraderclient.lang
%find_lang kbroadcastnotification || touch kbroadcastnotification.lang

%files -f filetypes.lang,kcmshell.lang,kdesu.lang,kioclient.lang,kmimetypefinder.lang,kstart.lang,ktraderclient.lang,kbroadcastnotification.lang
%{_bindir}/kbroadcastnotification
%{_bindir}/kdesu
%{_bindir}/kcmshell5
%{_bindir}/kde-open5
%{_bindir}/kdecp5
%{_bindir}/kdemv5
%{_bindir}/keditfiletype5
%{_bindir}/kioclient5
%{_bindir}/kmimetypefinder5
%{_bindir}/kstart5
%{_bindir}/ksvgtopng5
%{_bindir}/ktraderclient5
%{_libdir}/libexec/kf5/kdeeject
%{_libdir}/libexec/kf5/kdesu
%{_libdir}/libkdeinit5_kcmshell5.so
%{_libdir}/qt5/plugins/kcm_filetypes.so
%{_datadir}/kservices5/*
%{_mandir}/man1/kdesu.1*
%doc %{_docdir}/HTML/*/kdesu
%doc %{_docdir}/HTML/*/kcontrol5/filetypes
