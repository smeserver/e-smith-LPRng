# $Id: e-smith-LPRng.spec,v 1.7 2008/10/07 18:43:04 slords Exp $

Summary: e-smith server and gateway - LPRng module
%define name e-smith-LPRng
Name: %{name}
%define version 2.2.0
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
Requires: e-smith-base, LPRng
Requires: e-smith-lib >= 1.15.1-19
Requires: e-smith-formmagick >= 1.4.0-12
BuildRequires: e-smith-devtools >= 1.13.1-03
BuildArchitectures: noarch
AutoReqProv: no

%description
e-smith server and gateway software - LPRng module.
Add printing features, using the LPRng package.

%changelog
* Tue Oct 7 2008 Shad L. Lords <slords@mail.com> 2.2.0-1.sme
- Roll new stream to separate sme7/sme8 trees [SME: 4633]

* Sun Apr 27 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.14.0-9
- Add common <base> tags to e-smith-formmagick's general [SME: 4291]

* Wed Mar 12 2008 Shad L. Lords <slords@mail.com> 1.14.0-8
- Cleanup CREATE/ADD tag mixup [SME: 4045]

* Wed Feb 13 2008 Stephen Noble <support@dungog.net> 1.14.0-7
- Remove <base> tags now in general [SME: 3920]

* Tue Jan 08 2008 Stephen Noble <support@dungog.net> 1.14.0-6
- Warn not to use bad terms on Add Printer page [SME: 3667]

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Fri Apr 06 2007 Shad L. Lords <slords@mail.com> 1.14.0-5
- Remove duplicate papd.conf fragment. [SME: 1026]

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Wed Apr 19 2006 Charlie Brady <charlie_brady@mitel.com> 1.14.0-03
- Run printer-create during bootstrap-console-save, to ensure that
  spools exist after restore. [SME: 1280]

* Sat Apr  8 2006 Charlie Brady <charlieb@e-smith.com> 1.14.0-02
- Respect UseClientDriver property in smb.conf template fragment.
  [SME: 1216]

* Thu Mar 16 2006 Gordon Rowell <gordonr@gormand.com.au> 1.14.0-01
- Roll stable stream version. [SME: 1016]

* Tue Dec 20 2005 Gordon Rowell <gordonr@gormand.com.au> 1.13.3-09
- Revert last patch - not required for supervised services [SME: 351]

* Tue Dec 20 2005 Gordon Rowell <gordonr@gormand.com.au> 1.13.3-08
- And add lpd shutdown links [SME: 351]

* Tue Dec 20 2005 Gordon Rowell <gordonr@gormand.com.au> 1.13.3-07
- Redo -06 with missed patch from -03 [SME: 351]

* Tue Dec 20 2005 Gordon Rowell <gordonr@gormand.com.au> 1.13.3-06
- Create rc?.d and /service symlinks [SME: 351]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.13.3-05
- Bump release number only

* Mon Nov 21 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.3-04]
- Add /etc/atalk/papd.conf/20printers template (moved from e-smith-netatalk).
  [SF: 1361338]

* Mon Nov 21 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.3-03]
- Fix spec file formatting error, resulting in last patch being omitted.
  Move service startup symlink creation into createlinks script.
  [SF: 1362872]

* Wed Nov 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.3-02]
- Use sigterm to reconfigure lpd, since sighup doesn't seem to work reliably.
  [SF: 1358283]

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.13.3-01]
- Remove L10Ns from base packages [SF: 1309520]

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.13.2-01]
- New dev stream before relocating L10Ns

* Fri Sep 30 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-13]
- Added Italian L10N - Thanks Filippo Carletti [SF: 1309266]

* Mon Sep 26 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.13.1-12]
- Added German L10N - Thanks Dietmar Berteld [SF: 1293325]

* Fri Aug 26 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-11]
- Fix template expansion of /etc/printcap. [SF: 1273768]
- Remove unused and deprecated code from printer-{create,delete}.

* Tue Jul 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-10]
- Update to current db access APIs. Patch by Shad Lords. [SF: 1216546]

* Thu Mar 17 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-09]
- Add missing /etc/e-smith/template.metadata tree (which handles
  the lpd.perms relocation, without moving the template files).

* Wed Mar 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-08]
- Replace all LPRng-restart actions with call to 'adjust-services'.
  Use signhup rather than restart - supported by new LPRng.
  [MN00065576]
- Use generic_template_expand action in place of LPRng-conf.
  [MN00064130]
- Relocate /etc/lpd.perms to /etc/lpd/lpd.perms
- Remove obsolete printer-create-spool event directory

