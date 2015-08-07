Name:           ros-indigo-roslint
Version:        0.10.0
Release:        0%{?dist}
Summary:        ROS roslint package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roslint
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ros-indigo-catkin

%description
CMake lint commands for ROS packages. The lint commands perform static checking
of Python or C++ source code for errors and standards compliance.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Aug 07 2015 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.10.0-0
- Autogenerated by Bloom

* Tue Jan 06 2015 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.9.3-0
- Autogenerated by Bloom

