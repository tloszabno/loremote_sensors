
init:
	sudo pip3 install -r requirements.txt


test:
	nosetests3

run:
	sudo python3 app.py >> /home/pi/loremotelogs.txt 2>&1


run-mocked:
	sudo python3 app.py --mocked


clean:
	find . -name "*.pyc" -exec rm -rf {} \;


.PHONY: init test cleans
