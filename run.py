# run.py
import sys
sys.path.insert(0, '/home/abrahao/Documentos/Dev/Python/API_basica_mysql')

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
