Name:           ros-indigo-urdfdom-py
Version:        0.3.0
Release:        2%{?dist}
Summary:        ROS urdfdom_py package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/urdf
Source0:        %{name}-%{version}.tar.gz

Requires:       python-devel
Requires:       python-lxml
Requires:       ros-indigo-catkin
BuildRequires:  python-catkin_pkg
BuildRequires:  python-devel
BuildRequires:  ros-indigo-catkin

%description
A library to access URDFs using the DOM model.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
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
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Dec 21 2014 Ioan Sucan <isucan@google.com> - 0.3.0-2
- Autogenerated by Bloom

