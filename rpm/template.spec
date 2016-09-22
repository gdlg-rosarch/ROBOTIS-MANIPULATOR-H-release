Name:           ros-kinetic-manipulator-h-gui
Version:        0.2.1
Release:        0%{?dist}
Summary:        ROS manipulator_h_gui package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/ROBOTIS-MANIPULATOR-H
Source0:        %{name}-%{version}.tar.gz

Requires:       qt-devel
Requires:       ros-kinetic-cmake-modules
Requires:       ros-kinetic-eigen-conversions
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-qt-build
Requires:       ros-kinetic-roscpp
BuildRequires:  qt-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cmake-modules
BuildRequires:  ros-kinetic-eigen-conversions
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-manipulator-h-base-module-msgs
BuildRequires:  ros-kinetic-qt-build
BuildRequires:  ros-kinetic-robotis-controller-msgs
BuildRequires:  ros-kinetic-roscpp

%description
The manipulator_h_gui package This package provides simple GUI to control
ROBOTIS MANIPULATOR-H. This GUI is connected to manipulator_h_base_module.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Sep 22 2016 pyo <pyo@robotis.com> - 0.2.1-0
- Autogenerated by Bloom

* Fri Aug 19 2016 pyo <pyo@robotis.com> - 0.2.0-0
- Autogenerated by Bloom

