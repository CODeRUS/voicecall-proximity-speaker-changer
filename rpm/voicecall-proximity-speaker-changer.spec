# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       voicecall-proximity-speaker-changer

# >> macros
BuildArch: noarch
# << macros

Summary:    voicecall-proximity-speaker-changer
Version:    0.1
Release:    1
Group:      Qt/Qt
License:    TODO
URL:        http://example.org/
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager
Requires:   qt5-qtdeclarative-import-sensors

%description
Viocecall patch for automatically switching speaker by proximity sensor.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
mkdir -p %{buildroot}/usr/share/patchmanager/patches/
cp src/voicecall-proximity-speaker-changer %{buildroot}/usr/share/patchmanager/patches/
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches
# >> files
# << files
