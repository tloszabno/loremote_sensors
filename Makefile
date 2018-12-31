
init:
	sudo pip install -r requirements.txt


test:
	nosetests

run:
	sudo python2 app.py


run-mocked:
	sudo python2 app.py --mocked


clean:
	find . -name "*.pyc" -exec rm -rf {} \;


.PHONY: init test cleans
