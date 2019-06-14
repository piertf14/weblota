.PHONY: all

clean: clean-pyc
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	find . -name '.DS_Store' -delete
	rm -rf tests/__pycache__

clean-pyc:
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	find . -name '*~' -delete

dbtest:
	dropdb test_gotham || true
	rm backup.sql
	createdb test_gotham
	pg_dump gotham -h localhost --no-owner -v -Fc > backup.dump
	pg_restore -h localhost -p 5432 -d test_gotham -v -Fc backup.dump

test:
	python manage.py test --settings=crehana.settings.test --keepdb

refresh:
	./manage.py sync_plans
	./manage.py upgrade_stripe
