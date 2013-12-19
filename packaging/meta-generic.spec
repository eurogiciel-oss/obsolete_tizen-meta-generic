%define profile generic

Summary:	Generic Meta Data
Name:		meta-generic
Version:	001
Release:	1
BuildArch:  noarch
License:	GPL-2.0
Group:		Base/Configuration
URL:		http://www.tizen.org
Source:		%{name}-%{version}.tar.bz2

%description
Generic Meta Data.
Includes patterns and image configurations for Generic images.

%prep
%setup -q

%build
make

%install
%make_install


%files
%attr(644,-,-) %{_datadir}/package-groups/%{profile}/*.yaml
%{_datadir}/image-configurations/%{profile}/*.yaml
%{_datadir}/image-configurations/%{profile}/configs/*.yaml
%{_datadir}/image-configurations/%{profile}/partitions
%{_datadir}/image-configurations/%{profile}/scripts
