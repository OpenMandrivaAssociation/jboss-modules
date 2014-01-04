%{?_javapackages_macros:%_javapackages_macros}
%global namedreltag .Beta3
%global namedversion %{version}%{?namedreltag}

Name:             jboss-modules
Version:          1.3.0
Release:          0.1%{namedreltag}.0%{?dist}
Summary:          A Modular Classloading System
License:          LGPLv2+
URL:              https://github.com/jbossas/jboss-modules
Source0:          https://github.com/jbossas/jboss-modules/archive/%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    jboss-parent
BuildRequires:    shrinkwrap
%if 0%{?fedora}
BuildRequires:    apiviz
%endif

%description
Ths package contains A Modular Classloading System.

%package javadoc
Summary:          Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-modules-%{namedversion}

# Conditionally remove dependency on apiviz
if [ %{?rhel} ]; then
    %pom_remove_plugin :maven-javadoc-plugin
fi

# Tries to connect to remote host
rm src/test/java/org/jboss/modules/MavenResourceTest.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Sep 12 2013 Marek Goldmann <mgoldman@redhat.com> - 1.3.0-0.1.Beta3
- Upstream release 1.3.0.Beta3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 18 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-2
- Remove unneeded BR

* Tue Jun 04 2013 Marek Goldmann <mgoldman@redhat.com> - 1.2.1-1
- Upstream release 1.2.1.Final
- New guidelines

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.1.1-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Sep  3 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.1-7
- Conditionally remove dependency on apiviz

* Mon Sep  3 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.1-6
- Remove unneeded BR: maven-injection-plugin

* Fri Jul 20 2012 Marek Goldmann <mgoldman@redhat.com> 1.1.1-4
- Fixed BR

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 05 2012 Marek Goldmann <mgoldman@redhat.com> 1.1.1-3
- Patch to fix MODULES-128

* Thu Feb 23 2012 Marek Goldmann <mgoldman@redhat.com> 1.1.1-2
- Relocated jars to _javadir

* Sun Feb 19 2012 Marek Goldmann <mgoldman@redhat.com> 1.1.1-1
- Upstream release 1.1.1.GA

* Thu Jan 26 2012 Marek Goldmann <mgoldman@redhat.com> 1.1.0-0.3.CR8
- Upstream release 1.1.0.CR8

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.2.CR4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 02 2011 Marek Goldmann <mgoldman@redhat.com> 1.1.0-0.1.CR4
- Upstream release 1.1.0.CR4

* Tue Aug 02 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.2-1
- Initial packaging

