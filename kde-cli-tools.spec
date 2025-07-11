%define major %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name: kde-cli-tools
Version: 6.4.2
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/plasma/kde-cli-tools/-/archive/%{gitbranch}/kde-cli-tools-%{gitbranchd}.tar.bz2#/kde-cli-tools-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{major}/kde-cli-tools-%{version}.tar.xz
%endif
Summary: KDE Plasma 6 CLI (Command Line Interface) Tools
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6Su)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(PlasmaActivities)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6Parts)
BuildRequires: %mklibname -d KF6IconWidgets
BuildRequires: gettext
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
# Renamed 2025-05-02 after 6.0
%rename plasma6-kde-cli-tools

%description
KDE Plasma 6 CLI (Command Line Interface) Tools.

%files -f %{name}.lang
%{_bindir}/kbroadcastnotification
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
%{_bindir}/plasma-open-settings
%{_bindir}/kde-open
%{_bindir}/kdecp
%{_bindir}/kdemv
%{_bindir}/keditfiletype
%{_bindir}/kioclient
%{_bindir}/kmimetypefinder
%{_bindir}/kstart
%{_bindir}/ksvgtopng
%{_libdir}/libexec/kf6/kdeeject
%{_libdir}/libexec/kf6/kdesu
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_filetypes.so
%{_datadir}/applications/kcm_filetypes.desktop
%{_datadir}/applications/org.kde.keditfiletype.desktop
%{_datadir}/applications/org.kde.plasma.settings.open.desktop
%{_mandir}/man1/kdesu.1*
%{_datadir}/zsh/site-functions/_kde-inhibit
