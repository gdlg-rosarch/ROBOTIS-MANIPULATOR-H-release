# Script generated with Bloom
pkgdesc="ROS - The manipulator_h_manager package This package describes robot manager to execute manipulator_h_base_module."
url='http://wiki.ros.org/manipulator_h_manager'

pkgname='ros-kinetic-manipulator-h-manager'
pkgver='0.3.1_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-manipulator-h-base-module'
'ros-kinetic-robotis-controller'
'ros-kinetic-roscpp'
)

depends=('ros-kinetic-manipulator-h-base-module'
'ros-kinetic-robotis-controller'
'ros-kinetic-roscpp'
)

conflicts=()
replaces=()

_dir=manipulator_h_manager
source=()
md5sums=()

prepare() {
    cp -R $startdir/manipulator_h_manager $srcdir/manipulator_h_manager
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

