release: python manage.py migrate
web: gunicorn ipfs_indexer.wsgi
background: python manage.py process_queue