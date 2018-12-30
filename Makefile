
init:
	sudo pip install -r requirements.txt


test:
	nosetests

run:
	sudo python app.py


run-mocked:
	sudo python app.py --mocked


clean:
	find . -name "*.pyc" -exec rm -rf {} \;


.PHONY: init test cleans
