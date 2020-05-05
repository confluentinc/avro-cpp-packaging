PACKAGE_NAME?=	avro-cpp
VERSION?=	1.8.0
VERSION_SUFFIX?=

BUILD_NUMBER?= 1

MOCK_CONFIG?=default

RESULT_DIR?=pkgs-$(VERSION)$(VERSION_SUFFIX)-$(BUILD_NUMBER)-$(MOCK_CONFIG)

all: rpm


SOURCES:
	mkdir -p SOURCES

archive: SOURCES
	cd ../ && \
	git archive --prefix=$(PACKAGE_NAME)-$(VERSION)$(VERSION_SUFFIX)/ \
	  -o rpm/SOURCES/$(PACKAGE_NAME)-$(VERSION)$(VERSION_SUFFIX).tar.gz HEAD


build_prepare: archive
	cp *.patch SOURCES
	mkdir -p $(RESULT_DIR)
	rm -f $(RESULT_DIR)/$(PACKAGE_NAME)*.rpm


srpm: build_prepare
	/usr/bin/mock \
		$(MOCK_OPTIONS) \
		--no-cleanup-after \
		-r $(MOCK_CONFIG) \
		--define "__version $(VERSION)$(VERSION_SUFFIX)" \
		--define "__release $(BUILD_NUMBER)" \
		--resultdir=$(RESULT_DIR) \
		--buildsrpm \
		--spec=$(PACKAGE_NAME).spec \
		--sources=SOURCES
	@echo "======= Source RPM now available in $(RESULT_DIR) ======="

rpm: srpm
	/usr/bin/mock \
		$(MOCK_OPTIONS) \
		--no-cleanup-after \
		-r $(MOCK_CONFIG) \
		--define "__version $(VERSION)$(VERSION_SUFFIX)"\
		--define "__release $(BUILD_NUMBER)"\
		--resultdir=$(RESULT_DIR) \
		--rebuild $(RESULT_DIR)/$(PACKAGE_NAME)*.src.rpm
	@echo "======= Binary RPMs now available in $(RESULT_DIR) ======="

clean:
	rm -rf SOURCES

distclean: clean
	rm -f build.log root.log state.log available_pkgs installed_pkgs \
		*.rpm *.tar.gz