* Wed Dec 29 2004 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-07]
- Add down file, take II. This time for sure, Rocky! [MN00061223]

* Fri Dec 24 2004 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-06]
- Add down file so that supervised lpd stays down until started
  by rc7.d symlink. [MN00061223]

* Fri Dec 24 2004 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-05]
- Use /etc/rc.d/init.d, not /etc/init.d (which is a symlink) [MN00061223]

* Thu Dec 16 2004 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-04]
- Add missing execute permission for lpd run script [charlieb MN00061223]

* Thu Dec 16 2004 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-03]
- Fix /etc/init.d/supervise/lpd symlink path [charlieb MN00061223]

* Mon Dec 13 2004 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-02]
- Run lpd under supervise. [charlieb MN00061223]

* Mon Dec 13 2004 Charlie Brady <charlieb@e-smith.com>
- [1.13.1-01]
- New development stream - 1.13.1

* Tue Jul  6 2004 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-02]
- s/get/prop in LPRng-restart. [msoulier MN00036163]

* Thu Jan 22 2004 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-01]
- rolling to dev - 1.13.0

* Thu Jan 22 2004 Michael Soulier <msoulier@e-smith.com>
- [1.12.0-01]
- rolling to stable - 1.12.0

* Tue Jan  6 2004 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-06]
- Added 6.0 styling to printer panel. [msoulier 10876]

* Tue Nov 25 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-05]
- Added "use client driver" option to smb.conf. [msoulier 10623]

* Thu Aug 28 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-04]
- Check for enabled status before trying to restart.
  [charlieb 9861]

* Tue Aug 19 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-03]
- Replace LPRng-conf-startup action with default db fragments.
  [charlieb 9553]

* Tue Aug 19 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-02]
- Expand /etc/printcap unconditionally. [charlieb 9199]

* Tue Aug 19 2003 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-01]
- Changing version to development stream number - 1.11.0

* Wed Jul 16 2003 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-02]
- Remove obsolete printer-migrate action. [charlieb 9367]
- s/Copyright/License/ in RPM header.

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-01]
- Changing version to stable stream number - 1.10.0

* Tue Jun 24 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-20]
- Spanish nav bar [gordonr 9153]

* Tue May  6 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-19]
- Add Spanish lexicon for printers [lijied 3793]

* Thu Apr 24 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-18]
- Change button name "Add Printer" to "Add printer" [lijied 8491]

* Wed Apr 16 2003 Tony Clayton <apc@e-smith.com>
- [1.9.0-17]
- Remove module-load-usb-printer action and local event references [tonyc 6556]

* Tue Apr  8 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-16]
- Standardize the button name [lijied 7921]

* Fri Apr  4 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-15]
- Changed $q->table to $q->start_table where necessary [lijied 8034]

* Thu Mar 27 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-14]
- Modified French lexicon to use lang="fr", rename the lexicon
  directory to fr [lijied 6787] 
 
* Mon Mar 17 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-13]
- Deleted empty template-end files,
  deleted inappropariate template-begin files [lijied 3295]

* Thu Mar  6 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-12]
- Modified printers panel order [lijied 7356]

* Tue Mar  4 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-11]
- Split en-us lexicon from printer panel [lijied 4030]

* Mon Mar  3 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-10]
- Added French lexicon for printers. [lijied 5003]

* Sat Jan 25 2003 Mike Dickson <miked@e-smith.com>
- [1.9.0-09]
- added lexicon tag for 'Action' [miked 6363]

* Thu Jan  2 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-08]
- And add LPRng-conf-startup here [gordonr 5509]

* Thu Jan  2 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-07]
- And add the lpd startup here [gordonr 5509]

* Thu Jan  2 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-06]
- Split lpd startup from e-smith-base [gordonr 5509]

* Fri Dec 27 2002 Mike Dickson <miked@e-smith.com>
- [1.9.0-05]
- minor UI update [miked 5494]

* Mon Dec 16 2002 Mike Dickson <miked@e-smith.com>
- [1.9.0-04]
- UI Update, part of the tweaking for the new UI [miked 5494]

* Mon Dec  2 2002 Mike Dickson <miked@e-smith.com>
- [1.9.0-03]
- ui update  [miked 5494]

* Thu Nov 21 2002 Mike Dickson <miked@e-smith.com>
- [1.9.0-02]
- update to new UI system [miked 5494]

* Thu Nov  7 2002 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-01]
- Roll development stream to 1.9.0

* Fri Nov  1 2002 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-02]
- Try to load low level USB drivers before loading printer module.
  [charlieb 5288]

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-01]
- Rolling stable version number to 1.8.0

