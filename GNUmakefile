TOP?=$(shell cd ..; pwd)
START?=$(shell pwd)


all : SCRIPTPROVIDER PYTHONWRAPPER OMIGEN_PY TEST


.phony : SCRIPTPROVIDER
SCRIPTPROVIDER :
	$(MAKE) -C $(START)/provider \
		$(START)/bin/libOMIScriptProvider.so


.phony : PYTHONWRAPPER
PYTHONWRAPPER :
	cd $(START)/python && python2.7 omi_setup.py build


.phony : OMIGEN_PY
OMIGEN_PY :
	$(MAKE) -C $(START)/omigen_py \
		\$(START)/bin/omigen_py


.phony : TEST
TEST :
	$(MAKE) -C \$(START)/test \
		\$(START)/bin/test


.phony : clean
clean :
	$(MAKE) -C \$(START)/provider clean
	cd \$(START)/python && python2.7 omi_setup.py clean
	$(MAKE) -C \$(START)/omigen_py clean
	$(MAKE) -C \$(START)/test clean


.phony : install
install :
	$(MAKE) -C \$(START)/provider install
	cd \$(START)/python && python2.7 omi_setup.py install
	$(MAKE) -C \$(START)/omigen_py install


.phony : release
release : SCRIPTPROVIDER PYTHONWRAPPER OMIGEN_PY
	$(MAKE) -C \$(START)/installbuilder
