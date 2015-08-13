FILES :=                              \
    .travis.yml                       \
    .gitignore                        \
    makefile                          \
    requirements.txt

all:

check:
	@for i in $(FILES);                                         \
    do                                                          \
        [ -e $$i ] && echo "$$i found" || echo "$$i NOT FOUND"; \
    done

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -rf __pycache__

config:
	git config -l

test:
	python ./src/bq_delete.py test_img
	python ./src/bq_upload.py ./tests/test_img1.png
	python ./src/bq_upload.py ./tests/test_img2.jpeg
	python ./src/bq_annotation.py ./tests/test.txt


scripts.html: models.py
	pydoc -w models

bisque-lungMap.log:
	git log > IDB.log

annotation:
	python ./src/bq_annotation.py

dataset:
	python ./src/bq_dataset.py

tag:
	python ./src/bq_tags.py

query:
	python ./src/bq_query.py

