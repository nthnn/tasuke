#!/bin/sh
#
# This file is part of the tasuke project (https://github.com/nthnn/tasuke).
# Copyright (c) 2024 Nathanne Isip.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

mkdir -p dist/tasuke_0.1.0-1_any/usr/bin
mkdir -p dist/tasuke_0.1.0-1_any/etc/tasuke/conf.d
mkdir -p dist/tasuke_0.1.0-1_any/tmp/tasuke
mkdir -p dist/tasuke_0.1.0-1_any/DEBIAN

touch dist/tasuke_0.1.0-1_any/DEBIAN/control
echo "Package: tasuke" >> dist/tasuke_0.1.0-1_any/DEBIAN/control
echo "Version: 0.1.0" >> dist/tasuke_0.1.0-1_any/DEBIAN/control
echo "Architecture: all" >> dist/tasuke_0.1.0-1_any/DEBIAN/control
echo "Maintainer: Nathanne Isip <nathanneisip@gmail.com>" >> dist/tasuke_0.1.0-1_any/DEBIAN/control
echo "Description: Customizable personal computer assistant with AI voice command recognition." >> dist/tasuke_0.1.0-1_any/DEBIAN/control

touch dist/tasuke_0.1.0-1_any/etc/tasuke/conf.d/commands.json
echo "[\r\n\t[\r\n\t\t[\"what's the date today\"],\r\n\t\t[\"Here's the date today\"],\r\n\t\t\"date\"\r\n\t]\r\n]" >> dist/tasuke_0.1.0-1_any/etc/tasuke/conf.d/commands.json

chmod +x tasuke.py
cp tasuke.py dist/tasuke_0.1.0-1_any/usr/bin/tasuke

cd dist
dpkg-deb --build tasuke_0.1.0-1_any
rm -rf tasuke_0.1.0-1_any
cd ..