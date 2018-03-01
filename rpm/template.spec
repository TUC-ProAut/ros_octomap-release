Name:           ros-lunar-octomap-pa
Version:        1.3.3
Release:        0%{?dist}
Summary:        ROS octomap_pa package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       pcl
Requires:       pcl-tools
Requires:       ros-lunar-geometry-msgs
Requires:       ros-lunar-laser-geometry
Requires:       ros-lunar-message-runtime
Requires:       ros-lunar-nav-msgs
Requires:       ros-lunar-octomap-msgs
Requires:       ros-lunar-octomap-ros
Requires:       ros-lunar-parameter-pa
Requires:       ros-lunar-pcl-conversions
Requires:       ros-lunar-pcl-ros
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-sensor-msgs
Requires:       ros-lunar-std-msgs
Requires:       ros-lunar-std-srvs
Requires:       ros-lunar-tf
BuildRequires:  pcl-devel
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-geometry-msgs
BuildRequires:  ros-lunar-laser-geometry
BuildRequires:  ros-lunar-message-generation
BuildRequires:  ros-lunar-nav-msgs
BuildRequires:  ros-lunar-octomap-msgs
BuildRequires:  ros-lunar-octomap-ros
BuildRequires:  ros-lunar-parameter-pa
BuildRequires:  ros-lunar-pcl-conversions
BuildRequires:  ros-lunar-pcl-ros
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-sensor-msgs
BuildRequires:  ros-lunar-std-msgs
BuildRequires:  ros-lunar-std-srvs
BuildRequires:  ros-lunar-tf

%description
ProAut octomap package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Thu Mar 01 2018 Peter Weissig <wepet@hrz.tu-chemnitz.de> - 1.3.3-0
- Autogenerated by Bloom

* Sun Feb 25 2018 Peter Weissig <wepet@hrz.tu-chemnitz.de> - 1.2.2-0
- Autogenerated by Bloom

* Mon Feb 19 2018 Peter Weissig <wepet@hrz.tu-chemnitz.de> - 1.2.1-0
- Autogenerated by Bloom

* Sat Feb 17 2018 Peter Weissig <wepet@hrz.tu-chemnitz.de> - 1.2.0-0
- Autogenerated by Bloom

