.PHONY: test
test:
	python setup.py test

.PHONY: clean
clean:
	-rm -rf result_images build dist sample_repo.egg-info
	-find -name '__pycache__' -exec rm -rf '{}' \;
