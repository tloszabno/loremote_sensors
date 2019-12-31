
init:
	sudo pip3 install -r requirements.txt


test:
	python3 -m "nose"

run:
	sudo python3 app.py > /home/pi/loremotelogs.txt 2> /home/pi/loremotelogs_errors.txt


run-mocked:
	sudo python3 app.py --mocked


clean:
	find . -name "*.pyc" -exec rm -rf {} \;


.PHONY: init test cleans
