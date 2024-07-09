#!/bin/bash
rpmbuild -bb packaging/pypy-twisted-sockjs-nomock.spec --define "_topdir `pwd`/rpmbuild" --define "_iv_pkg_release 0" --define "gitdir `pwd`" --define "_iv_pkg_version truc"
