%define git 20210613

Summary:	Plasma 5 network samba drives
Name:		samba-mounter
Version:	0.1
Release:	0.%{git}.1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
Source0:	%{name}-%{git}.tar.bz2
Patch0:		samba-mounter-20210613-ru.patch
BuildRequires:	extra-cmake-modules
BuildRequires:	kf5auth-devel
BuildRequires:	kf5config-devel
BuildRequires:	kf5i18n-devel
BuildRequires:	kf5kcmutils-devel
BuildRequires:	kf5kio-devel
BuildRequires:	kf5solid-devel
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)

%description
Plasma 5 network samba drives.

%files -f kcm_sambamounter.lang
%{_kde5_applicationsdir}/sambamounter.desktop
%{_kde5_applicationsdir}/sambamounterapp.desktop
%{_kde5_bindir}/samba-onstart
%{_kde5_bindir}/samba-realmounter
%{_kde5_bindir}/samba-realumounter
%{_kde5_libexecdir}/kauth/samba_helper
%{_kde5_services}/sambamount.desktop
%{_kde5_sysconfdir}/xdg/autostart/sambamounter.desktop
%{_datadir}/polkit-1/actions/org.kde.sambamounter.policy
%{_datadir}/dbus-1/system-services/org.kde.sambamounter.service
%{_datadir}/dbus-1/system.d/org.kde.sambamounter.conf
%{_qt5_plugindir}/kcm_sambamount.so

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{git}
%patch0 -p1

%build
%cmake_kde5
%make

%install
%makeinstall_std -C build

%find_lang kcm_sambamounter
