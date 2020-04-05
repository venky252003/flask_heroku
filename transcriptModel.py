#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from setting import app

import datetime
import json

from sqlalchemy import create_engine  
from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

##db = SQLAlchemy(app)
db_string = "postgres://ADL_ADMIN:P0stg4_2017@10.246.5.211:5444/ADL"

db = create_engine(db_string)  
base = declarative_base()

class Transcript(base):
    __tablename__ = 'transcript'
    id = Column(Integer, primary_key=True)
    file_name = Column(String(150), nullable=False)
    file_path = Column(String(250), nullable=True)
    lanuguage = Column(String(80), nullable=False)
    file_format = Column(String(50), nullable=False)
    text = Column(String(1000), nullable=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    accuracy = Column(Float)

    Session = sessionmaker(db)  
    session = Session()
    base.metadata.create_all(db)
        
    # def json(self):        
	# 	return { 'file_name': self.file_name, 'file_path': self.file_path, 'lanuguage': self.lanuguage, 'file_format': self.file_format, 'text': self.text }

    def add_transcript(_name,_path,_lanuguage,_format,_text,_accuracy):
        new_transcript = Transcript(file_name=_name, file_path=_path, 
                                    lanuguage=_lanuguage,file_format=_format, 
                                    text=_text, accuracy=_accuracy)
        session.add(new_transcript)
        session.commit()

    # def __repr__(self):
	# 	book_object = {
	# 		'file_name': self.file_name,
	# 		'file_path': self.file_path,
	# 		'lanuguage': self.lanuguage,
    #         'file_format': self.file_format,
    #         'text': self.text
	# 	}
	# 	return json.dumps(book_object)