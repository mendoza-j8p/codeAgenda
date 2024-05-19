import fastapi
import logging, json

app = fastapi(__name__)



gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)









if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

