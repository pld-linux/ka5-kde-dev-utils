%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		kde-dev-utils
Summary:	Kde dev utils
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	176d804ba28e384d7d90d6d7461d0213
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kparts-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small utilities for developers using KDE/Qt libs/frameworks.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpartloader
%attr(755,root,root) %{_bindir}/kuiviewer
%attr(755,root,root) %{_libdir}/qt5/plugins/kuiviewerpart.so
%attr(755,root,root) %{_libdir}/qt5/plugins/quithumbnail.so
%{_desktopdir}/org.kde.kuiviewer.desktop
%{_iconsdir}/hicolor/128x128/apps/kuiviewer.png
%{_iconsdir}/hicolor/16x16/apps/kuiviewer.png
%{_iconsdir}/hicolor/32x32/apps/kuiviewer.png
%{_iconsdir}/hicolor/48x48/apps/kuiviewer.png
%{_iconsdir}/hicolor/64x64/apps/kuiviewer.png
%{_iconsdir}/hicolor/scalable/apps/kuiviewer.svg
%{_datadir}/kservices5/designerthumbnail.desktop
%{_datadir}/kservices5/kuiviewer_part.desktop
%{_datadir}/kxmlgui5/kpartloader
%{_datadir}/kxmlgui5/kuiviewer
%{_datadir}/kxmlgui5/kuiviewerpart
