SHELL := /bin/bash

build: --environment --test
	@echo "build done"

# Delete all files in the current directory that are normally created by
# building the program. Also delete files in other directories if they
# are created by this makefile. However, don’t delete the files that
# record the configuration. Also preserve files that could be made by
# building, but normally aren't because the distribution comes with them.

# There is no need to delete parent directories that were created with
# 'mkdir -p', since they could have existed anyway.
clean:
	@echo "clean done"

# Delete all files in the current directory (or created by this makefile)
# that are created by configuring or building the program. If you have
# unpacked the source and built the program without creating any other
# files, ‘make distclean’ should leave only the files that were in the
# distribution. However, there is no need to delete parent directories
# that were created with ‘mkdir -p’, since they could have existed anyway.
distclean:
	@echo "distclean done"

# Like 'clean', but may refrain from deleting a few files that people
# normally don't want to recompile. For example, the 'mostlyclean' target
# for GCC does not delete libgcc.a, because recompiling it is rarely
# necessary and takes a lot of time.
mostlyclean:
	@echo "mostlyclean done"

--test:
	@echo "eu sou privado"

--environment:
	@echo "load docker environment variables"
