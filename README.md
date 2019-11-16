acceder al ambiente virtual
    source env/bin/activate

variables de entorno de flask
    FLASK_APP -> ejecutable ".py" del proyecto
    FLASK_ENV -> ambiente de desarrollo (development, production)
las variables de entorno se escriben corriendo
    export FLASK_APP=run.py
    export FLASK_ENV=development

automáticamente generar lista de requerimientos para nuestro proyecto
    pip3 freeze > requirements.txt
Para instalar los requerimientos de del archivo requirements.txt tenemos que correr
    pip3 install -r requirements.txt


VAriables de entorno que podemos modificar en flask
    ENV: development
    DEBUG: True
    TESTING: False
    PROPAGATE_EXCEPTIONS: None
    PRESERVE_CONTEXT_ON_EXCEPTION: None
    SECRET_KEY: None
    PERMANENT_SESSION_LIFETIME: 31 days, 0:00:00
    USE_X_SENDFILE: False
    SERVER_NAME: None
    APPLICATION_ROOT: /
    SESSION_COOKIE_NAME: session
    SESSION_COOKIE_DOMAIN: None
    SESSION_COOKIE_PATH: None
    SESSION_COOKIE_HTTPONLY: True
    SESSION_COOKIE_SECURE: False
    SESSION_COOKIE_SAMESITE: None
    SESSION_REFRESH_EACH_REQUEST: True
    MAX_CONTENT_LENGTH: None
    SEND_FILE_MAX_AGE_DEFAULT: 12:00:00
    TRAP_BAD_REQUEST_ERRORS: None
    TRAP_HTTP_EXCEPTIONS: False
    EXPLAIN_TEMPLATE_LOADING: False
    PREFERRED_URL_SCHEME: http
    JSON_AS_ASCII: True
    JSON_SORT_KEYS: True
    JSONIFY_PRETTYPRINT_REGULAR: False
    JSONIFY_MIMETYPE: application/json
    TEMPLATES_AUTO_RELOAD: None
    MAX_COOKIE_SIZE: 4093