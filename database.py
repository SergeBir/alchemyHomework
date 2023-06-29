from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Создание соединения с базой данных
engine = create_engine('postgresql://postgres: @localhost:5432/homework_db')

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()
