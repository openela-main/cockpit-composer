Name:           cockpit-composer
Version:        45
Release:        1%{?dist}
Summary:        Composer GUI for use with Cockpit

License:        MIT
URL:            http://weldr.io/
Source0:        https://github.com/osbuild/cockpit-composer/releases/download/%{version}/cockpit-composer-%{version}.tar.gz

BuildArch:      noarch

Requires:       cockpit
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 8
Requires: osbuild-composer >= 28
%else
Requires: weldr
Suggests: osbuild-composer >= 28
%endif

%description
Composer generates custom images suitable for deploying systems or uploading to
the cloud. It integrates into Cockpit as a frontend for osbuild.

%prep
%setup -q -n cockpit-composer

%build
# Nothing to build

%install
mkdir -p %{buildroot}/%{_datadir}/cockpit/composer
cp -a public/* %{buildroot}/%{_datadir}/cockpit/composer
mkdir -p %{buildroot}/%{_datadir}/metainfo/
cp -a public/io.weldr.cockpit-composer.metainfo.xml %{buildroot}/%{_datadir}/metainfo/ 

%files
%doc README.md
%license LICENSE.txt
%{_datadir}/cockpit/composer
%{_datadir}/metainfo/*

%changelog
* Wed Mar 15 2023 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 45-1
- New upstream release

* Thu Feb 23 2023 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 44-1
- New upstream release

* Wed Feb 15 2023 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 43-1
- New upstream release

* Mon Nov 28 2022 imagebuilder-bot <imagebuilder-bots+imagebuilder-bot@redhat.com> - 42-1
- New upstream release

* Tue Aug 23 2022 Jacob Kozol <jkozol@redhat.com> - 40-1
- New upstream release

* Fri Aug 19 2022 Jacob Kozol <jkozol@redhat.com> - 39-1
- New upstream release

* Tue Aug 16 2022 Jacob Kozol <jkozol@redhat.com> - 38-1
- New upstream release

* Wed Jul 27 2022 Jacob Kozol <jacobdkozol@gmail.com> - 37-1
- New upstream release

* Thu Feb 24 2022 Jacob Kozol <jacobdkozol@gmail.com> - 35-1
- New upstream release

* Wed Feb 23 2022 Jacob Kozol <jacobdkozol@gmail.com> - 34-1
- New upstream release

* Fri Feb 04 2022 Jacob Kozol <jkozol@redhat.com> - 33-1
- Add support for OCI upload target
- Update translations
- Update dependencies

* Wed Dec 01 2021 Jacob Kozol <jkozol@redhat.com> - 32-1
- Add Edge Raw, RHEL Installer, Edge Simplified Installer image types
- Improve user account modal responsiveness
- Update tests
- Update minor NPM dependencies
- Update translation files

* Thu Aug 26 2021 Jacob Kozol <jkozol@redhat.com> - 31-1
- Add new ostree image types
- Improve loading state when waiting for api responses
- Improve notification system
- Improve test stability
- Update NPM dependencies
- Update translations

* Mon Feb 22 2021 Jacob Kozol <jkozol@redhat.com> - 29-1
- Add ability to upload to VMWare
- Add support for additional ostree parameters
- Update NPM dependencies
- Add and update translations
- Minor test fixes

* Mon Jan 18 2021 Jacob Kozol <jkozol@redhat.com> - 28-1
- Use sentence case rather than title case
- Add and update tests
- Update translations from weblate
- Update minor NPM dependencies

* Thu Dec 10 2020 Jacob Kozol <jkozol@redhat.com> - 27-1
- Sync with upstream release 27
- Add additional form validation for the Create Image Wizard
- Improve page size dropdown styling
- Improve error state messages
- Update pagination component for pf4
- Add wildcards and support for multiple values to input filter
- Update translations

* Wed Jul 15 2020 Jacob Kozol <jkozol@redhat.com> - 22.1-1
- Patternfly imports are standardized to be consistent with cockpit
- Cancel image build button bug fixed
- Empty components state provides a help message
- Wizard component has bug fixes and is refactored for future scalability
- Test updates
- ESLint upgraded to version 7 and the code style is improved
- Translation files are updated from fedora weblate
- Cockpit-composer's dependency on osbuild-composer  is more specific
- Coverity scan is now supported to help improve code quality
- Resolves: #1820539 

* Wed Jun 14 2020 Lars Karlitski <larskarlitski@redhat.com> - 21.1-1
- Support setting parameters (ref and parent) for ostree images
- Loosen restrictions on password strength
- Various UI refinements

* Wed Jun 08 2020 Lars Karlitski <larskarlitski@redhat.com> - 20.1-1
- Migrate to the osbuild-composer backend
- Supports uploading images to AWS and Azure

* Wed Feb 19 2020 Matej Marusak <mmarusak@redhat.com> - 12.1-1
- Fix integration tests, external test repository URL ceased to exist
- Translation updates rhbz#1784453
- Add documentation URL page help menu

* Tue Dec 17 2019 Matej Marusak <mmarusak@redhat.com> - 11-1
- Show depsolve errors on the blueprints page
- Add labels for additional output types (rhbz#1769154)
- Expose Image Builder on /composer, not /welder
- Define a URL for each tab on a blueprint page
- Provide a link in the image creation notification to the Images tab on the blueprint page

* Fri Aug 09 2019 Matej Marusak <mmarusak@redhat.com> - 5-1
- Fix PropTypes for the homepage
- Code clean up for the list of components

* Wed Jul 31 2019 Martin Pitt <mpitt@redhat.com> - 4-1
- Add additional blueprint name validation rhbz#1696415
- Fix images not loading on refresh
- Add notification for source repo deletion
- Fix AppStream ID
- Translation updates

* Wed Jun 26 2019 Martin Pitt <mpitt@redhat.com> - 2-1
- Strip newlines from SSH keys before saving
- Translation updates rhbz#1689979

* Wed Jun 05 2019 Martin Pitt <mpitt@redhat.com> - 1-1
- New version 1
- Translation updates rhbz#1689979

* Mon May 27 2019 Martin Pitt <mpitt@redhat.com> - 0.4-1
- New version 0.4
- Include ability to start lorax-composer rhbz#1708387

* Mon May 06 2019 Martin Pitt <mpitt@redhat.com> - 0.3-1
- New version 0.3
- Add/edit/remove sources
- Remove new line in encrypted password rhbz#1655862
- Resolve issues with changes saved to the workspace

* Mon Apr 15 2019 Martin Pitt <mpitt@redhat.com> - 0.2.1-1
- New version 0.2.1
- Several fixes to User Account creation dialog

* Mon Apr 01 2019 Martin Pitt <mpitt@redhat.com> - 0.2.0-1
- New version 0.2.0
- Include ability to add a user to a blueprint rhbz#1655862

* Mon Feb 11 2019 Martin Pitt <mpitt@redhat.com> - 0.1.8-1
- New version 0.1.8
- Provide visual indication when a blueprint component is a dependency
- Enable Undo to retrieve changes after the Discard Changes action
- Update how blueprint contents are depsolved when contents are added/removed
- Display an error if a component is added that results in a depsolve failure
- Show all versions available for a package
- Provide ability to specify a wildcard version for a package rhbz#1673066

* Fri Dec 14 2018 Brian C. Lane <bcl@redhat.com> - 0.1.7-1
- New version 0.1.7
  Resolves: rhbz#1640184
- Capitalize OpenStack corrently in the image create dialog (anilsson)
- Add AppStream metainfo (mpitt)
- Make cockpit-composer the only package name (mpitt)
- Lots of integration test improvements (henrywangxf)

* Mon Oct 29 2018 Brian C. Lane <bcl@redhat.com> - 0.1.6-1
- New version 0.1.6
  Resolves: rhbz#1640184
- Include spec into release tarball (mpitt)
- Fix a bug in importSanity test. (henrywangxf)
- Add RHEL-X in welder-web test scenarios. (henrywangxf)
- test: Support Cockpit test scenario (mpitt)
- Makefile: Simplify variable defaults (mpitt)
- A big commit to fix random failure on chrome. (henrywangxf)
- Remove inert 'Architecture' field in 'Create Image' dialog (#388) (stefw)
- po: Update from Fedora Zanata (lars)
- Remove ForEach to run two test cases but use two separate cases. If there's
  one case failed, I can find it according to case name. (henrywangxf)
- Wait for delete menu action visable before click it. (henrywangxf)
- test: Drop node installation from vm.install (mpitt)
- Don't clean bots/ directory for VM preparation (mpitt)
- Two improvements: (henrywangxf)
- Go to view blueprint page by clicking blueprint name link instead of by URL.
  That helps improving case stability. (henrywangxf)
- Move sed to test/vm.install from test/run because developers do not normally
  use test/run to trigger tests. (henrywangxf)
- test: Only install node if it isn't already available (mpitt)
- Makefile: bots is not a phony target (mpitt)

* Mon Oct 15 2018 Brian C. Lane <bcl@redhat.com> - 0.1.5-1
- New version 0.1.5
  Related: rhbz#1613058
- Found a code coverage bug and fix it. (henrywangxf)
- Update README.md to support Cockpit CI. (henrywangxf)
- Updates Create Image modal to not have a default image type (jgiardin)
- Add support for Modules during Add/Remove (jgiardin)
- new test: Build mock images and verify download becomes enabled (atodorov)
- Fix flaky issue when running test on chrome (henrywangxf)
- Add selenium debug support. (henrywangxf)
- Creates user-friendly labels to display for image types (jgiardin)
- Compile with code coverage enabled, collect coverage result and upload to codecov.io. (henrywangxf)
- new test: verify stock blueprints from backend are displayed (atodorov)
- Simplify selenium startup again (mpitt)
- Temporarily support selenium images with and without -debug variants (mpitt)
- Fix python string format issue (henrywangxf)
- Remove ugly blank except in tests (henrywangxf)
- README: We're running tests on Cockpit's CI now (lars)
- Fix tests to not exit with non-zero code (#362) (henrywangxf)
- Update Discard Changes to delete workspace (jgiardin)
- Fix test case "Then selected component icon should have border" (henrywangxf)
- Cockpit CI Integration (henrywangxf)
- Display modules in list of selected components (jgiardin)
- pass blueprint data that's expected on save (jgiardin)
- Fix /run/weldr permission issue (henrywangxf)
- Fix end-to-end test cases (henrywangxf)
- po: Update Japanese translations from Zanata (lars)

* Tue Sep 04 2018 Brian C. Lane <bcl@redhat.com> - 0.1.4-1
- New version 0.1.4
  Related: rhbz#1613058
- Adds queue status to an infotip in the Create Image modal (jgiardin)
- Update Create Image modal to also commit unsaved changes (jgiardin)
- Catching a couple of minor issues (jgiardin)
- Update Create Image modal to include blueprint object instead of just name (jgiardin)
- Update Create Image button selector in end-to-end test (jgiardin)
- Display warning messages to the user in Create Image modal (jgiardin)
- use updated property key from api for date created (jgiardin)
- translations: Fail when zanata-js is not installed (lars)
- README.md: Add missing `translations:` (lars)
- translations: remove test target (lars)
- po: Update from Fedora Zanata (lars)
- translations: move po files and scripts to po/ (lars)
- translations: Strip country code when loading react-intl's locale-data (mpitt)
- remove redundant .then(data => data) (jgiardin)
- Add ability to stop builds that are waiting or running (jgiardin)
- Change text from "Delete Build" to "Delete Image" (jgiardin)
- Update Delete Blueprint modal to match layout of Delete Build (jgiardin)
- Fix miscellaneous propType warnings (jgiardin)
- Include confirmation modal for deleting a finished build (jgiardin)
- Swap order of date and type in the Image list item details (jgiardin)
- Add Delete action for Finished composes (jgiardin)
- Add ability to delete Failed builds (jgiardin)
- test_blueprints: Make blueprint selection more robust (lars)
- Use upstream patternfly-react's Tab component (lars)
- Changes en-dash to dash and adds spaces (jgiardin)
- Updates based on a11y review, also simplified i18n format (jgiardin)
- minor tweaks to improve the screen reader experience (jgiardin)
- Makes strings translatable in pagination for available components (jgiardin)
- Update React and enzyme (lars)
- package.json: Use ~ instead of ^ versions for dependencies (lars)
- Drop unused dependencies (lars)
- package.json: update dependencies (lars)
- Remove package-lock.json (lars)

* Wed Aug 29 2018 Brian C. Lane <bcl@redhat.com> - 0.1.3-1
- New version 0.1.3
  Related: rhbz#1613058
- Update Create Image notifications (#328) (jgiardin)
- Make strings translatable in Pending Changes dialog (#341) (jgiardin)
- Makefile: don't run po-pull on dist (lars)
- Add the .spec files to .PHONY (bcl)

* Fri Aug 10 2018 Brian C. Lane <bcl@redhat.com> - 0.1.2-1
- New Version 0.1.2
  Related: rhbz#1613058
- Add the .spec files to .PHONY (bcl)
- Add welder-web and cockpit-composer release instructions (bcl)
- Add a 'tag' target to the Makefile (bcl)
- Adjust image list layout to improve alignment (jgiardin)
- Fix blueprint packages getting added to history (jacobdkozol)
- Fixed bug where startComposeApi would not return start compose response (sfondell)
- Run `make po-push` from travis on pushes to master. (dshea)
- Add a po-push target to the Makefile. (dshea)
- Don't call compose API on the blueprints page (lars)
- Support downloading images (lars)
- Fix fetchComposes() call (lars)
- Update text string (jgiardin)
- add bootstrap class for large modals (jgiardin)
- Fix issues with translated strings and add one more for "Close" (jgiardin)
- Make strings translatable (but includes build error) (jgiardin)
- Update layout (jgiardin)
- Don't show custom sources section if empty (jgiardin)
- Add modal for listing sources (jgiardin)
- Revert "Revert "Add python and gcc to the Dockerfiles."" (dshea)
- Include translations in the dist tarball (dshea)
- Remove the zanata-js crud from package-lock.json (dshea)
- Fix how fetching blueprints/composes is triggered (jacobdkozol)
- Update API calls error messages (jacobdkozol)
- Fix polling issue. Add error action. (jacobdkozol)
- Add loading images from prior sessions and sort by start time. (jacobdkozol)
- Revert "Run `npm rebuild` after `npm install`." (lars)
- Revert "Add python and gcc to the Dockerfiles." (lars)
- Don't update translations on every build (lars)
- Fix yamllint errors on .travis.yml (dshea)
- Add new requirements to the travis environment (dshea)
- Add a script for testing translations. (dshea)
- Run `npm rebuild` after `npm install`. (dshea)
- Make the editBlueprint selector more specific. (dshea)
- Add python and gcc to the Dockerfiles. (dshea)
- Add a i18n section to the README (dshea)
- Create cockpit translation modules. (dshea)
- Extract cockpit manifest strings for translation. (dshea)
- Add translated messages. (dshea)
- Add scripts for interacting with Zanata. (dshea)
- Internationalize strings with react-intl. (dshea)
- Fix PR#309 imported issue. The rpm package should be welder-web*.noarch.rpm, not welder-web*.x86_64.rpm (henrywangxf)
- Build srpm together with rpm (atodorov)
- Images list UI refinements (jgiardin)
- cockpituous-release: Use upstream release-source (martinpitt)
- core: Use escalated privileges to access Lorax API (stefw)
- remove utils from Layout (jgiardin)
- Remove unused Layout components (jgiardin)
- Submit coverage report only if present (atodorov)
- Use default composer dir without --group option (atodorov)
- Fix created image not being added to state (jacobdkozol)
- package.json: Remove bootstrap-select (lars)
- package.json: Update stylelint (lars)
- blueprints: Show actual error message (lars)
- core: propagate errors from cockpitFetch() (lars)

* Tue Jul 10 2018 Brian C. Lane <bcl@redhat.com> - 0.1.1-1
- fixes blueprints end-to-end test (jgiardin)
- Hides Comment feature from Pending Changes modal (jgiardin)
- Remove non-functional UI elements/components (jgiardin)
- fixes line length in unit test (jgiardin)
- update selector for Edit Blueprint button in test (jgiardin)
- fixes empty state on blueprints page and tests (jgiardin)
- fixes spacing errors (jgiardin)
- fixes bad merges during rebase (jgiardin)
- handles error case for fetching blueprints (jgiardin)
- sets timeout on Loading state (jgiardin)
- how did that 'n' get in there? (jgiardin)
- fixes line length (jgiardin)
- Disables actions (jgiardin)
- Updates UI based on state, for loading and error (jgiardin)
- Adds reducer for updating state when an error occurs (jgiardin)
- updates state to hold values for fetch status (jgiardin)
- components: Use consistent syntax for handlers (lars)
- Fix two issues. (henrywangxf)
- test/create.image: simplify shallow wrapper creation (lars)
- CreateImage: don't call unset handlers (lars)
- test/create.image: also conider handleStartCompose (lars)
- correcting the initial state (jgiardin)
- updates mockState in unit tests to match state updates for Filters (jgiardin)
- Merge pull request #250 from larskarlitski/remove-mock-data (jgiardin)
- Remove mock data (lars)
- Add lorax-composer test and remove stand alone welder-web test. (henrywangxf)
- Domain socket support in UI testing. (henrywangxf)
- Update queue status text, Remove cancel button (jacobdkozol)
- Added status icons for imageListView (jacobdkozol)
- Add start compose functionality (jacobdkozol)
- Fix blueprint page issue loading components (jacobdkozol)
- Remove redux persist (jacobdkozol)
- Remove unused code (lars)
- Merge pull request #248 from jgiardino/filter (jgiardin)
- Merge pull request #262 from andreasn/form-control-fx-style (jgiardin)
- Fix style of pagination input under available components (anilsson)
- fix issue when multiple filters are defined (jgiardin)
- implements filtering and refactors toolbars (jgiardin)