* Wed Oct  2 2002 Mark Knox <markk@e-smith.com>
- [1.7.3-04]
- Removed stray braces from templates [markk 3786]

* Mon Sep 23 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.3-03]
- Fix a problem with the "deprecate split" template re-ord. [charlieb 3786]

* Tue Sep 10 2002 Mark Knox <markk@e-smith.com>
- [1.7.3-02]
- Remove deprecated split on pipe [markk 3786]

* Fri Aug 30 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.3-01]
- Fixed typo in "Hostname of IP address" [gordonr 4750]

* Mon Aug 26 2002 Mark Knox <markk@e-smith.com>
- [1.7.2-01]
- Limit name and description fields to 32 chars for Appletalk [markk 4322]

* Fri Aug  2 2002 Tony Clayton <apc@e-smith.com>
- [1.7.1-01]
- change if(scalar %printers) to if(keys %printers) as a workaround to
  perl-5.6.1 bug with tied hashes [tonyc 4537]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-01]
- Changing version to maintained stream number to 1.7.0

* Tue May 28 2002 Kirrily Robert <skud@e-smith.com>
- [1.6.7-01]
- remoteaddress field now checked for valid hostname/ip [skud 3691]

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.6.5-01]
- RPM rebuild forced by cvsroot2rpm

* Wed May  1 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.6.4-01]
- esmith::AccountDB -> esmith::AccountsDB [schwern 3287]

* Mon Apr 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.6.3-01]
- Language en->en-us

* Thu Apr 11 2002 Mark Knox <markk@e-smith.com>
- [1.6.2-01]
- Converted all code to FormMagick panel and placed it in 
  esmith::FormMagick::Panel::printers [markk 3156]
- Internationalized [markk 3156]
- Converted to AccountDB API. [markk 3156]
- Added tests dir and test suite. Automatically build suite via buildtests.
  [markk 3156]

* Thu Apr 11 2002 Mark Knox <markk@e-smith.com>
- [1.6.1-01]
- rollRPM: Rolled version number to 1.6.1-01. Includes patches up to 1.6.0-02.

* Tue Dec 11 2001 Adrian Chung <adrianc@e-smith.com>
- [1.6.0-02]
- Adding module-load-usb-printer action
- Linking into "local" event.

* Tue Dec 11 2001 Adrian Chung <mac@e-smith.com>
- [1.6.0-01]
- rollRPM: Rolled version number to 1.6.0-01. Includes patches up to 1.5.0-06.

* Wed Nov 14 2001 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-06]
- Add missing hidden state variable in network printer create form.

* Tue Nov 13 2001 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-05]
- Changed "Network Printer (Specify below)" => "Network Printer ..." (thanks
  to DanY for reporting).

* Fri Nov 9 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-04]
- Left-justified smb.conf fragments

* Fri Nov 2 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-03]
- Remove comments from output file and unify indentation

* Thu Oct 25 2001 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-02]
- Break "Add printer" screen into two pages, so that network parameter
  form elements only appear if a network printer is being added.

* Fri Oct 12 2001 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-01]
- Rolled version number to 1.5.0-01. Includes patches upto 1.4.0-04.
- Add missing event directories to tarball - remove mkdirs from %build.

* Fri Oct 12 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-04]
- Add support for /dev/usb/{lp0,lp1}

* Tue Aug 28 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-03]
- Fixed problem with printer-delete expecting wrong type
- Fixed problem with printer-delete script not having "use esmith::db;".

* Fri Aug 17 2001 gordonr
- [1.4.0-02]
- Autorebuild by rebuildRPM

* Wed Aug 8 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-01]
- Rolled version number to 1.4.0-01. Includes patches upto 1.3.0-03.

* Fri Jul 6 2001 Peter Samuel <peters@e-smith.com>
- [1.3.0-03]
- Changed license to GPL

* Wed Apr 11 2001 Adrian Chung <adrianc@e-smith.com>
- [1.3.0-02]
- changing h4 tags to paragraph bold tags.

* Wed Apr 11 2001 Adrian Chung <mac@e-smith.com>
- [1.3.0-01]
- Rolled version number to 1.3.0-01. Includes patches upto 1.2.0-07.

* Mon Feb 12 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-07]
- Change ownership of printspools to lp.lp (not daemon.daemon).
- Remove obsolete :sf: property from /etc/printcap

* Thu Feb  8 2001 Adrian Chung <adrianc@e-smith.com>
- Rolled version to GPG sign package.

* Mon Jan 29 2001 Paul Nesbit <pkn@e-smith.com>
- [1.2.0-05]
- contents of $OUT now being display properly (I claimed it w/ my)

