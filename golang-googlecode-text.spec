# http://github.com/golang/text
%global forgeurl        https://github.com/golang/text
%global goipath         golang.org/x/text
Version:                0.3.0

%gometa

%global x_provider      golang
%global x_provider_tld  org
%global x_repo          text
%global x_goipath   %{x_provider}.%{x_provider_tld}/x/%{x_repo}
%global x_name          golang-%{x_provider}%{x_provider_tld}-%{x_repo}

%global devel_main      %{x_name}-devel
%global devel_prefix    x

Name:       golang-googlecode-text
Release:    1%{?dist}
Summary:    Supplementary Go text libraries
License:    BSD
URL:        %{gourl}
Source0:    %{gosource}

%description
%{summary}

%package -n %{x_name}-devel
Summary:    Supplementary Go text libraries for golang.org/x/ imports
BuildArch:  noarch

%description -n %{x_name}-devel

This package contains library source intended for building other packages
which use the supplementary Go text libraries with golang.org/x/ imports.

%prep
%forgesetup

%install
%goinstall

%check
%gochecks -d currency -d unicode/norm

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files -n %{x_name}-devel -f devel.file-list
%license LICENSE
%doc AUTHORS CONTRIBUTORS PATENTS README.md

%changelog
* Sat Oct 27 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.0-1
- Update to release 0.3.0

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.26.git3bd178b
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.25.git3bd178b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.24.git3bd178b
- Fix typo in package name

* Thu Mar 15 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.23.git3bd178b
- Update to spec 3.0
- Fix test error reported by go1.10

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22.git3bd178b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 24 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.21.git3bd178b
- Bump to upstream 3bd178b88a8180be2df394a1fbb81313916f0e7b
  related: #1254601

* Fri Aug 11 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0-0.20.git65f4f82
- Bump to upstream 65f4f820a7954b82e5c9325e1e088a4fda098f36
- related: #1254601

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.git04b8648
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.git04b8648
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.git04b8648
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.16.git04b8648
- Bump to upstream 04b8648d973c126ae60143b3e1473bc1576c7597
  related: #1254601

* Wed Dec 14 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.15.git6fc2e00
- Polish the spec file
  related: #1254601

* Wed Aug 10 2016 jchaloup <jchaloup@redhat.com> - 0-0.14.git6fc2e00
- skip currency test on aarch64 (binaries have different size)
  resolves: #1365814

* Wed Jul 27 2016 jchaloup <jchaloup@redhat.com> - 0-0.13.git6fc2e00
- skip currency test on s390x (binaries have different size)
  resolves: #1360388

* Mon Jul 25 2016 jchaloup <jchaloup@redhat.com> - 0-0.12.git6fc2e00
- Polishing the spec file
  related: #1254601

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.11.git6fc2e00
- https://fedoraproject.org/wiki/Changes/golang1.7

* Tue Feb 23 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0-0.10.git6fc2e00
- License and arch definition cleanup

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.git6fc2e00
- https://fedoraproject.org/wiki/Changes/golang1.6

* Fri Feb 19 2016 jchaloup <jchaloup@redhat.com> - 0-0.8.git6fc2e00
- Bump to upstream 6fc2e00a0d64b1f7fc1212dae5b0c939cf6d9ac4
  Repository has moved from code.google.com/p/go.text to github.com/golang/text
  related: #1254601

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.hg5b2527008a4c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 20 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.hg5b2527008a4c
- Choose the correct devel subpackage
  related: #1254601

* Thu Aug 20 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.hg5b2527008a4c
- Update spec file to spec-2.0
  resolves: #1254601

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.hg5b2527008a4c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 09 2014 jchaloup <jchaloup@redhat.com> - 0-0.3.hg5b2527008a4c
- Update to the latest commit 5b2527008a4c8988ca9dc6f010ebfb9dae67150b
  related: #1056285

* Fri Nov 21 2014 jchaloup <jchaloup@redhat.com> - 0-0.2.hg024681b033be
- Extend import paths for golang.org/x/
- Choose the correct architecture
  related: #1056285

* Sun Sep 28 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.1.hg024681b033be
- Resolves: rhbz#1056285 - Initial package
