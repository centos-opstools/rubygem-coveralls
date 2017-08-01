# Generated from coveralls-0.8.15.gem by gem2rpm -*- rpm-spec -*-
%global gem_name coveralls

Name: rubygem-%{gem_name}
Version: 0.8.15
Release: 1%{?dist}
Summary: A Ruby implementation of the Coveralls API
Group: Development/Languages
License: MIT
URL: https://coveralls.io
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.8.7
Requires: rubygem(json) >= 1.8
Requires: rubygem(json) < 3
Requires: rubygem(simplecov) >= 0.12.0
Requires: rubygem(simplecov) < 0.13
Requires: rubygem(term-ansicolor) >= 1.3
Requires: rubygem(term-ansicolor) < 2
Requires: rubygem(thor) >= 0.19.1
Requires: rubygem(thor) < 0.20
Requires: rubygem(tins) >= 1.6.0
Requires: rubygem(tins) < 2
# the following BuildRequires are development dependencies
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A Ruby implementation of the Coveralls API.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{_bindir}/coveralls
%exclude %{gem_instdir}/.gitignore
%{gem_instdir}/.rspec
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/coveralls-ruby.gemspec
%{gem_instdir}/spec

%changelog
* Thu Sep 29 2016 Rich Megginson <rmeggins@redhat.com> - 0.8.15-1
- Initial package
