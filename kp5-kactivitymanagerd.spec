%define		kdeplasmaver	5.11.2
%define		qtver		5.4.0
%define		kpname		kactivitymanagerd
Summary:	kactivitymanagerd
Name:		kp5-%{kpname}
Version:	5.11.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	9a9a6b0ef0e9d8740755c2efb3797091
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5X11Extras-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-khtml-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kactivitymanagerd

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kactivitymanagerd
%{_libdir}/libkactivitymanagerd_plugin.so
%dir %{_libdir}/qt5/plugins/kactivitymanagerd
%dir %{_libdir}/qt5/plugins/kactivitymanagerd/1
%{_libdir}/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_activitytemplates.so
%{_libdir}/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_eventspy.so
%{_libdir}/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_globalshortcuts.so
%{_libdir}/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_runapplication.so
%{_libdir}/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_slc.so
%{_libdir}/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_sqlite.so
%{_libdir}/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_virtualdesktopswitch.so
%{_datadir}/kservices5/kactivitymanagerd.desktop
%{_datadir}/kservicetypes5/kactivitymanagerd-plugin.desktop
