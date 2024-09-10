SOURCE_FOLDER=./intentions

get-project-version:
	@cat .project-version

install-requirements:
	pip3 install \
	    -r requirements/dev.txt \
	    -r requirements/ops.txt \
	    -r requirements/tests.txt

check-code-quality:
	isort $(SOURCE_FOLDER) --diff --check-only
	darglint $(SOURCE_FOLDER)
	ruff check $(SOURCE_FOLDER) --fix
	yamllint .

format:
	isort $(SOURCE_FOLDER)
	ruff check $(SOURCE_FOLDER) --fix
