%define debug_package %{nil}
%define major %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kde-cli-tools
Version: 5.1.95
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/plasma/%{major}/%{name}-%{version}.tar.xz
Source1000: %{name}.rpmlintrc
Summary: KDE Plasma 5 CLI (Command Line Interface) Tools
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5Su)
BuildRequires: cmake(KF5KDE4Support)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5ItemModels)
BuildRequires: cmake(KF5Init)
BuildRequires: ninja

%description
KDE Plasma 5 CLI (Command Line Interface) Tools

%prep
%setup -qn %{name}-%{major}
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install
%find_lang filetypes
%find_lang kcmshell
%find_lang kdesu
%find_lang kioclient
%find_lang kmimetypefinder
%find_lang kstart
%find_lang ktraderclient

%files -f filetypes.lang,kcmshell.lang,kdesu.lang,kioclient.lang,kmimetypefinder.lang,kstart.lang,ktraderclient.lang
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
%{_libdir}/libexec/kdeeject
%{_libdir}/libexec/kdesu
%{_libdir}/libkdeinit5_kcmshell5.so
%{_libdir}/qt5/plugins/kcm_filetypes.so
%{_datadir}/kservices5/*
%{_mandir}/man1/kdesu.1*
%doc %{_docdir}/HTML/en/kdesu
