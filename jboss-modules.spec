%bcond_with javadoc

Name:             jboss-modules
Version:          2.3.0
Release:          1
Summary:          A Modular Classloading System
Group:            Development/Java
License:          LGPLv2+
URL:              https://github.com/jboss-modules/jboss-modules
Source0:          https://github.com/jboss-modules/jboss-modules/archive/refs/tags/%{version}.tar.gz

BuildArch:        noarch
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven

BuildRequires:    jboss-parent

%description
Ths package contains A Modular Classloading System.

%if %{with javadoc}
%package javadoc
Summary:          Javadocs for %{name}

%endif
%if %{with javadoc}
%description javadoc
This package contains the API documentation for %{name}.

%endif
%prep
%setup -q -n jboss-modules-%{version}

# Tries to connect to a remote host. Tests are skipped, but Maven still
# parses the file if it is left on the compile path of a test-jar goal.
rm -f src/test/java/org/jboss/modules/MavenResourceTest.java

%files -f .mfiles

%if %{with javadoc}
%files javadoc -f .mfiles-javadoc

%endif
