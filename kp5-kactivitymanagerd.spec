%define		kdeplasmaver	5.23.1
%define		qtver		5.9.0
%define		kpname		kactivitymanagerd
Summary:	kactivitymanagerd
Name:		kp5-%{kpname}
Version:	5.23.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	f96f611119d551399297074fc1f882f9
URL:		http://www.kde.org/
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Sql-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5X11Extras-devel >= %{qtver}
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-kglobalaccel-devel
BuildRequires:	kf5-khtml-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	qt5-qmake
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
System service to manage user's activities, track the usage patterns
etc.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/kactivitymanagerd
%{_libdir}/libkactivitymanagerd_plugin.so
%dir %{_libdir}/qt5/plugins/kactivitymanagerd
%dir %{_libdir}/qt5/plugins/kactivitymanagerd/1
%attr(755,root,root) %{_libdir}/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_activitytemplates.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_eventspy.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_globalshortcuts.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_runapplication.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_slc.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_sqlite.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_virtualdesktopswitch.so
%{_datadir}/kservices5/kactivitymanagerd.desktop
%{_datadir}/kservicetypes5/kactivitymanagerd-plugin.desktop
%{systemduserunitdir}/plasma-kactivitymanagerd.service
%attr(755,root,root) %{_libdir}/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_gtk_eventspy.so
%{_datadir}/dbus-1/services/org.kde.ActivityManager.service
%{_datadir}/qlogging-categories5/kactivitymanagerd.categories
%attr(755,root,root) %{_libdir}/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_activityrunner.so
%{_datadir}/krunner/dbusplugins/plasma-runnners-activities.desktop
