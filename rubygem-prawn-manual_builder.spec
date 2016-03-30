#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-prawn-manual_builder
Version  : 0.2.0
Release  : 6
URL      : https://rubygems.org/downloads/prawn-manual_builder-0.2.0.gem
Source0  : https://rubygems.org/downloads/prawn-manual_builder-0.2.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : Ruby
BuildRequires : ruby
BuildRequires : rubygem-coderay
BuildRequires : rubygem-rdoc

%description
# Prawn::ManualBuilder
This library is used by Prawn to generate its self-documenting manual,
and could be used by third-party Prawn extensions to create manuals
for their functionality as well.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n prawn-manual_builder-0.2.0
gem spec %{SOURCE0} -l --ruby > rubygem-prawn-manual_builder.gemspec

%build
gem build rubygem-prawn-manual_builder.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
prawn-manual_builder-0.2.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/prawn-manual_builder-0.2.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/prawn-manual_builder-0.2.0/COPYING
/usr/lib64/ruby/gems/2.3.0/gems/prawn-manual_builder-0.2.0/GPLv2
/usr/lib64/ruby/gems/2.3.0/gems/prawn-manual_builder-0.2.0/GPLv3
/usr/lib64/ruby/gems/2.3.0/gems/prawn-manual_builder-0.2.0/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/prawn-manual_builder-0.2.0/README.md
/usr/lib64/ruby/gems/2.3.0/gems/prawn-manual_builder-0.2.0/data/fonts/DejaVuSans.ttf
/usr/lib64/ruby/gems/2.3.0/gems/prawn-manual_builder-0.2.0/data/fonts/Dustismo_Roman.ttf
/usr/lib64/ruby/gems/2.3.0/gems/prawn-manual_builder-0.2.0/data/fonts/gkai00mp.ttf
/usr/lib64/ruby/gems/2.3.0/gems/prawn-manual_builder-0.2.0/lib/prawn/manual_builder.rb
/usr/lib64/ruby/gems/2.3.0/gems/prawn-manual_builder-0.2.0/lib/prawn/manual_builder/example.rb
/usr/lib64/ruby/gems/2.3.0/gems/prawn-manual_builder-0.2.0/lib/prawn/manual_builder/example_file.rb
/usr/lib64/ruby/gems/2.3.0/gems/prawn-manual_builder-0.2.0/lib/prawn/manual_builder/example_package.rb
/usr/lib64/ruby/gems/2.3.0/gems/prawn-manual_builder-0.2.0/lib/prawn/manual_builder/example_section.rb
/usr/lib64/ruby/gems/2.3.0/gems/prawn-manual_builder-0.2.0/lib/prawn/manual_builder/syntax_highlight.rb
/usr/lib64/ruby/gems/2.3.0/specifications/prawn-manual_builder-0.2.0.gemspec
