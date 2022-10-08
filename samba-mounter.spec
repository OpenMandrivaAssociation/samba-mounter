%define git 20210613

Summary:	Plasma 5 network samba drives
Name:		samba-mounter
Version:	0.1
Release:	0.%{git}.2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://invent.kde.org/system/samba-mounter
Source0:	%{name}-%{git}.tar.bz2
BuildRequires:  cmake
BuildRequires:	extra-cmake-modules
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)

%description
Plasma 5 network samba drives.
#-f kcm_sambamounter.lang
%files 
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
%{_libdir}/qt5/plugins/kcm_sambamount.so

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{git}

%build
%cmake
%make_build

%install
%make_install -C build

%__mv %{buildroot}%{_libdir}/plugins %{buildroot}%{_libdir}/qt5/plugins

#find_lang kcm_sambamounter