* Mon Jan 29 2001 Paul Nesbit <pkn@e-smith.com>
- [1.2.0-04]
- fixed bug in printcap template (contents of $OUT were not being returned)
- added missing $printer variable to db_get_prop call

* Mon Jan 29 2001 Paul Nesbit <pkn@e-smith.com>
- [1.2.0-03]
- moved printcap template processing from template-begin to 05printers
- recoded to use accounts db instead of printers db
- updated code to use  db utils

* Thu Jan 25 2001 Jason Miller <jmiller@e-smith.com> 
- [1.2.0-02]
- Fixed printer-migrate action to call printer-create-spool
  when it used to say printer-spool-create (a non-existant
  action) as well as a minor compile error regarding db_set 

* Thu Jan 25 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-01]
- Rolled version number to 1.2.0-01. Includes patches upto 1.1.0-04.

* Thu Jan 25 2001 Charlie Brady <charlieb@e-smith.com>
- Migrate "printers" database entries in "accounts" db.
- Iterate over printer entries during post-upgrade (for
  use in restore). "printer-create-spool" event created
  for this, and printer-create script modified so that it
  is non-fatal to run it more than once.
- Replace direct access to hashes to use of esmith::db.

* Tue Jan 23 2001 Gordon Rowell <gordonr@e-smith.com>
- Renamed action scripts to <package>-action form

* Fri Jan 05 2001 Jason Miller <jmiller@e-smith.com>
- updated copyright information and added prototypes
  for all subroutines to avoid the warning messages
  sent to the log files

* Fri Nov 10 2000 Peter Samuel <peters@e-smith.com>
- Rolled version number to 1.1.0. Includes patches up to 0.2-2.

* Mon Oct 30 2000 Charlie Brady <charlieb@e-smith.com>
- Merge services database back into configuration database

* Thu Oct 26 2000 Peter Samuel <peters@e-smith.com>
- Rolled version number to 0.2. Includes patches up to 0.1-17.

* Thu Oct 19 2000 Adrian Chung <adrian.chung@e-smith.com>
- Updated scripts in web/functions directory to pass
  merged configuration/services hash to esmith::cgi
  functions.

* Thu Oct 06 2000 Tony Clayton <tonyc@e-smith.com>
- Fixed require dependency (was e-smith-lib >= 1.0-21)

* Fri Oct 06 2000 Adrian Chung <adrian.chung@e-smith.com>
- Removed %post directive.  Enabling this service is handled
  for now in e-smith-base.
- Added require dependency for e-smith-lib.

* Tue Oct 04 2000 Adrian Chung <adrian.chung@e-smith.com>
- Changed restart action to use serviceControl(restart).

* Tue Oct 04 2000 Adrian Chung <adrian.chung@e-smith.com>
- Changed so that templates are only expanded if service is enabled.

* Tue Oct 03 2000 Charlie Brady <charlieb@e-smith.com>
- Make lpd restart depend on services database.

* Tue Oct 03 2000 Adrian Chung  <mac@e-smith.com>
- Rebuilt on allspice.

* Thu Sep 28 2000 Paul Nesbit  <pkn@e-smith.com>
- updated URL and support contact info

* Tue Sep 26 2000 Peter Samuel <peters@e-smith.com>
- upgraded createlinks to a perl script using standard event_link
-    and panel_link subroutines
- upgraded spec file to use /sbin/e-smith/genfilelist instead of
-    hardwired internal routines
- created /etc/lpd.perms template to tighten security
- added conf-LPRng action to:
-    console-save, network-create and network-delete
- added restart-LPRng action to
-    network-create and network-delete

* Wed Jul 12 2000 Joseph Morrison <jdm@e-smith.net>
- Add -1 argument to split command in case of blank last configuration field

* Tue Jun 13 2000 Charlie Brady <charlieb@e-smith.net>
- Fix missing panel/manager/cgi-bin directory
- Add missing "print command = .." line in smb.conf

* Mon Jun 12 2000 Charlie Brady <charlieb@e-smith.net>
- Add missing conf-LPRng action script
- Fix some broken event symlinks

* Thu Jun 1 2000 Charlie Brady <charlieb@e-smith.net>
- First created - broken out of e-smith-base 4.0.11.

%prep
%setup

%build
perl createlinks
/sbin/e-smith/buildtests 30e-smith-LPRng
touch root/var/service/lpd/down
 
%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    --file /var/service/lpd/run 'attr(0755,root,root)' \
    > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist

%post
rm -f /etc/lpd.perms

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
