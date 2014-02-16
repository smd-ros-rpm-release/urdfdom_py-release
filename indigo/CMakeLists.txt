cmake_minimum_required(VERSION 2.8.3)
project(urdfdom_py)

find_package(catkin)
catkin_python_setup()
catkin_package()

install(PROGRAMS
  urdf_parser_py/scripts/display_urdf
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
  )
