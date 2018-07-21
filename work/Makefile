#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
AGATE_FILES = ../Agate/RUNME.py

BERYL_FILES = \
    ../Beryl/__init__.py \
    ../Beryl/Ask.py \
    ../Beryl/BerylAnswer.py \
    ../Beryl/Main.py

WORK_FILES = \
    Makefile

FILES = \
    $(AGATE_FILES) \
    $(BERYL_FILES) \
    $(WORK_FILES)


all: clean files links


clean:
	rm -rf __pycache__
	rm -f *.old *.new *.pyc
	rm -f ag.py
	rm -f ba.py bi.py bk.py bm.py
	rm -f files
	rm -f hma1.py hma2.py
	rm -f j1p.py jb.py
	rm -f l.txt
	rm -f m
	rm -f ps3.py
	rm -f rm.py
	rm -f t.java t1.py


files:
	echo $(FILES) >files.1.tmp
	tr ' ' '\n' <files.1.tmp >files.2.tmp
	mv files.2.tmp files


links:
	ln -s ../Agate/RUNME.py                                                     ag.py
	ln -s ../Beryl/BerylAnswer.py                                               ba.py
	ln -s ../Beryl/__init__.py                                                  bi.py
	ln -s ../Beryl/Ask.py                                                       bk.py
	ln -s ../Beryl/Main.py                                                      bm.py
	ln -s ../bin/.pyxie/hma.py                                                  hma1.py
	ln -s ../bin/.pyxie/hma2.py                                                 hma2.py
	ln -s ../Junk/Boot.py                                                       jb.py
	ln -s log.txt                                                               l.txt
	ln -s Makefile                                                              m
	ln -s ../Junk/PortrayString_3.py                                            ps3.py
	ln -s ../Agate/RUNME.py                                                     rm.py
	ln -s test.java                                                             t.java
	ln -s test.py                                                               t1.py


wc:
	#
	#  Excludes $(AGATE_FILES)
	#
	wc -l \
        $(BERYL_FILES) \
        $(WORK_FILES)

test:
	cat \
        $(BERYL_FILES) \
            >test.py
	bash run.sh
