[project]
name = java-jre
version = 1.8.0.151
release = 4
vendor = oracle.com
homepage = http://www.oracle.com/technetwork/java/javase/downloads/index.html
groups = dev/sys-runtime
description = Java SE Development Kit

%build

cd {{.inpack__pack_dir}}/deps

if [ ! -f "jre-8u151-linux-x64.tar.gz" ]; then
    exit 1;
fi
if [ ! -d "jre1.8.0_151" ]; then
    tar -zxf jre-8u151-linux-x64.tar.gz
fi

mkdir -p {{.buildroot}}/misc

cd jre1.8.0_151
cp -rp bin  {{.buildroot}}/
cp -rp lib  {{.buildroot}}/
cp -rp COPYRIGHT  {{.buildroot}}/
cp -rp LICENSE  {{.buildroot}}/
cp -rp README  {{.buildroot}}/
cp -rp release  {{.buildroot}}/
cp -rp THIRDPARTYLICENSEREADME-JAVAFX.txt  {{.buildroot}}/
cp -rp THIRDPARTYLICENSEREADME.txt  {{.buildroot}}/
install -m 775 {{.inpack__pack_dir}}/misc/inner-init.sh {{.buildroot}}/inner-init.sh
cp -rp {{.inpack__pack_dir}}/misc/profile.d_java.sh  {{.buildroot}}/misc/profile.d_java.sh

cd {{.inpack__pack_dir}}/deps
rm -rf jre1.8.0_151

%files
