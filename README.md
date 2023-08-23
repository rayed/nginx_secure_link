
# NGINX Secure Link Demo


## Setup

    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt


## Run 

    flask run --debug --host=0.0.0.0
    docker run --rm -p 80:80 \
        -v $(PWD)/nginx.conf:/etc/nginx/conf.d/default.conf \
        -v $(PWD)/static:/www/static \
        -v $(PWD)/download:/www/download \
        nginx 