release: python manage.py migrate & vendor/go-ipfs/ipfs init
web: gunicorn ipfs_indexer.wsgi
background: python manage.py process_queue
ipfs: vendor/go-ipfs/ipfs daemon --enable-pubsub-experiment