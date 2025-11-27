#!/bin/bash
FLASK_ENDPOINT=http://127.0.0.1:5000

rm -rf docs
mkdir -p docs
cp -r static docs/static

curl -s $FLASK_ENDPOINT -o docs/index.html
curl -s $FLASK_ENDPOINT/about -o docs/about.html
curl -s $FLASK_ENDPOINT/consultation -o docs/consultation.html
curl -s $FLASK_ENDPOINT/testimonials -o docs/testimonials.html
curl -s $FLASK_ENDPOINT/blog -o docs/blog.html


