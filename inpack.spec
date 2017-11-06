[project]
name = java-jre
version = 1.8.0.151
vendor = oracle.com
homepage = http://www.oracle.com/technetwork/java/javase/downloads/index.html
groups = dev/sys-runtime
description = Java SE Development Kit

%build
PREFIX="{{.project__prefix}}"

cd {{.inpack__pack_dir}}/deps

if [ ! -f "jre-8u151-linux-x64.tar.gz" ]; then
    exit 1;
fi
if [ ! -d "jre1.8.0_151" ]; then
    tar -zxf jre-8u151-linux-x64.tar.gz
fi


cd jre1.8.0_151
chown -R action:action .
cp -rp bin  {{.buildroot}}/
cp -rp lib  {{.buildroot}}/
cp -rp COPYRIGHT  {{.buildroot}}/
cp -rp LICENSE  {{.buildroot}}/
cp -rp README  {{.buildroot}}/
cp -rp release  {{.buildroot}}/
cp -rp THIRDPARTYLICENSEREADME-JAVAFX.txt  {{.buildroot}}/
cp -rp THIRDPARTYLICENSEREADME.txt  {{.buildroot}}/

cd {{.inpack__pack_dir}}/deps
rm -rf jre1.8.0_151

%files
