# Script generated with Bloom
pkgdesc="ROS - ROS packages for the ROBOTIS MANIPULATOR-H (metapackage)"
url='http://wiki.ros.org/manipulator_h'

pkgname='ros-kinetic-manipulator-h'
pkgver='0.3.1_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-manipulator-h-base-module'
'ros-kinetic-manipulator-h-base-module-msgs'
'ros-kinetic-manipulator-h-bringup'
'ros-kinetic-manipulator-h-description'
'ros-kinetic-manipulator-h-gazebo'
'ros-kinetic-manipulator-h-gui'
'ros-kinetic-manipulator-h-kinematics-dynamics'
'ros-kinetic-manipulator-h-manager'
)

conflicts=()
replaces=()

_dir=manipulator_h
source=()
md5sums=()

prepare() {
    cp -R $startdir/manipulator_h $srcdir/manipulator_h
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

